# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class Point(models.Model):
    _name = 'uni.point'
    _description = 'uni point'

    subject = fields.Many2one('uni.subject', string='Tên môn')