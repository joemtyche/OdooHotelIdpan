# -*- coding: utf-8 -*-

#rooms.py


from odoo import models, fields, api

class rooms(models.Model):
    _name = 'hotel.rooms'
    _description = 'Hotel Rooms'
    _order="name"

    name = fields.Char("Room No.")
    description = fields.Char("Room Description")

    roomtype_id = fields.Many2one('hotel.roomtypes', string="Room Type")
    roomtypename=fields.Char("Room Type",related='roomtype_id.name')
    