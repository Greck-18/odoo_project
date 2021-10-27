{
    'name': 'Polish Test',
    'version': '1.1',
    'summary': 'Invoices & Payments',
    'sequence': 2,
    'description': """
Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com/page/billing',
    'images': [],
    'depends': ['base', 'mail'],
    'data': [
        'views/polish_test_views.xml',
        'views/polish_test2_views.xml',
        'wizard/polish_test_entry_wizard_views.xml',
        'views/res_partner_views.xml',
        'security/ir.model.access.csv'

    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
