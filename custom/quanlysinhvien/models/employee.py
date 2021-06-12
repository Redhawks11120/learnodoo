# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class Employee(models.Model):
    _name = 'uni.employee'
    _description = 'uni employee'

    name = fields.Char(string= 'Tên', required=True)
    address = fields.Char(string='Địa chỉ')
    phone = fields.Char(string='Số điện thoại')
    salary = fields.Float(string='Lương')
    gender = fields.Selection(
        [('male','Nam'), ('female', 'Nữ')]
    )
    code = fields.Char(string='CMND/CCCD')
    birthday = fields.Date(string='Ngày sinh')