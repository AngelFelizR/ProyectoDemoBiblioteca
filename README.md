# 📚 Sistema de Gestión de Biblioteca - Práctica de Maestría

## Descripción del Proyecto

Sistema completo de gestión de biblioteca desarrollado en Python con SQL Server, implementando el patrón de diseño MVC (Model-View-Controller) y utilizando SQLAlchemy como ORM. Incluye tanto una interfaz de consola como una aplicación web con Flask.

## 🎯 Objetivos de Aprendizaje

- Conexión y manipulación de bases de datos SQL Server desde Python
- Uso de ORMs (Object-Relational Mapping) con SQLAlchemy
- Implementación del patrón de diseño MVC
- Desarrollo de aplicaciones web con Flask
- Operaciones CRUD completas
- Manejo de transacciones y errores

## 📋 Prerrequisitos

### Software Necesario

1. **Python 3.8 o superior**
   - Descargar desde: https://www.python.org/downloads/

2. **SQL Server 2016 o superior**
   - SQL Server Express (gratuito): https://www.microsoft.com/sql-server/sql-server-downloads
   - SQL Server Developer Edition (gratuito para desarrollo)

3. **SQL Server Management Studio (SSMS)**
   - Descargar desde: https://docs.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms

4. **ODBC Driver for SQL Server**
   - Windows: Generalmente ya está instalado
   - Linux: Seguir instrucciones en https://docs.microsoft.com/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server

5. **Editor de Código** (recomendado)
   - Visual Studio Code: https://code.visualstudio.com/
   - PyCharm Community: https://www.jetbrains.com/pycharm/

## 🚀 Instalación

### Paso 1: Clonar o Descargar el Proyecto

```bash
# Si tienes Git instalado
git clone <url-del-repositorio>
cd biblioteca-practica

# O simplemente descarga y descomprime el archivo ZIP
```

### Paso 2: Crear Entorno Virtual

Se recomienda usar un entorno virtual para aislar las dependencias:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

Si tienes problemas con pyodbc, puedes necesitar instalar Visual C++ Build Tools en Windows:
https://visualstudio.microsoft.com/visual-cpp-build-tools/

### Paso 4: Configurar SQL Server

#### Opción A: Autenticación de Windows (Recomendada para desarrollo local)

1. Abrir SQL Server Management Studio (SSMS)
2. Conectar usando autenticación de Windows
3. Ejecutar el script `biblioteca_setup.sql`

#### Opción B: Autenticación SQL Server

1. Abrir SSMS
2. Habilitar autenticación mixta en el servidor:
   - Clic derecho en el servidor → Properties → Security
   - Seleccionar "SQL Server and Windows Authentication mode"
   - Reiniciar el servicio de SQL Server

3. Crear un usuario SQL:
```sql
CREATE LOGIN biblioteca_user WITH PASSWORD = 'Password123!';
USE BibliotecaDB;
CREATE USER biblioteca_user FOR LOGIN biblioteca_user;
ALTER ROLE db_owner ADD MEMBER biblioteca_user;
```

4. Ejecutar el script `biblioteca_setup.sql`

### Paso 5: Configurar la Conexión

Editar el archivo `config.py` con tus credenciales:

```python
# Para Autenticación Windows
use_windows_auth = True

# Para Autenticación SQL Server
use_windows_auth = False
USERNAME = 'biblioteca_user'
PASSWORD = 'Password123!'
SERVER = 'localhost'  # o 'localhost\SQLEXPRESS'
```

### Paso 6: Verificar la Instalación

```bash
# Probar la conexión básica
python modulo1_conexion_basica.py

# Probar el ORM
python modulo2_orm_sqlalchemy.py
```

## 📁 Estructura del Proyecto

```
biblioteca-practica/
│
├── biblioteca_setup.sql          # Script de creación de BD
├── config.py                      # Configuración de conexión
├── database.py                    # Configuración SQLAlchemy
├── requirements.txt               # Dependencias Python
├── README.md                      # Este archivo
│
├── GUIA_PRACTICA_BIBLIOTECA.md   # Guía completa de la práctica
│
├── modulo1_conexion_basica.py    # Módulo 1: Conexión con pyodbc
├── modulo2_orm_sqlalchemy.py     # Módulo 2: SQLAlchemy ORM
│
├── models/                        # Capa de Modelo
│   ├── __init__.py
│   └── models.py                  # Definición de modelos
│
├── controllers/                   # Capa de Controlador
│   ├── __init__.py
│   ├── libro_controller.py
│   ├── usuario_controller.py
│   └── prestamo_controller.py
│
├── views/                         # Capa de Vista (Consola)
│   ├── __init__.py
│   └── console_view.py
│
├── main.py                        # Aplicación MVC de consola
│
├── app.py                         # Aplicación web Flask
│
├── templates/                     # Templates HTML
│   ├── base.html
│   ├── index.html
│   ├── libros/
│   ├── usuarios/
│   └── prestamos/
│
└── static/                        # Archivos estáticos
    ├── css/
    │   └── style.css
    └── js/
        └── main.js
```

