# -*- coding: utf-8 -*-
# Copyright 2017 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Veggie Order Rules',
    'version': '11.0.1.0.1',
    'category': 'Website',
    'author': 'Empero, ',
    'website': '',
    'license': 'AGPL-3',
    'depends': [
        'website_sale',
        'product',
    ],
    'data': [
        'views/pricelist_view.xml',
        'views/cart_template.xml',
    ],
    'installable': True,
}
