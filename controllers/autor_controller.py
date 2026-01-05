# controllers/autor_controller.py
# Controlador para operaciones de autores

from models import Autor
from database import db
from sqlalchemy import or_
from sqlalchemy.orm import joinedload

class AutorController:
    """Controlador para operaciones de autores"""

    def __init__(self):
        pass  # No mantener sesión persistente

    def obtener_todos(self):
        """
        Obtiene todos los autores

        Returns:
            list: Lista de objetos Autor
        """
        session = db.get_session()
        try:
            autores = session.query(Autor).options(
                joinedload(Autor.libros)
            ).order_by(Autor.Apellido, Autor.Nombre).all()
            # Expunge objetos para usarlos fuera de la sesión
            for autor in autores:
                session.expunge(autor)
            return autores
        except Exception as e:
            print(f"Error al obtener autores: {e}")
            return []
        finally:
            session.close()

    def obtener_por_id(self, autor_id):
        """
        Obtiene un autor por su ID

        Args:
            autor_id (int): ID del autor

        Returns:
            Autor: Objeto Autor o None
        """
        session = db.get_session()
        try:
            autor = session.query(Autor).options(
                joinedload(Autor.libros)
            ).filter(Autor.AutorID == autor_id).first()
            if autor:
                session.expunge(autor)
            return autor
        except Exception as e:
            print(f"Error al obtener autor: {e}")
            return None
        finally:
            session.close()

    def buscar(self, termino_busqueda):
        """
        Busca autores por nombre, apellido o nacionalidad

        Args:
            termino_busqueda (str): Término de búsqueda

        Returns:
            list: Lista de autores encontrados
        """
        session = db.get_session()
        try:
            autores = session.query(Autor).filter(
                or_(
                    Autor.Nombre.like(f'%{termino_busqueda}%'),
                    Autor.Apellido.like(f'%{termino_busqueda}%'),
                    Autor.Nacionalidad.like(f'%{termino_busqueda}%')
                )
            ).order_by(Autor.Apellido, Autor.Nombre).all()

            for autor in autores:
                session.expunge(autor)
            return autores
        except Exception as e:
            print(f"Error en la búsqueda: {e}")
            return []
        finally:
            session.close()

    def crear(self, datos_autor):
        """
        Crea un nuevo autor

        Args:
            datos_autor (dict): Diccionario con los datos del autor

        Returns:
            tuple: (éxito: bool, mensaje: str, autor_id: int)
        """
        session = db.get_session()
        try:
            # Crear el nuevo autor
            nuevo_autor = Autor(
                Nombre=datos_autor['nombre'],
                Apellido=datos_autor['apellido'],
                Nacionalidad=datos_autor.get('nacionalidad'),
                FechaNacimiento=datos_autor.get('fecha_nacimiento'),
                Biografia=datos_autor.get('biografia')
            )

            session.add(nuevo_autor)
            session.commit()

            autor_id = nuevo_autor.AutorID

            return (True, f"Autor '{nuevo_autor.nombre_completo}' creado exitosamente", autor_id)

        except Exception as e:
            session.rollback()
            return (False, f"Error al crear autor: {e}", None)
        finally:
            session.close()

    def actualizar(self, autor_id, datos_actualizados):
        """
        Actualiza un autor existente

        Args:
            autor_id (int): ID del autor a actualizar
            datos_actualizados (dict): Datos a actualizar

        Returns:
            tuple: (éxito: bool, mensaje: str)
        """
        session = db.get_session()
        try:
            autor = session.query(Autor).filter(Autor.AutorID == autor_id).first()

            if not autor:
                return (False, f"No se encontró el autor con ID {autor_id}")

            # Actualizar campos
            for campo, valor in datos_actualizados.items():
                if hasattr(autor, campo):
                    setattr(autor, campo, valor)

            session.commit()

            return (True, f"Autor '{autor.nombre_completo}' actualizado exitosamente")

        except Exception as e:
            session.rollback()
            return (False, f"Error al actualizar autor: {e}")
        finally:
            session.close()

    def eliminar(self, autor_id):
        """
        Elimina un autor

        Args:
            autor_id (int): ID del autor a eliminar

        Returns:
            tuple: (éxito: bool, mensaje: str)
        """
        session = db.get_session()
        try:
            autor = session.query(Autor).filter(Autor.AutorID == autor_id).first()

            if not autor:
                return (False, f"No se encontró el autor con ID {autor_id}")

            # Verificar si tiene libros asociados
            if autor.libros and len(autor.libros) > 0:
                return (False, f"No se puede eliminar: el autor tiene {len(autor.libros)} libro(s) asociado(s)")

            nombre = autor.nombre_completo
            session.delete(autor)
            session.commit()

            return (True, f"Autor '{nombre}' eliminado exitosamente")

        except Exception as e:
            session.rollback()
            return (False, f"Error al eliminar autor: {e}")
        finally:
            session.close()

    def contar_libros(self, autor_id):
        """
        Cuenta el número de libros de un autor

        Args:
            autor_id (int): ID del autor

        Returns:
            int: Número de libros
        """
        session = db.get_session()
        try:
            autor = session.query(Autor).filter(
                Autor.AutorID == autor_id
            ).first()

            if not autor:
                return 0

            return len(autor.libros) if autor.libros else 0
        except Exception as e:
            print(f"Error al contar libros: {e}")
            return 0
        finally:
            session.close()
