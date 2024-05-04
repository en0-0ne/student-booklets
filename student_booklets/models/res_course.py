from odoo import fields, models, api


class ResCourse(models.Model):
    _name = 'res.course'
    _description = 'Course'

    name = fields.Char('Name', required=True)
    professor_id = fields.Many2one(
        comodel_name='res.professor',
        string='Professors',
        required=True,
    )
    level_unit_id = fields.Many2one(
        comodel_name='level.unit',
        string='Level Unit',
    )
    level_id = fields.Many2one(
        comodel_name='school.level',
        related='level_unit_id.level_id'
    )
    program_ids = fields.Many2many(
        comodel_name='school.program',
        string='Programs',
        domain="[('child_ids', '=', False)]"
    )
    credit = fields.Integer('Credit')
    coefficient = fields.Float('Coefficient')