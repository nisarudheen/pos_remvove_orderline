odoo.define('pos_clear_orderline.clearline', function(require) {
'use strict';
  const Registries = require('point_of_sale.Registries');
  const Orderline = require('point_of_sale.Orderline')
  const RemoveLine = (Orderline) => class RemoveLine extends Orderline {
  clear_line(){
    console.log(this)
    var order = this.env.pos.get_order();
    order.remove_orderline(order.get_selected_orderline())
  }
  };
Registries.Component.extend(Orderline,RemoveLine);
});