## 🎓 Cómo Usar Esta Práctica

### Para Estudiantes

1. **Leer la guía completa** en `GUIA_PRACTICA_BIBLIOTECA.md`
2. **Completar los módulos en orden**:
   - Módulo 1: Conexión básica con pyodbc
   - Módulo 2: ORM con SQLAlchemy
   - Módulo 3: Implementación del patrón MVC
   - Módulo 4: Aplicación web con Flask

3. **Realizar los ejercicios** propuestos en cada módulo
4. **Completar el proyecto final integrador**

### Para Profesores

- La guía incluye objetivos claros de aprendizaje
- Ejercicios progresivos de dificultad incremental
- Rúbrica de evaluación detallada
- Estimación de tiempo: 40-50 horas

## 🏃‍♂️ Ejecución

### Aplicación de Consola (MVC)

```bash
python main.py
```

### Aplicación Web (Flask)

```bash
python app.py
```

Luego abrir el navegador en: http://localhost:5000

## 📚 Módulos de la Práctica

### Módulo 1: Conexión Básica
- Conexión a SQL Server con pyodbc
- Consultas SQL básicas
- Operaciones CRUD simples
- Manejo de parámetros y prevención de SQL Injection

### Módulo 2: SQLAlchemy ORM
- Definición de modelos
- Relaciones entre tablas
- Consultas con el ORM
- Operaciones CRUD con objetos

### Módulo 3: Patrón MVC
- Separación de responsabilidades
- Controllers (lógica de negocio)
- Views (presentación)
- Models (datos)

### Módulo 4: Aplicación Web
- Flask framework
- Templates Jinja2
- Rutas y vistas
- Formularios y validación
- API REST básica

## 🔧 Solución de Problemas

### Error: "pyodbc.InterfaceError: ('IM002'...)"

**Problema**: Driver ODBC no instalado o no encontrado

**Solución**:
- Windows: Descargar e instalar ODBC Driver 17 para SQL Server
- Verificar el nombre del driver en config.py

### Error: "Cannot open database..."

**Problema**: Base de datos no creada o no accesible

**Solución**:
1. Verificar que SQL Server esté corriendo
2. Ejecutar el script `biblioteca_setup.sql` en SSMS
3. Verificar el nombre del servidor en config.py

### Error de Autenticación

**Problema**: Usuario o contraseña incorrectos

**Solución**:
1. Verificar credenciales en config.py
2. Verificar que el usuario tenga permisos en la base de datos
3. Para Windows Auth, verificar que el usuario de Windows tenga acceso

### Error: "ModuleNotFoundError: No module named..."

**Problema**: Dependencias no instaladas

**Solución**:
```bash
pip install -r requirements.txt
```

### Puerto 5000 ya en uso (Flask)

**Solución**:
```python
# En app.py, cambiar el puerto
app.run(debug=True, port=5001)
```

## 📖 Recursos Adicionales

### Documentación Oficial
- [Python](https://docs.python.org/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [Flask](https://flask.palletsprojects.com/)
- [SQL Server](https://docs.microsoft.com/sql/)
- [pyodbc](https://github.com/mkleehammer/pyodbc/wiki)

### Tutoriales Recomendados
- [Real Python - SQLAlchemy ORM](https://realpython.com/python-sqlalchemy-orm/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [SQL Server Tutorial](https://www.sqlservertutorial.net/)

### Videos
- [Python + SQL Server (YouTube)](https://www.youtube.com/results?search_query=python+sql+server+tutorial)
- [SQLAlchemy Tutorial (YouTube)](https://www.youtube.com/results?search_query=sqlalchemy+tutorial)
- [Flask Tutorial (YouTube)](https://www.youtube.com/results?search_query=flask+tutorial)

## 🤝 Contribuciones

Si encuentras errores o tienes sugerencias para mejorar esta práctica:

1. Reporta issues con detalle
2. Propón mejoras en la documentación
3. Comparte tus implementaciones exitosas

## 📝 Licencia

Este material es para uso educativo en el contexto de cursos de maestría.

## 👨‍🏫 Contacto

Para dudas sobre la práctica, consultar con el profesor del curso.

---

## ✅ Checklist de Completitud

- [ ] Base de datos creada y poblada
- [ ] Módulo 1: Conexión básica funcionando
- [ ] Módulo 2: ORM implementado correctamente
- [ ] Módulo 3: Patrón MVC aplicado
- [ ] Módulo 4: Aplicación web funcional
- [ ] Todos los ejercicios completados
- [ ] Código documentado
- [ ] Tests básicos implementados (bonus)
- [ ] README del proyecto personal

---

**Versión**: 1.0  
**Fecha**: Noviembre 2025  
**Nivel**: Maestría en Ciencias de la Computación / Ingeniería de Software

¡Éxito en tu práctica! 🚀📚
