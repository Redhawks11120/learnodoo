# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class Employee(models.Model):
    _name = 'hotel.employee'
    _description = 'Hotel Employee'

    name = fields.Char(string='Tên nhân viên', required = True)
    identify = fields.Char(string='CMND/CCCD', required= True)
    gender = fields.Selection(
        [('male', 'Nam'),('female', 'Nữ'), ('other', 'Khác')],
        string='Giới tính', default = 'male', required = True
    )
    salary = fields.Float(string='Lương', required = True)
    images = fields.Binary(string='Ảnh chân dung')