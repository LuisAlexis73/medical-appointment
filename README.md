# **⚠️ Proyecto en desarrollo**

> Este repositorio está en fase de desarrollo activo y **aún no ha sido lanzado a producción**. Las funcionalidades, documentación y estructura pueden cambiar sin previo aviso.

---

# 🏥 Sistema de Reservas Médicas - Odoo 18

Este proyecto es una aplicación web para la gestión de **reservas médicas**, desarrollada sobre **Odoo 18**. Permite a los usuarios reservar turnos médicos de forma sencilla, administrar pacientes y profesionales, y gestionar horarios de atención.

## 🚀 Tecnologías utilizadas

- **Odoo 18**: Framework ERP para la lógica de negocio y gestión.
- **PostgreSQL**: Base de datos relacional.
- **Docker & Docker Compose**: Orquestación y despliegue local.

## 🧪 Funcionalidades principales

- Gestión de turnos médicos.
- Administración de pacientes y profesionales.
- Configuración de horarios y disponibilidad.
- Interfaz amigable para la carga y modificación de datos.

---

## ⚙️ Instalación y puesta en marcha

### ✅ Requisitos previos

- [Docker Desktop](https://docs.docker.com/get-docker/) instalado.

### 🚨 Primer uso

1. Clona este repositorio:

   ```bash
   git clone https://github.com/LuisAlexis73/medical-appointment.git
   cd medical-appointment
   ```

2. Crea el archivo `.env` a partir del archivo `.env.example`.

3. Agrega el flag `-i base` luego de `odoo -d odoo_db` en el archivo `docker-compose.yml` al iniciar el contenedor por primera vez. Luego el flag `-i base` debe quitarse del comando, ya que este indicador recrea la base de datos.

4. Levanta el entorno local:

   ```bash
   docker-compose up -d
   ```

5. Accede al portal de Odoo:
   ```
   http://localhost:8069
   ```

#### ⚠️ Posibles problemas

- Si el puerto 8069 está ocupado, modifícalo en `docker-compose.yml` o dentro del archivo `.env`.
- Verifica los permisos de los volúmenes para evitar errores de escritura.

### 📁 Estructura del proyecto

```
├── docker-compose.yml   # Orquestador de servicios
├── config               # Configuración de Odoo
├── addons               # Módulos personalizados
├── .env                 # Variables de entorno
├── README.md            # Documentación del proyecto
```

### 🛠️ Personalización y desarrollo

- Agrega tus módulos personalizados en la carpeta `addons`.
- Verifica que cada módulo tenga su archivo `__manifest__.py` correctamente configurado.
- Para instalar nuevos módulos, sigue la documentación oficial de Odoo.

### 🤝 Contribución

¿Quieres colaborar? ¡Genial! Por favor, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu mejora/bugfix.
3. Envía un pull request describiendo los cambios.

### 📚 Recursos adicionales

- [Documentación Odoo](https://www.odoo.com/documentation/18.0/)
- [Documentación Docker](https://docs.docker.com/)
- [Guía rápida para módulos Odoo](https://www.odoo.com/documentation/18.0/reference/addons.html)

### Contacto

Para consultas, sugerencias o reportes de errores, por favor abre un [issue](https://github.com/LuisAlexis73/medical-appointment/issues) en este repositorio.  
De esta manera, tu aporte podrá ayudar a otros usuarios y facilitar el seguimiento de las respuestas.
Si tienes alguna duda o sugerencia, no dudes en contactarme en `luisalexisgalarza73@gmail.com`.

## 📝 Licencia

Este proyecto está licenciado bajo la [LGPLv3](https://www.gnu.org/licenses/lgpl-3.0.en.html).
