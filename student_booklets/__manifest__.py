# -*- coding: utf-8 -*-
{
    'name': "Student Booklets",
    'summary': """
        Student cursus management made for college    
    """,
    'description': """
        This module is made especially for managing and supervising all
        students cursus during its 
    """,
    'author': "DevTitans Go",
    'website': "https://gitlab.com/devtitans-go",
    'category': 'Education',
    'version': '0.1',
    'depends': [
        'base',
        'contacts'
    ],

    'data': [
        'security/ir.model.access.csv',
        # data
        'data/ir_sequence.xml',
        # views
        'views/res_student_views.xml',
        'views/res_professor_views.xml',
        'views/res_course_views.xml',
        'views/level_unit_views.xml',
        'views/student_mark_views.xml',
        'views/student_result_views.xml',
        'views/student_subscription_views.xml',
        'views/school_level_views.xml',
        'views/school_program_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'student_booklets/static/src/scss/*.scss',
        ],
    },
    'license': 'LGPL-3',
}
