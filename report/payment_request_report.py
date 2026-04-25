from odoo import models, api

class PaymentRequestReport(models.AbstractModel):
    _name = 'report.account_payment_request.report_payment_request_document'
    _description = 'Payment Request Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        if not docids and data.get('active_ids'):
            docids = data.get('active_ids')
        docs = self.env['account.move'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs,
            'data': data or {},
        }


class PaymentRequestReportA5(models.AbstractModel):
    _name = 'report.account_payment_request.payment_request_a5'
    _description = 'Payment Request Report A5'
    _inherit = 'report.account_payment_request.report_payment_request_document'