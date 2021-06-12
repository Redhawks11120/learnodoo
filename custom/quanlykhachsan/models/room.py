# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from odoo.exceptions import UserError


class Room(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'

    name = fields.Char(string='Tên', required=True)
    price = fields.Float(string='Giá phòng')
    code = fields.Char(string='Mã phòng', required=True)
    type = fields.Selection(
        [('basic', 'Normal'), ('vip', 'Vip'), ('lux', 'Luxury')],
        string='Loại phòng', default='basic', required=True
    )
    view_room = fields.Selection(
        [('sea_view', 'View Biển'), ('mountain_view', 'View Núi'), ('city_view', 'View Thành phố'),
         ('other_view', 'Khác')],
        string="View phòng", required=True
    )
    description = fields.Text(string='Mô tả')
    bed_count = fields.Integer(string='Số giường')
    max_person = fields.Integer(string='Số người tối đa')
    status = fields.Selection(
        [('open', 'Open'), ('close', 'Close'), ('maintain', 'Maintain'), ('stop', 'Stop')],
        default='open', string='Trạng thái'
    )
    images = fields.Binary(string='Hình ảnh')

    _sql_constraints = [
        ('code_room_uniq', 'unique(code,name)', 'Tên và Mã phòng phải là duy nhất'),
    ]

    @api.constrains('max_person')
    def validate_max_person(self):
        if self.max_person < 1:
            raise UserError('Max Person phải lớn hơn 1')

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        if args is None:
            args = []
        if name and operator in ('=', 'ilike', '=ilike', 'like', '=like'):
            domain = ['|', ('name', operator, name), ('code', operator, name)]
            return self.search(domain + args, limit=limit).name_get()
        return super(Room, self).name_search(name, args=args, operator=operator, limit=limit)
