from odoo import fields, models, api


class StudentMark(models.Model):
    _name = 'student.mark'
    _description = 'Mark'

    name = fields.Char('Name')
    student_id = fields.Many2one(
        comodel_name='res.student',
        string='Student',
        required=True
    )
    course_id = fields.Many2one(
        comodel_name='res.course',
        string='Course',
        required=True
    )
    level_unit_id = fields.Many2one(
        related='course_id.level_unit_id'
    )
    level_id = fields.Many2one(
        related='course_id.level_id'
    )
    score = fields.Float('Score', required=True)
