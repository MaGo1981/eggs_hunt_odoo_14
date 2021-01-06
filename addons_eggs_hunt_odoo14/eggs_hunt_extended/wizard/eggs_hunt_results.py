from odoo import api, fields, models, _, exceptions
from odoo.exceptions import UserError, ValidationError


class ResultsWizard(models.TransientModel):
    _name = "results.wizard"
    _description = "Eggs Hunt Result Wizard"

    results = fields.Selection([("individual", "Individual"), ("family", "Family"), ("both", "Individual and Family")],  string="Results", default='both')



    def calculate_results(self):
        hunt_id = self.env.context.get('active_id')
        hunt = self.env['eggs.hunt'].browse(hunt_id)
        if self.results == 'individual':
            hunt.write({'results': self.results})
            return hunt.action_individual_results()
        elif self.results == 'family':
            hunt.write({'results': self.results})
            return hunt.action_family_results()
        elif self.results == 'both':
            hunt.write({'results': self.results})
<<<<<<< HEAD
            return (hunt.action_individual_results(), hunt.action_family_results())
=======
            return (hunt.action_family_results(), hunt.action_individual_results()) # family must be first to get the child_ids.
>>>>>>> test-19
        else:
            raise UserError(_('Please select the results you want to calculate!'))

