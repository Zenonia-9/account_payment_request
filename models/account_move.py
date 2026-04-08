from odoo import models
from odoo.exceptions import UserError
from odoo import _

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_open_payment_request(self):
        # ✅ Validation for multiple records
        if not self:
            raise UserError(_("No bills selected."))

        if any(move.state != 'posted' for move in self):
            raise UserError(_("You can only request payment for posted bills."))

        if any(move.move_type == 'entry' for move in self):
            raise UserError(_("Miscellaneous entries are not allowed."))

        # ✅ Return wizard
        return {
            'type': 'ir.actions.act_window',
            'name': 'Payment Request',
            'res_model': 'payment.request.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'active_ids': self.ids,
                'active_model': 'account.move',
            }
        }