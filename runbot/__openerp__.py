{
    'name': 'Runbot',
    'category': 'Website',
    'summary': 'Runbot',
    'version': '1.0',
    'description': "Runbot",
    'author': 'OpenERP SA',
    'depends': ['website'],
    'external_dependencies': {
        'python': ['matplotlib'],
    },
    'data': [
        'runbot.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
