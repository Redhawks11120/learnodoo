# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class Price(models.Model):
    _name = 'hotel.price'
    _description = 'Hotel Price Room'

    room_id = fields.Many2one('hotel.room', string='Phòng')
    code_room = fields.Char(string="Mã Phòng", required=True)
    base_price = fields.Float(string="Giá cơ bản", related='room_id.price')

    preferential_percent = fields.Float(string="Phần trăm ưu đãi")
    days = fields.Float(string="Số ngày thuê", required=True)
    price_service = fields.Float(string="Giá sử dụng các dịch vụ đi kèm", required=True)
    current_price = fields.Float(string="Giá hiện tại", compute="_count_price", store=True)

    @api.depends("base_price", "preferential_percent", "days", "price_service")
    def _count_price(self):
        for price in self:
            if price.preferential_percent == 0 or price.days == 0:
                price.current_price = price.base_price
            elif price.preferential_percent > 0:
                price.current_price = price.base_price * (1 - price.preferential_percent)*price.days+price.price_service
