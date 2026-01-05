# controllers/__init__.py
# Paquete de controladores para el patrón MVC

from .libro_controller import LibroController
from .usuario_controller import UsuarioController
from .prestamo_controller import PrestamoController
from .categoria_controller import CategoriaController
from .autor_controller import AutorController

__all__ = ['LibroController', 'UsuarioController', 'PrestamoController', 'CategoriaController', 'AutorController']
