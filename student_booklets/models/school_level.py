from odoo import fields, models, api


class SchoolLevel(models.Model):
    _name = 'school.level'
    _description = 'School Level'

    name = fields.Char(required=True)
    color = fields.Integer(default=0)
    # TODO : Add a color fields to set the badge's color on the tree view
