{
    'name': 'Account Payment Request',
    'version': '1.0.5',
    'summary': 'Create and print payment request from vendor bills',
    'description': """
        This module adds a Payment Request button on Vendor Bills.
        It allows users to:
        - Open a wizard to select payment date
        - Mark group requests
        - Print a custom payment request report
        - Handle multiple bills in a single request
    """,

    'author': 'Thein Htoo Aung',

    'category': 'Accounting',
    'license': 'LGPL-3',

    'depends': [
        'account',
        'web',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/payment_request_views.xml',
        'wizard/payment_request_wizard_views.xml',
        'report/paperformat.xml',
        'report/payment_request_layout.xml',
        'report/payment_request_template.xml',
        'report/payment_request_report.xml',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}  #type: ignore
