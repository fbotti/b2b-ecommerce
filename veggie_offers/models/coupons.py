# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

#import logging
#_logger = logging.getLogger(__name__)

class Coupons(models.Model):
    _inherit = 'sale.coupon.program'

    descript = fields.Text(string="Descripción")

    @api.multi
    def get_offers(self):
        offers = self.search([('id','>',0)])

        partner = self.env["res.users"].search([('id', '=', self._context.get("uid"))]).partner_id

        banners = []
        partners = []
        for offer in offers:
            """_logger.info("\n\n\n 1: {} \n 2: {} \n\n\n".format(
                offer.rule_partners_domain,
                offer.rule_products_domain,
                ))"""
            domain = []
            if offer.rule_partners_domain:
                for d in eval(offer.rule_partners_domain):
                    if d not in ["&",'|']:
                        domain.append(tuple(d))
                    else:
                        domain.append(d)
            else:
                domain = [('id','>',0)]
            #_logger.info("\n\n\n domain: {} \n\n\n".format(domain))

            partners = self.env['res.partner'].search(domain).ids
            #_logger.info("\n\n\n Partners: {} \n\n\n".format(partners))

            domain = []
            if offer.rule_products_domain:
                for d in eval(offer.rule_products_domain):
                    if d not in ["&",'|']:
                        domain.append(tuple(d))
                    else:
                        domain.append(d)
            else:
                domain = [('id','>',0)]
            domain.append(('website_published','=',True))
            #_logger.info("\n\n\n domain: {} \n\n\n".format(domain))

            products = self.env['product.product'].search(domain)
            #_logger.info("\n\n\n Products: {} \n\n\n".format(products))

            if partner.id in partners:
                banners.append({
                    "offer": offer,
                    "product": products,
                    "n": len(products),
                })

        #_logger.info("\n\n\n banners: {} \n\n\n".format(banners))
        return banners