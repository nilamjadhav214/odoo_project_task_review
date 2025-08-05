from odoo import models, fields

class TaskReview(models.Model):
    _name = "task.review"
    _description = "Task Review"
    _order = "review_date desc"
    _rec_name = "task_id"

    task_id = fields.Many2one("project.task", string="Task", required=True, ondelete="cascade")
    review_date = fields.Date(string="Review Date", required=True)
    reviewer_id = fields.Many2one("res.users", string="Reviewer", required=True)
    notes = fields.Text(string="Notes")
    score = fields.Selection(
        selection=[(str(i), str(i)) for i in range(1, 6)],
        string="Score",
        required=True,
        help="Score from 1 (worst) to 5 (best)"
    )


