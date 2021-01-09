# -*- coding: utf-8 -*-

{
  "name" : "Eggs Hunt",
  "version" : "0.1",
  "author" : "Marko",
  "category" : "Other",
  "summary": "Eggs Hunt",
  'description':
  """
  Eggs Hunt
  """,
  "depends" : [
    'base',
    'sales_team',
    'portal',
    'web',
    'utm',
    'mail',
    'web',
   ],
  'data': [
    'security/eggs_hunt_security.xml',
      'security/ir.model.access.csv',
      'views/hunt_config_settings_views.xml',
      'views/eggs_hunt_views.xml',
      'views/eggs_hunt_line_views.xml',
      'views/eggs_hunt_line_color_views.xml',
      'views/eggs_hunt_calculate_views.xml',
      'views/eggs_hunt_calculate_colors_views.xml',
      'views/eggs_color_views.xml',
      'data/ir_sequence_data.xml',
      'report/eggs_hunt_reports.xml',
      'report/eggs_hunt_templates.xml',
  ],
  # data files containing optionally loaded demonstration data
  'demo': [
  ],
  'css':[
   ],
  "application": True,
  "installable": True,
}





