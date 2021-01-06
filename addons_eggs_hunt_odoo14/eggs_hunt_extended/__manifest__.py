# -*- coding: utf-8 -*-
{
    'name': "Eggs Hunt Extended",

    'summary':
        """
        Eggs Hunt Extended
        """,

    'description': """
        Eggs Hunt Extended
    """,

    'author': "Marko",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'eggs_hunt',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/eggs_hunt_results_views.xml',
        'views/eggs_hunt_views.xml',
        'views/eggs_hunt_line_views.xml',
        'views/res_partner_views.xml',
        'views/eggs_hunt_result_views.xml',
        'report/eggs_hunt_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
