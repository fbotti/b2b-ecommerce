# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.http import request
from odoo.tools.translate import _

import logging
_logger = logging.getLogger(__name__)


class WebsiteSale2(http.Controller):


    @http.route(['/shop/cart/compare'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update_json(self, **kw):

        order = request.website.sale_get_order()
        partner = order.partner_id

        values = {
            'send': False,
            'send_2': True,
            'order': order,
        }
        cont = False
        #_logger.info("\n\n\n {} \n\n\n".format(order))
        if partner.property_product_pricelist:
            values['min'] = str(partner.property_product_pricelist.min_amount_total)
            if order.amount_total >= partner.property_product_pricelist.min_amount_total:
                values['send'] = True
            else:
                for line in order.order_line:
                    for item in line.product_id.item_ids:
                        if partner.property_product_pricelist.id == item.pricelist_id.id:
                            if line.product_uom_qty >= item.min_quantity:
                                values['send'] = True
                                break
                    if values['send'] == True:
                        break
            #values['message'][0].format(partner.property_product_pricelist.min_amount_total)
        else:
            values['send'] = True

        products = {}
        for line in order.order_line:
            if line.product_id.pack_veggie_id:
                if line.product_id.pack_veggie_id not in products:
                    products[line.product_id.pack_veggie_id] = {
                        "qty": int(line.product_uom_qty),
                        "total": line.product_id.pack_veggie_id.min_qty_pack,
                    }
                else:
                    products[line.product_id.pack_veggie_id]['qty'] += int(line.product_uom_qty)
        for p in products:
            #_logger.info("\n\n\n p: {} \n\n\n".format(products))
            #_logger.info("\n\n\n p: {} \n\n\n".format(products[p]['qty'] % products[p]['total']))
            #_logger.info("\n\n\n p: {} \n\n\n".format(type(products[p]['qty'] / products[p]['total'])))
            if products[p]['qty'] % products[p]['total'] != 0:
                values['send_2'] = False

        return values