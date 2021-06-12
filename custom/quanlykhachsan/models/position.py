# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from odoo.exceptions import ValidationError
from datetime import date

class Position(models.Model):
    _name = 'hotel.position'
    _description = 'Hotel Position'

    name = fields.Char(string='Tên chức vụ')
    description = fields.Text(string= 'Mô tả')