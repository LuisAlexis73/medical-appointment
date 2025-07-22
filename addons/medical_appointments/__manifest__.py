{
  'name': "Medical Appointment",
  'version': '18.0.0.1',
  'category': 'Medical',
  'summary': 'Gestión de citas médicas',
  'description': 'Permite gestionar especialidades, médicos y citas médicas para pacientes',
  'author': 'Alexis Galarza',
  'depends': ['base', 'calendar', 'contacts', 'portal', 'web'],
  'data': [
    'security/ir.model.access.csv',
    'views/medical_appointment_view.xml',
    'views/medical_specialty_view.xml',
  ],
  'instalable': True,
  'application': False,
  'auto_install': False
}