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
   ],
  'data': [
      'views/hunt_config_settings_views.xml',
      'views/eggs_hunt_views.xml',
      'views/eggs_hunt_line_views.xml',
      'views/eggs_hunt_line_color_views.xml',
      'views/eggs_hunt_calculate_views.xml',
      'views/eggs_hunt_calculate_colors_views.xml',
      'views/eggs_color_views.xml',
      'security/ir.model.access.csv',
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





