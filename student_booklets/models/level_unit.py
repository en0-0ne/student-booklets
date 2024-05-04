from odoo import fields, models, api


class LevelUnit(models.Model):
    _name = 'level.unit'
    _description = 'Level Unit'

    name = fields.Char('Name')
    course_ids = fields.One2many(
        comodel_name='res.course',
        inverse_name='level_unit_id',
        string='Courses'
    )
    level_id = fields.Many2one(
        comodel_name='school.level',
        string='Level',
        required=True
    )
    is_valid = fields.Boolean('Validity')
    average = fields.Float('Average')