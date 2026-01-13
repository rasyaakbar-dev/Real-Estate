# -*- coding: utf-8 -*-
{
    'name': "Card Reader System",

    'summary': "Sistem pembacaan kartu fisik dengan card reader",

    'description': """
    Sistem manajemen kartu fisik dengan card reader
    - Kelola data kartu (Card UID)
    - Pencatatan setiap pembacaan kartu
    - API untuk card reader
    - Log aktivitas pembacaan
    """,

    'author': "Muhammad Sulthan",
    'website': "ABMATUKAM",

    'category': 'Tools',
    'version': '1.0',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/card_views.xml',
        'views/card_reading_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
}

