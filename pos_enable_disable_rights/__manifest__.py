# -*- coding: utf-8 -*-
{
    'name': "POS Enable/Disable Features",

    'summary': """This module allows you to enable/disable change price, discount and refund buttons per user.
        """,

    'description': """ 
        
    """,

    'author': "Abdelmalik Yousif",
    'sequence': 1,
    'website': "",
    'category': 'Generic Modules',
    'version': '1.0',
    'price': 18.0,
    'currency': 'EUR',
    'depends': ['point_of_sale'],


    'data': [
        'views/res_users_view.xml',
        'views/malik_v.xml',
    ],
    'images': [
        'static/description/pos_interface.png',
    ],

    'demo': [
        #'demo/demo.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
