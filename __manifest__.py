{'name': 'Clear Orderline',
 'version': '16.0.1.0.0',
 'sequence': -1,
 'category': 'all',
 'installable': True,
 'application': True,
 'auto_install': False,
 'depends': ['base','point_of_sale'],
 'data': [
 ],
 'assets':{
  'point_of_sale.assets':[
  'pos_clear_orderline/static/src/js/pos_inherit.js',
   'pos_clear_orderline/static/src/js/order_line.js',
   'pos_clear_orderline/static/src/xml/pos_orderline.xml',
   'pos_clear_orderline/static/src/xml/pos_inherit.xml'
 ]
     }
 }