# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models

class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    min_amount_total = fields.Float(string="Min Purchase Amount")



class ProductPricelist(models.Model):
    _inherit = 'product.template'

    product_pack_veggie = fields.One2many("product.template", 'pack_veggie_id', string="Pack of Products")
    pack_veggie_id = fields.Many2one("product.template", string="In pack")
    min_qty_pack = fields.Integer("Products in Pack")
    is_a_pack = fields.Boolean("Is a Pack")