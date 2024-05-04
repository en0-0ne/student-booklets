from odoo import fields, models, api


class CourseSchedule(models.Model):
    _name = 'course.schedule'
    _description = 'Course Schedule'

    name = fields.Char()
    date_from = fields.Datetime(
        string='Date From',
        required=True,
        default=fields.Datetime.now()
    )
    date_to = fields.Datetime(
        string='Date To',
        required=True,
        default=fields.Datetime.now()
    )
    duration = fields.Float(
        string='Duration'
    )

    course_id = fields.Many2one(
        comodel_name='res.course',
        string='Course',
        required=True
    )
    professor_id = fields.Many2one(
        comodel_name='res.professor',
        related='course_id.professor_id',
        store=True
    )

    state = fields.Selection(
        string='State',
        selection=[
            ('incoming', 'Incoming'),
            ('done', 'Done'),
            ('reported', 'Reported'),
            ('canceled', 'Canceled'),
        ],
        default='incoming',
        required=True
    )

