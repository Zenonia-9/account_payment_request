from odoo import api, models


def _get_payment_request_report_values(report_model, docids, data=None):
    data = data or {}
    if not docids and data.get('active_ids'):
        docids = data.get('active_ids')

    docs = report_model.env['account.move'].browse(docids).exists()
    return {
        'doc_ids': docs.ids,
        'doc_model': 'account.move',
        'docs': docs,
        'data': data,
    }


class PaymentRequestReport(models.AbstractModel):
    _name = 'report.account_payment_request.report_payment_request_document'
    _description = 'Payment Request Report'
    _table = 'apr_report_payment_request'
    _auto = False

    @api.model
    def _get_report_values(self, docids, data=None):
        return _get_payment_request_report_values(self, docids, data=data)


class PaymentRequestReportA5(models.AbstractModel):
    _name = 'report.account_payment_request.payment_request_a5'
    _description = 'Payment Request Report A5'
    _table = 'apr_report_payment_request_a5'
    _auto = False

    @api.model
    def _get_report_values(self, docids, data=None):
        return _get_payment_request_report_values(self, docids, data=data)
