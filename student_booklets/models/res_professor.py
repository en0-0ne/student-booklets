from odoo import fields, models, api, _


class ResProfessor(models.Model):
    _name = 'res.professor'
    _description = 'Professor'
    _inherits = {'res.partner': 'partner_id'}
    _rec_names_search = ['name', 'registration_number']

    partner_id = fields.Many2one(
        'res.partner',
        string="Partner",
        ondelete="cascade",
        auto_join=True,
        index=True
    )

    registration_number = fields.Char("Registration number", required=True)
    grade = fields.Char("Grade", required=True)

    course_ids = fields.One2many(
        comodel_name='res.course',
        inverse_name='professor_id',
        string='Courses'
    )
    course_count = fields.Integer(string='Course Count', compute='_compute_course_ids')

    @api.depends('course_ids')
    def _compute_course_ids(self):
        for professor in self:
            professor.course_count = len(professor.course_ids)

    def action_view_courses(self):
        return {
            'name': _('Courses taugh by %s') % self.name,
            'view_type': 'tree',
            'view_mode': 'tree',
            'res_model': 'res.course',
            'type': 'ir.actions.act_window',
            'domain': [('professor_id', '=', self.id)],
            'target': 'current',
        }
