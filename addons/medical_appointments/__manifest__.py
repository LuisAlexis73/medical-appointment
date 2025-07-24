{
  'name': "Medical Appointment",
  'version': '18.0.0.1',
  'category': 'Medical',
  'summary': 'Gestión de citas médicas',
  'description': 'Permite gestionar especialidades, médicos y citas médicas para pacientes',
  'author': 'Alexis Galarza',
  'depends': ['base', 'calendar', 'contacts', 'hr'],
  'data': [
    'security/ir.model.access.csv',
    'views/medical_appointment_view.xml',
    'views/medical_specialty_view.xml',
  ],
  'installable': True,
  'application': False,
  'auto_install': False
}