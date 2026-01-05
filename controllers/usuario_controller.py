# controllers/usuario_controller.py
# Controlador para operaciones de usuarios

from models import Usuario, Prestamo
from database import db
from sqlalchemy.orm import joinedload

class UsuarioController:
    """Controlador para operaciones de usuarios"""

    def __init__(self):
        self.session = None

    def _get_session(self):
        """Obtiene una sesión de base de datos"""
        if not self.session:
            self.session = db.get_session()
        return self.session

    def _close_session(self):
        """Cierra la sesión actual"""
        if self.session:
            self.session.close()
            self.session = None

    def obtener_todos(self, solo_activos=True):
        """
        Obtiene todos los usuarios

        Args:
            solo_activos (bool): Si es True, solo retorna usuarios activos

        Returns:
            list: Lista de usuarios
        """
        try:
            session = self._get_session()
            query = session.query(Usuario).options(
                joinedload(Usuario.prestamos)
            )

            if solo_activos:
                query = query.filter(Usuario.Estado == 'Activo')

            usuarios = query.all()

            # Detach from session
            for usuario in usuarios:
                session.expunge(usuario)

            return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return []
        finally:
            self._close_session()

    def obtener_por_id(self, usuario_id):
        """Obtiene un usuario por su ID"""
        try:
            session = self._get_session()
            usuario = session.query(Usuario).options(
                joinedload(Usuario.prestamos)
            ).filter(Usuario.UsuarioID == usuario_id).first()

            if usuario:
                session.expunge(usuario)

            return usuario
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            return None
        finally:
            self._close_session()

    def obtener_por_carnet(self, numero_carnet):
        """Obtiene un usuario por su número de carnet"""
        try:
            session = self._get_session()
            usuario = session.query(Usuario).filter(
                Usuario.NumeroCarnet == numero_carnet
            ).first()
            return usuario
        except Exception as e:
            print(f"Error al obtener usuario: {e}")
            return None
        finally:
            self._close_session()

    def crear(self, datos_usuario):
        """
        Crea un nuevo usuario

        Args:
            datos_usuario (dict): Datos del usuario

        Returns:
            tuple: (éxito: bool, mensaje: str, usuario_id: int)
        """
        session = self._get_session()

        try:
            nuevo_usuario = Usuario(
                NumeroCarnet=datos_usuario['numero_carnet'],
                Nombre=datos_usuario['nombre'],
                Apellido=datos_usuario['apellido'],
                Email=datos_usuario['email'],
                Telefono=datos_usuario.get('telefono'),
                Direccion=datos_usuario.get('direccion'),
                Estado='Activo'
            )

            session.add(nuevo_usuario)
            session.commit()

            usuario_id = nuevo_usuario.UsuarioID

            return (True, f"Usuario '{nuevo_usuario.nombre_completo}' creado exitosamente", usuario_id)

        except Exception as e:
            session.rollback()
            return (False, f"Error al crear usuario: {e}", None)
        finally:
            self._close_session()

    def actualizar(self, usuario_id, datos_actualizados):
        """Actualiza un usuario existente"""
        session = self._get_session()

        try:
            usuario = session.query(Usuario).filter(Usuario.UsuarioID == usuario_id).first()

            if not usuario:
                return (False, f"No se encontró el usuario con ID {usuario_id}")

            for campo, valor in datos_actualizados.items():
                if hasattr(usuario, campo):
                    setattr(usuario, campo, valor)

            session.commit()

            return (True, f"Usuario '{usuario.nombre_completo}' actualizado exitosamente")

        except Exception as e:
            session.rollback()
            return (False, f"Error al actualizar usuario: {e}")
        finally:
            self._close_session()

    def desactivar(self, usuario_id):
        """Desactiva un usuario (no lo elimina)"""
        return self.actualizar(usuario_id, {'Estado': 'Inactivo'})

    def activar(self, usuario_id):
        """Activa un usuario"""
        return self.actualizar(usuario_id, {'Estado': 'Activo'})

    def obtener_prestamos_activos(self, usuario_id):
        """Obtiene los préstamos activos de un usuario"""
        try:
            session = self._get_session()

            prestamos = session.query(Prestamo).filter(
                Prestamo.UsuarioID == usuario_id,
                Prestamo.Estado == 'Prestado'
            ).all()

            return prestamos
        except Exception as e:
            print(f"Error al obtener préstamos: {e}")
            return []
        finally:
            self._close_session()
