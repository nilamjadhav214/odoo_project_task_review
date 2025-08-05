from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    review_count = fields.Integer(string="Review Count", compute="_compute_review_count")

    def _compute_review_count(self):
        for task in self:
            task.review_count = self.env['task.review'].search_count([('task_id', '=', task.id)])

    def action_open_task_reviews(self):
        self.ensure_one()
        return {
            'name': 'Task Reviews',
            'type': 'ir.actions.act_window',
            'res_model': 'task.review',
            'view_mode': 'tree,form',
            'domain': [('task_id', '=', self.id)],
            'context': {'default_task_id': self.id},
        }
