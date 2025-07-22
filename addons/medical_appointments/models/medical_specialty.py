from odoo import models, fields

class MedicalSpecialty(models.Model):
  _name = 'medical.specialty'
  _description = 'Especialidad médica'

  name = fields.Char(string='Nombre', required=True)
  description = fields.Text(string='Descripción')