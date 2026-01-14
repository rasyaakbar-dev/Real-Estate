{
    'name': "Real Estate",
    'version': '1.0.0',
    'depends': ['base'],
    'author': "Rasya A.N",
    'category': 'Sales',
    'summary': "Module for managing real estate properties",
    'description': """
This module allows you to manage real estate properties with various attributes,
including offers, tags, and property types.
    """,
    'website': "https://github.com/rasyaakbar-dev/Real-Estate",
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menu.xml',
    ],
}
