# controllers/prestamo_controller.py
# Controlador para operaciones de préstamos

from models import Prestamo, Libro, Usuario
from database import db
from datetime import datetime, timedelta
from sqlalchemy.orm import joinedload

class PrestamoController:
    """Controlador para operaciones de préstamos"""

    def __init__(self):
        self.session = None
        self.DIAS_PRESTAMO_DEFAULT = 14
        self.MULTA_POR_DIA = 10.00  # Multa en pesos por día de retraso

    def _get_session(self):
        if not self.session:
            self.session = db.get_session()
        return self.session

    def _close_session(self):
        if self.session:
            self.session.close()
            self.session = None

    def crear_prestamo(self, libro_id, usuario_id, dias_prestamo=None):
        """
        Crea un nuevo préstamo

        Args:
            libro_id (int): ID del libro
            usuario_id (int): ID del usuario
            dias_prestamo (int): Días de duración (default: 14)

        Returns:
            tuple: (éxito: bool, mensaje: str, prestamo_id: int)
        """
        session = self._get_session()

        try:
            # Verificar que el libro existe y está disponible
            libro = session.query(Libro).filter(Libro.LibroID == libro_id).first()
            if not libro:
                return (False, f"No se encontró el libro con ID {libro_id}", None)

            if libro.CopiasDisponibles <= 0:
                return (False, f"No hay copias disponibles de '{libro.Titulo}'", None)

            # Verificar que el usuario existe y está activo
            usuario = session.query(Usuario).filter(Usuario.UsuarioID == usuario_id).first()
            if not usuario:
                return (False, f"No se encontró el usuario con ID {usuario_id}", None)

            if usuario.Estado != 'Activo':
                return (False, f"El usuario '{usuario.nombre_completo}' no está activo", None)

            # Verificar si el usuario tiene préstamos vencidos
            prestamos_vencidos = session.query(Prestamo).filter(
                Prestamo.UsuarioID == usuario_id,
                Prestamo.Estado == 'Prestado',
                Prestamo.FechaDevolucionEsperada < datetime.now().date()
            ).count()

            if prestamos_vencidos > 0:
                return (False, f"El usuario tiene {prestamos_vencidos} préstamo(s) vencido(s)", None)

            # Crear el préstamo
            dias = dias_prestamo or self.DIAS_PRESTAMO_DEFAULT
            fecha_devolucion = (datetime.now() + timedelta(days=dias)).date()

            nuevo_prestamo = Prestamo(
                LibroID=libro_id,
                UsuarioID=usuario_id,
                FechaPrestamo=datetime.now(),
                FechaDevolucionEsperada=fecha_devolucion,
                Estado='Prestado',
                Multa=0
            )

            # Actualizar copias disponibles
            libro.CopiasDisponibles -= 1

            session.add(nuevo_prestamo)
            session.commit()

            prestamo_id = nuevo_prestamo.PrestamoID

            return (True, f"Préstamo creado exitosamente. Devolver antes del {fecha_devolucion}", prestamo_id)

        except Exception as e:
            session.rollback()
            return (False, f"Error al crear préstamo: {e}", None)
        finally:
            self._close_session()

    def devolver_libro(self, prestamo_id):
        """
        Procesa la devolución de un libro

        Args:
            prestamo_id (int): ID del préstamo

        Returns:
            tuple: (éxito: bool, mensaje: str, multa: float)
        """
        session = self._get_session()

        try:
            prestamo = session.query(Prestamo).filter(
                Prestamo.PrestamoID == prestamo_id
            ).first()

            if not prestamo:
                return (False, f"No se encontró el préstamo con ID {prestamo_id}", 0)

            if prestamo.Estado == 'Devuelto':
                return (False, "Este préstamo ya fue devuelto", 0)

            # Calcular multa si hay retraso
            fecha_actual = datetime.now()
            multa = 0

            if fecha_actual.date() > prestamo.FechaDevolucionEsperada:
                dias_retraso = (fecha_actual.date() - prestamo.FechaDevolucionEsperada).days
                multa = dias_retraso * self.MULTA_POR_DIA

            # Actualizar préstamo
            prestamo.FechaDevolucionReal = fecha_actual
            prestamo.Estado = 'Devuelto'
            prestamo.Multa = multa

            # Actualizar copias disponibles del libro
            libro = session.query(Libro).filter(Libro.LibroID == prestamo.LibroID).first()
            libro.CopiasDisponibles += 1

            session.commit()

            mensaje = "Libro devuelto exitosamente"
            if multa > 0:
                mensaje += f". Multa por retraso: ${multa:.2f}"

            return (True, mensaje, multa)

        except Exception as e:
            session.rollback()
            return (False, f"Error al devolver libro: {e}", 0)
        finally:
            self._close_session()

    def obtener_prestamos_activos(self):
        """Obtiene todos los préstamos activos"""
        try:
            session = self._get_session()
            prestamos = session.query(Prestamo).options(
                joinedload(Prestamo.usuario),
                joinedload(Prestamo.libro).joinedload(Libro.autor),
                joinedload(Prestamo.libro).joinedload(Libro.categoria)
            ).filter(
                Prestamo.Estado == 'Prestado'
            ).all()

            # Detach from session
            for prestamo in prestamos:
                session.expunge(prestamo)

            return prestamos
        except Exception as e:
            print(f"Error al obtener préstamos activos: {e}")
            return []
        finally:
            self._close_session()

    def obtener_prestamos_vencidos(self):
        """Obtiene todos los préstamos vencidos"""
        try:
            session = self._get_session()
            prestamos = session.query(Prestamo).options(
                joinedload(Prestamo.usuario),
                joinedload(Prestamo.libro).joinedload(Libro.autor),
                joinedload(Prestamo.libro).joinedload(Libro.categoria)
            ).filter(
                Prestamo.Estado == 'Prestado',
                Prestamo.FechaDevolucionEsperada < datetime.now().date()
            ).all()

            # Detach from session
            for prestamo in prestamos:
                session.expunge(prestamo)

            return prestamos
        except Exception as e:
            print(f"Error al obtener préstamos vencidos: {e}")
            return []
        finally:
            self._close_session()

    def obtener_por_id(self, prestamo_id):
        """Obtiene un préstamo por su ID"""
        try:
            session = self._get_session()
            prestamo = session.query(Prestamo).filter(
                Prestamo.PrestamoID == prestamo_id
            ).first()
            return prestamo
        except Exception as e:
            print(f"Error al obtener préstamo: {e}")
            return None
        finally:
            self._close_session()

    def obtener_por_libro(self, libro_id):
        """Obtiene todos los préstamos de un libro específico"""
        try:
            session = self._get_session()
            prestamos = session.query(Prestamo).options(
                joinedload(Prestamo.usuario),
                joinedload(Prestamo.libro)
            ).filter(
                Prestamo.LibroID == libro_id
            ).order_by(Prestamo.FechaPrestamo.desc()).all()

            # Detach from session
            for prestamo in prestamos:
                session.expunge(prestamo)

            return prestamos
        except Exception as e:
            print(f"Error al obtener préstamos del libro: {e}")
            return []
        finally:
            self._close_session()
