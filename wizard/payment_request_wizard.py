from odoo import models, fields, api
from odoo.exceptions import UserError


class PaymentRequestWizard(models.TransientModel):
    _name = 'payment.request.wizard'
    _description = 'Payment Request Wizard'

    payment_date = fields.Date(
        string="Request Date",
        required=True,
        default=fields.Date.context_today
    )

    group_request = fields.Boolean(
        string="Group Request"
    )

    paper_size = fields.Selection(
        [
            ('a4', 'A4'),
            ('a5', 'A5'),
        ],
        string="Paper Size",
        default='a4',
        required=True
    )

    # Optional: show total amount (nice UX)
    total_amount = fields.Monetary(
        string="Total Amount",
        currency_field='currency_id',
        readonly=True
    )

    currency_id = fields.Many2one(
        'res.currency',
        string="Currency",
        readonly=True
    )

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)

        active_ids = self.env.context.get('active_ids', [])
        moves = self.env['account.move'].browse(active_ids)

        # Default group_request: True if multiple bills
        res['group_request'] = len(active_ids) > 1

        if len(active_ids) <= 5:
            res['paper_size'] = 'a5'
        else:
            res['paper_size'] = 'a4'

        # Optional UX: show total
        if moves:
            res['total_amount'] = sum(moves.mapped('amount_total'))
            res['currency_id'] = moves[0].currency_id.id

        return res

    def action_confirm(self):
        active_ids = self.env.context.get('active_ids')

        if not active_ids:
            raise UserError("No Vendor Bills selected.")

        moves = self.env['account.move'].browse(active_ids)

        # Safety check (like Pay button)
        if any(move.state != 'posted' for move in moves):
            raise UserError("You can only request payment for posted bills.")

        report_ref = (
            'account_payment_request.action_payment_request_report_a5'
            if self.paper_size == 'a5'
            else 'account_payment_request.action_payment_request_report'
        )

        return self.env.ref(report_ref).report_action(
            self.env['account.move'].browse(active_ids),
            data={
                'payment_date': self.payment_date,
                'payment_date_display': self._format_report_date(self.payment_date),
                'group_request': self.group_request,
                'active_ids': active_ids,
            }
        )

    @api.model
    def _format_report_date(self, date_value):
        date_value = fields.Date.to_date(date_value)
        if not date_value:
            return ""
        return date_value.strftime("%d-%b-%Y")
