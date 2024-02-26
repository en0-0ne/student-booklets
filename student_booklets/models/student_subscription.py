from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class StudentSubscription(models.Model):
    _name = 'student.subscription'
    _description = 'Student subscription'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(readonly=True, default=lambda self: _('New'))
    student_id = fields.Many2one(
        comodel_name='res.student',
        string='Student',
        required=True
    )
    active = fields.Boolean(default=True)

    year_from = fields.Selection(
        string='Year from',
        selection='_get_years',
        required=True,
        default=lambda x: str(fields.Date.today().year)
    )
    year_to = fields.Selection(
        string="Year to",
        selection='_get_years',
        default=lambda x: str(fields.Date.today().year + 1),
        required=True
    )
    level_id = fields.Many2one(
        comodel_name='school.level',
        string='Level',
        required=True
    )

    # TODO : Use the module 'document' if possible to wrap those following files in ir.attachment
    deposit_slip = fields.Binary("Deposit slip")
    subscription_request = fields.Binary("Subscription request")
    information_sheet = fields.Binary("Information sheet")

    # Only for re-registration
    discharge = fields.Binary("Discharge")

    state = fields.Selection(
        string='State',
        selection=[
            ('draft', 'Draft'),
            ('on_hold', 'On hold'),
            ('valid', 'Valid'),
            ('canceled', 'Canceled'),
            ('closed', 'Closed'),
        ],
        required=True,
        default='draft'
    )

    def _get_years(self):
        return [(str(i), i) for i in range(fields.Date.today().year - 5, fields.Date.today().year + 6)]

    @api.onchange('year_from')
    def onchange_year_from(self):
        self.year_to = str(int(self.year_from) + 1)

    def action_set_to_draft(self):
        self.state = 'draft'

    def action_on_hold(self):
        self.state = 'on_hold'

    def action_confirm(self):
        self.check_one_validated_subscription_per_student()
        self.student_id.subscription_id = self.id
        self.state = 'valid'

    def action_cancel(self):
        self.write({
            'state': 'canceled'
        })

    def action_close(self):
        self.write({
            'state': 'closed',
            'active': False
        })

    @api.model
    def create(self, values):
        if values.get('name', _('New')) == _('New'):
            values['name'] = "{}/{}-{}".format(
                self.env['ir.sequence'].next_by_code('student.subscription.seq'),
                values['year_from'],
                values['year_to']
            )
        return super(StudentSubscription, self).create(values)

    def check_one_validated_subscription_per_student(self):
        self.ensure_one()
        existing_subscription = self.search([
            ('student_id', '=', self.student_id.id),
            ('state', '=', 'valid'),
            ('id', '!=', self.id)
        ], limit=1)
        if existing_subscription:
            raise ValidationError(_(
                "There is already a validated subscription."
            ))


