from odoo import fields, models, api


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
