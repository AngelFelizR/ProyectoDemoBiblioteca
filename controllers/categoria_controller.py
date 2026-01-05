# controllers/categoria_controller.py
# Controlador para operaciones de categorías

from models import Categoria
from database import db
from sqlalchemy.orm import joinedload

class CategoriaController:
    """Controlador para operaciones de categorías"""

    def __init__(self):
        pass  # No mantener sesión persistente

    def obtener_todos(self):
        """
        Obtiene todas las categorías

        Returns:
            list: Lista de objetos Categoria
        """
        session = db.get_session()
        try:
            categorias = session.query(Categoria).options(
                joinedload(Categoria.libros)
            ).order_by(Categoria.NombreCategoria).all()
            # Expunge objetos para usarlos fuera de la sesión
            for categoria in categorias:
                session.expunge(categoria)
            return categorias
        except Exception as e:
            print(f"Error al obtener categorías: {e}")
            return []
        finally:
            session.close()

    def obtener_por_id(self, categoria_id):
        """
        Obtiene una categoría por su ID

        Args:
            categoria_id (int): ID de la categoría

        Returns:
            Categoria: Objeto Categoria o None
        """
        session = db.get_session()
        try:
            categoria = session.query(Categoria).options(
                joinedload(Categoria.libros)
            ).filter(Categoria.CategoriaID == categoria_id).first()
            if categoria:
                session.expunge(categoria)
            return categoria
        except Exception as e:
            print(f"Error al obtener categoría: {e}")
            return None
        finally:
            session.close()

    def buscar(self, termino_busqueda):
        """
        Busca categorías por nombre

        Args:
            termino_busqueda (str): Término de búsqueda

        Returns:
            list: Lista de categorías encontradas
        """
        session = db.get_session()
        try:
            categorias = session.query(Categoria).filter(
                Categoria.NombreCategoria.like(f'%{termino_busqueda}%')
            ).order_by(Categoria.NombreCategoria).all()

            for categoria in categorias:
                session.expunge(categoria)
            return categorias
        except Exception as e:
            print(f"Error en la búsqueda: {e}")
            return []
        finally:
            session.close()

    def crear(self, datos_categoria):
        """
        Crea una nueva categoría

        Args:
            datos_categoria (dict): Diccionario con los datos de la categoría

        Returns:
            tuple: (éxito: bool, mensaje: str, categoria_id: int)
        """
        session = db.get_session()
        try:
            # Verificar si ya existe una categoría con ese nombre
            categoria_existente = session.query(Categoria).filter(
                Categoria.NombreCategoria == datos_categoria['nombre_categoria']
            ).first()

            if categoria_existente:
                return (False, "Ya existe una categoría con ese nombre", None)

            # Crear la nueva categoría
            nueva_categoria = Categoria(
                NombreCategoria=datos_categoria['nombre_categoria'],
                Descripcion=datos_categoria.get('descripcion')
            )

            session.add(nueva_categoria)
            session.commit()

            categoria_id = nueva_categoria.CategoriaID

            return (True, f"Categoría '{nueva_categoria.NombreCategoria}' creada exitosamente", categoria_id)

        except Exception as e:
            session.rollback()
            return (False, f"Error al crear categoría: {e}", None)
        finally:
            session.close()

    def actualizar(self, categoria_id, datos_actualizados):
        """
        Actualiza una categoría existente

        Args:
            categoria_id (int): ID de la categoría a actualizar
            datos_actualizados (dict): Datos a actualizar

        Returns:
            tuple: (éxito: bool, mensaje: str)
        """
        session = db.get_session()
        try:
            categoria = session.query(Categoria).filter(
                Categoria.CategoriaID == categoria_id
            ).first()

            if not categoria:
                return (False, f"No se encontró la categoría con ID {categoria_id}")

            # Verificar si el nuevo nombre ya existe (si se está cambiando)
            if 'NombreCategoria' in datos_actualizados:
                categoria_existente = session.query(Categoria).filter(
                    Categoria.NombreCategoria == datos_actualizados['NombreCategoria'],
                    Categoria.CategoriaID != categoria_id
                ).first()

                if categoria_existente:
                    return (False, "Ya existe otra categoría con ese nombre")

            # Actualizar campos
            for campo, valor in datos_actualizados.items():
                if hasattr(categoria, campo):
                    setattr(categoria, campo, valor)

            session.commit()

            return (True, f"Categoría '{categoria.NombreCategoria}' actualizada exitosamente")

        except Exception as e:
            session.rollback()
            return (False, f"Error al actualizar categoría: {e}")
        finally:
            session.close()

    def eliminar(self, categoria_id):
        """
        Elimina una categoría

        Args:
            categoria_id (int): ID de la categoría a eliminar

        Returns:
            tuple: (éxito: bool, mensaje: str)
        """
        session = db.get_session()
        try:
            categoria = session.query(Categoria).filter(
                Categoria.CategoriaID == categoria_id
            ).first()

            if not categoria:
                return (False, f"No se encontró la categoría con ID {categoria_id}")

            # Verificar si tiene libros asociados
            if categoria.libros and len(categoria.libros) > 0:
                return (False, f"No se puede eliminar: la categoría tiene {len(categoria.libros)} libro(s) asociado(s)")

            nombre = categoria.NombreCategoria
            session.delete(categoria)
            session.commit()

            return (True, f"Categoría '{nombre}' eliminada exitosamente")

        except Exception as e:
            session.rollback()
            return (False, f"Error al eliminar categoría: {e}")
        finally:
            session.close()

    def contar_libros(self, categoria_id):
        """
        Cuenta el número de libros en una categoría

        Args:
            categoria_id (int): ID de la categoría

        Returns:
            int: Número de libros
        """
        session = db.get_session()
        try:
            categoria = session.query(Categoria).filter(
                Categoria.CategoriaID == categoria_id
            ).first()

            if not categoria:
                return 0

            return len(categoria.libros) if categoria.libros else 0
        except Exception as e:
            print(f"Error al contar libros: {e}")
            return 0
        finally:
            session.close()
