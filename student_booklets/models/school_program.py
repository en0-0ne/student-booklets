from odoo import fields, models, api, _


class SchoolProgram(models.Model):
    _name = 'school.program'
    _description = 'School Program'
    _rec_name = 'acronym'

    name = fields.Char(required=True)
    acronym = fields.Char(string='Acronym', required=True)
    parent_id = fields.Many2one(
        'school.program',
        'Parent program',
        ondelete='restrict',
        index=True
    )
    parent_path = fields.Char(index=True)
    child_ids = fields.One2many(
        'school.program',
        'parent_id',
        'Child Programs'
    )

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError(_("Error! You cannot create recursive categories."))
