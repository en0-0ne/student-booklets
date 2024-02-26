from odoo import fields, models, api


class StudentResult(models.Model):
    _name = 'student.result'
    _description = 'Mark'

    name = fields.Char('Name')
    student_id = fields.Many2one(
        comodel_name='res.student',
        string='Student',
        required=True
    )
    level_id = fields.Many2one(
        comodel_name='school.level',
        string='Level',
        required=True
    )
    line_ids = fields.Many2many(
        comodel_name='student.mark',
        string='Mark Lines'
    )
    total_mark = fields.Float("Total Marks")
    total_coefficient = fields.Float("Total Coefficient")
    average = fields.Float('Average', required=True)
    status = fields.Selection(
        string='Status',
        selection=[
            ('pass', 'Pass'),
            ('fail', 'Fail')
        ]
    )

