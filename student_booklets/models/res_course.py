from odoo import fields, models, api


class ResCourse(models.Model):
    _name = 'res.course'
    _description = 'Course'

    name = fields.Char('Name')
    professor_ids = fields.Many2many(
        comodel_name='res.professor',
        string='Professors'
    )
    level_unit_id = fields.Many2one(
        comodel_name='level.unit',
        string='Level Unit',
    )
    level_id = fields.Many2one(
        comodel_name='school.level',
        related='level_unit_id.level_id'
    )
    coefficient = fields.Integer('Coefficient')