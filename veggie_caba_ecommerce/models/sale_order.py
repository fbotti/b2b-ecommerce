# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def get_deuda_total(self, partner):
        orders = self.search([
                ('partner_id','=',partner.id),
                ('state','in',['draft','sent'])
            ])
        deuda = 0
        for o in orders:
            deuda += o.amount_total
        return deuda


    @api.multi
    def in_caba(self, partner):
        _logger.info("\n\n\n deuda: {} \n\n\n".format(partner.state_id))
        if partner.state_id.id in [
            self.env.ref("base.state_ar_c").id, 
            self.env.ref("base.state_ar_b").id]:
            return True
        else:
            return False