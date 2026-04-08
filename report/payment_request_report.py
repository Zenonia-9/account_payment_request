from odoo import models

class PaymentRequestReport(models.AbstractModel):
    _name = 'report.account_payment_request.report_payment_request_document'
    _description = 'Payment Request Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['account.move'].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': 'account.move',
            'docs': docs,
            'data': data or {},  # 👈 THIS FIXES YOUR ERROR
        }