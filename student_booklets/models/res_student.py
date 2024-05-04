# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ResStudent(models.Model):
    _name = 'res.student'
    _description = 'Student'
    _inherits = {'res.partner': 'partner_id'}
    _rec_names_search = ['name', 'registration_number']

    partner_id = fields.Many2one(
        'res.partner',
        string='Related partner',
        ondelete="cascade",
        auto_join=True,
        index=True
    )

    registration_number = fields.Char("Registration number", required=True)
    subscription_number = fields.Char("Subscription number")

    birthday = fields.Date("Birthday", default=fields.Date.today())
    birthplace = fields.Char("Birthplace")
    # TODO : Must be computed
    age = fields.Integer("Age")

    father_name = fields.Char("Father's name")
    mother_name = fields.Char("Mother's name")

    cin = fields.Char("CIN")
    cin_issue_date = fields.Char("Issue's date")
    cin_issue_place = fields.Char("Issue's place")

    subscription_ids = fields.One2many(
        comodel_name='student.subscription',
        inverse_name='student_id',
        string='Subscriptions',
        required=False
    )
    subscription_id = fields.Many2one(
        comodel_name='student.subscription',
        string='Current subscription',
        # compute='get_active_subscription',
        # search='_search_subscription',
        # store=True
    )
    subscription_ok = fields.Boolean(compute='_compute_subscription_status', default=False)

    year_from = fields.Selection(
        string='Year from',
        related='subscription_id.year_from'
    )
    year_to = fields.Selection(
        string='Year to',
        related='subscription_id.year_to'
    )
    level_id = fields.Many2one(
        comodel_name='school.level',
        string='Level',
        related='subscription_id.level_id'
    )
    program_id = fields.Many2one(
        comodel_name='school.program',
        string='Program',
        related='subscription_id.program_id'
    )

    mark_ids = fields.One2many(
        comodel_name='student.mark',
        inverse_name='student_id',
        string='Marks'
    )

    def _search_subscription(self, operator, value):
        if operator == 'like':
            operator = 'ilike'
            subscription_name = self.env['student.subscription'].search([('name', operator, value)], limit=None)
        return [('name', operator, subscription_name.name)]

    def action_to_subscription_history(self):
        return {
            'name': _('Subscriptions for %s') % self.name,
            'view_type': 'tree',
            'view_mode': 'tree,form',
            'res_model': 'student.subscription',
            'type': 'ir.actions.act_window',
            'domain': [('student_id', '=', self.id)],
            'target': 'current',
        }

    def action_view_mark(self):
        return {
            'name': _('Marks of %s') % self.name,
            'view_type': 'tree',
            'view_mode': 'tree,form',
            'res_model': 'student.mark',
            'type': 'ir.actions.act_window',
            'domain': [('student_id', '=', self.id), ('level_id', '=', self.level_id.id)],
            'target': 'current',
        }

    # @api.depends('subscription_ids')
    # def get_active_subscription(self):
    #     for record in self:
    #         current_subscription = False
    #         if len(record.subscription_ids) > 0:
    #             current_subscription = record.subscription_ids.filtered(lambda sub: sub.active and sub.state == 'valid')
    #         record.subscription_id = current_subscription

    @api.depends('subscription_id')
    def _compute_subscription_status(self):
        for record in self:
            record.subscription_ok = True if record.subscription_id and record.subscription_id.state == 'valid' else False


