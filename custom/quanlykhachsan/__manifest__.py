# -*- coding: utf-8 -*-

{
    'name': 'Quản lý khách sạn',
    'version': '0.1',
    'author': 'Đinh Ngọc Đức',
    'category': 'PTIT Application',
    'license': 'AGPL-3',
    'sequence': 1,
    'summary': 'Quản lý khách sạn',
    'description': """Mô tả quản lý khách sạn""",
    'website': '',
    'depends': ['base'],
    'data': [
        'security/hotel_security.xml',
        'security/ir.model.access.csv',
        'views/room.xml',
    ],
    'demo': [ ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
