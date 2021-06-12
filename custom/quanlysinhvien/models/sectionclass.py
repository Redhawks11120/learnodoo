# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions

class SectionClass(models.Model):
    _name = 'uni.sectionclass'
    _description = 'uni sectionclass'

    teacher = fields.Many2one('uni.teacher', string='Tên giảng viên')
    subject = fields.Many2one('uni.subject', string='Tên môn học')
    room = fields.Integer(string='Phòng học')