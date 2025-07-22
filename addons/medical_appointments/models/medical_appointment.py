from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class MedicalAppointment(models.Model):
  _name = 'medical.appointment'
  _description = 'Cita médica'
  _order = 'start_datetime'

  patient_id = fields.Many2one('res.partner', string='Paciente', required=True, domain="[('is_company', '=', False)]")
  doctor_id = fields.Many2one('hr.employee', string='Doctor', required=True)
  specialty_id = fields.Many2one('medical.specialty', string='Especialidad', required=True)
  start_datetime = fields.Datetime(string='Inicio de la cita', required=True)
  end_datetime = fields.Datetime(string='Fin de la cita', required=True)
  reason = fields.Text(string='Motivo de la consulta')
  state = fields.Selection([
    ('draft', 'Borrador'),
    ('confirmed', 'Confirmada'),
    ('cancelled', 'Cancelada')
  ], string='Estado', default='draft')
  calendar_event_id = fields.Many2one('calendar.event', string='Evento en calendario', readonly=True, copy=False)

  @api.constrains('start_datetime', 'end_datetime', 'doctor_id')
  def _check_overlapping_appointments(self):
    for rec in self:
      if not (rec.start_datetime and rec.end_datetime and rec.doctor_id and rec.doctor_id._origin):
        continue

      if rec.start_datetime >= rec.end_datetime:
        raise ValidationError('La hora de inicio debe ser menor a la hora de fin')

      overlapping = self.search([
        ('id', '!=', rec.id),
        ('doctor_id', '=', rec.doctor_id.id),
        ('start_datetime', '<', rec.end_datetime),
        ('end_datetime', '>', rec.start_datetime),
        ('state', '!=', 'cancelled')
      ])

      if overlapping:
        raise ValidationError('El doctor ya tiene una cita programada para ese horario')

  @api.constrains('patient_id', 'start_datetime')
  def _check_patient_daily_limit(self):
    for rec in self:
      if not (rec.start_datetime and rec.patient_id and rec.patient_id._origin):
        continue

      start_day = rec.start_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
      end_day = start_day + timedelta(days=1)

      appointments = self.search_count([
        ('id', '!=', rec.id),
        ('patient_id', '=', rec.patient_id.id),
        ('start_datetime', '>=', start_day),
        ('start_datetime', '<', end_day),
        ('state', '!=', 'cancelled')
      ])

      if appointments >= 2:
        raise ValidationError('El paciente no puede tener mas de 2 citas programadas para el mismo dia')

  def action_confirm_appointment(self):
    for rec in self:
      if rec.state != 'draft':
        continue

      if not (rec.doctor_id and rec.doctor_id._origin and rec.patient_id and rec.patient_id._origin):
        raise ValidationError('Debe seleccionar un paciente y un doctor antes de confirmar la cita.')

      user = rec.doctor_id.user_id
      if not user:
        raise ValidationError('El doctor debe tener un usuario asignado.')

      event = self.env['calendar.event'].create({
        'name': f'Cita con {rec.patient_id.name}',
        'start': rec.start_datetime,
        'stop': rec.end_datetime,
        'user_id': user.id,
        'partner_ids': [(4, rec.patient_id.id)],
        'description': rec.reason or '',
        'allday': False,
      })
      rec.calendar_event_id = event.id
      rec.state = 'confirmed'