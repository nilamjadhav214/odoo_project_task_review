{
    "name": "Project Task Review",
    "version": '16.0',
    "category": "Project",
    "summary": "Add reviews to project tasks with scores",
    "author": "Nilam Jadhav",
    "depends": ["project"],
    
    'data': [
        'security/ir.model.access.csv',
        'views/task_review_views.xml',
        'views/project_task_views.xml'
    ],
    
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
