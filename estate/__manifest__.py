{
    'name': "Real Estate",

    'summary': "Module for managing real estate properties",

    'description': """
    This module allows you to manage real estate properties with various attributes
    """,

    'author': "Rasya A.N",
    'website': "https://github.com/rasyaakbar-dev/Real-Estate",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Marketing',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'application': True,
}

