# 🏥 Sistema de Reservas Médicas - Odoo 18

Este proyecto es una aplicación web para la gestión de **reservas médicas**, desarrollada sobre **Odoo 18**. Está diseñada para permitir a los usuarios realizar reservas de turnos médicos de forma simple, mientras que los administradores pueden gestionar pacientes, profesionales de la salud y la disponibilidad de horarios desde un entorno centralizado.

## 🚀 Tecnologías utilizadas

- **Odoo 18**: Framework de ERP para la lógica de negocio y gestión del sistema.
- **PostgreSQL**: Base de datos relacional utilizada por Odoo.
- **Docker & Docker Compose**: Para la orquestación y despliegue local de los servicios.

## 🧪 Funcionalidades principales

- Gestión de turnos médicos.
- Administración de pacientes y profesionales.
- Configuración de horarios y disponibilidad.
- Interfaz amigable para la carga y modificación de datos.

---

## ⚙️ Cómo levantar el entorno local

### ✅ Requisitos previos

- Tener instalado [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/install/)

### 🚨 Primer uso

1. Cloná este repositorio:

   ```bash
   git clone https://github.com/LuisAlexis73/medical-appointment.git
   cd medical-appointment
   ```

2. Crea el archivo `.env` a partir del archivo `.env.example`.

3. Levanta el entorno local:

   ```bash
   docker-compose up -d
   ```

4. Accedé al portal de Odoo:
   ```bash
   http://localhost:8069
   ```

### 📁 Estructura del proyecto

├── docker-compose.yml # Orquestador de servicios
├── odoo # Volumen persistente para Odoo
├── postgres # Volumen persistente para PostgreSQL
├── addons # Módulos personalizados (si aplica)
└── README.md

### Notas

- El archivo `.env` contiene las variables de entorno necesarias para el funcionamiento del entorno local.
- El archivo `docker-compose.yml` define los servicios necesarios para el funcionamiento del entorno local.
- El usuario y contraseña por defecto pueden configurarse en el `docker-compose.yml` o bien en el primer inicio de sesión.
- Si estas desarrollando módulos personalizados, puedes agregarlos en el archivo `addons`. Asegurate de que el archivo `__manifest__.py` tenga los campos necesarios para que el módulo se pueda instalar correctamente.

### Contacto

Si tienes alguna duda o sugerencia, no dudes en contactarme en [luisalexis73@gmail.com](mailto:luisalexis73@gmail.com).

## 📝 Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).
