# views/console_view.py
# Vista de consola para interacción con el usuario

from datetime import datetime

class ConsoleView:
    """Vista de consola para interacción con el usuario"""

    @staticmethod
    def mostrar_menu_principal():
        """Muestra el menú principal"""
        print("\n" + "=" * 80)
        print("SISTEMA DE GESTIÓN DE BIBLIOTECA")
        print("=" * 80)
        print("1. Gestión de Libros")
        print("2. Gestión de Usuarios")
        print("3. Gestión de Préstamos")
        print("4. Reportes y Estadísticas")
        print("5. Salir")
        print("-" * 80)
        return input("Seleccione una opción: ")

    @staticmethod
    def mostrar_menu_libros():
        """Muestra el menú de gestión de libros"""
        print("\n" + "=" * 60)
        print("GESTIÓN DE LIBROS")
        print("=" * 60)
        print("1. Listar todos los libros")
        print("2. Buscar libro")
        print("3. Agregar nuevo libro")
        print("4. Actualizar libro")
        print("5. Eliminar libro")
        print("6. Ver libros disponibles")
        print("7. Volver al menú principal")
        print("-" * 60)
        return input("Seleccione una opción: ")

    @staticmethod
    def mostrar_menu_usuarios():
        """Muestra el menú de gestión de usuarios"""
        print("\n" + "=" * 60)
        print("GESTIÓN DE USUARIOS")
        print("=" * 60)
        print("1. Listar todos los usuarios")
        print("2. Buscar usuario por carnet")
        print("3. Agregar nuevo usuario")
        print("4. Actualizar usuario")
        print("5. Activar/Desactivar usuario")
        print("6. Ver préstamos de un usuario")
        print("7. Volver al menú principal")
        print("-" * 60)
        return input("Seleccione una opción: ")

    @staticmethod
    def mostrar_menu_prestamos():
        """Muestra el menú de gestión de préstamos"""
        print("\n" + "=" * 60)
        print("GESTIÓN DE PRÉSTAMOS")
        print("=" * 60)
        print("1. Crear nuevo préstamo")
        print("2. Devolver libro")
        print("3. Listar préstamos activos")
        print("4. Listar préstamos vencidos")
        print("5. Volver al menú principal")
        print("-" * 60)
        return input("Seleccione una opción: ")

    @staticmethod
    def mostrar_lista_libros(libros):
        """
        Muestra una lista de libros

        Args:
            libros (list): Lista de objetos Libro
        """
        if not libros:
            print("\nNo se encontraron libros.")
            return

        print("\n" + "=" * 110)
        print(f"{'ID':<5} {'Título':<35} {'Autor':<25} {'Categoría':<15} {'Disponibles':<12} {'Total':<8}")
        print("-" * 110)

        for libro in libros:
            print(f"{libro.LibroID:<5} {libro.Titulo[:34]:<35} "
                  f"{libro.autor.nombre_completo[:24]:<25} "
                  f"{libro.categoria.NombreCategoria[:14]:<15} "
                  f"{libro.CopiasDisponibles:<12} {libro.CopiasTotal:<8}")

    @staticmethod
    def mostrar_detalle_libro(libro):
        """
        Muestra los detalles completos de un libro

        Args:
            libro (Libro): Objeto Libro
        """
        print("\n" + "=" * 80)
        print("DETALLES DEL LIBRO")
        print("=" * 80)
        print(f"ID: {libro.LibroID}")
        print(f"Título: {libro.Titulo}")
        print(f"ISBN: {libro.ISBN}")
        print(f"Autor: {libro.autor.nombre_completo}")
        print(f"Categoría: {libro.categoria.NombreCategoria}")
        print(f"Editorial: {libro.Editorial or 'N/A'}")
        print(f"Páginas: {libro.NumeroPaginas or 'N/A'}")
        print(f"Fecha de publicación: {libro.FechaPublicacion or 'N/A'}")
        print(f"Copias disponibles: {libro.CopiasDisponibles}/{libro.CopiasTotal}")
        print(f"Descripción: {libro.Descripcion or 'N/A'}")
        print("-" * 80)

    @staticmethod
    def solicitar_datos_libro():
        """Solicita los datos para crear/actualizar un libro"""
        print("\n" + "=" * 60)
        print("DATOS DEL LIBRO")
        print("=" * 60)

        datos = {}
        datos['titulo'] = input("Título: ")
        datos['isbn'] = input("ISBN: ")
        datos['autor_id'] = int(input("ID del Autor: "))
        datos['categoria_id'] = int(input("ID de la Categoría: "))
        datos['editorial'] = input("Editorial (opcional): ") or None

        paginas = input("Número de páginas (opcional): ")
        datos['numero_paginas'] = int(paginas) if paginas else None

        copias = input("Número de copias: ")
        datos['copias'] = int(copias) if copias else 0

        datos['descripcion'] = input("Descripción (opcional): ") or None

        return datos

    @staticmethod
    def mostrar_lista_usuarios(usuarios):
        """Muestra una lista de usuarios"""
        if not usuarios:
            print("\nNo se encontraron usuarios.")
            return

        print("\n" + "=" * 100)
        print(f"{'ID':<5} {'Carnet':<12} {'Nombre':<30} {'Email':<30} {'Estado':<10}")
        print("-" * 100)

        for usuario in usuarios:
            print(f"{usuario.UsuarioID:<5} {usuario.NumeroCarnet:<12} "
                  f"{usuario.nombre_completo[:29]:<30} "
                  f"{usuario.Email[:29]:<30} {usuario.Estado:<10}")

    @staticmethod
    def mostrar_detalle_usuario(usuario):
        """Muestra los detalles de un usuario"""
        print("\n" + "=" * 80)
        print("DETALLES DEL USUARIO")
        print("=" * 80)
        print(f"ID: {usuario.UsuarioID}")
        print(f"Carnet: {usuario.NumeroCarnet}")
        print(f"Nombre: {usuario.nombre_completo}")
        print(f"Email: {usuario.Email}")
        print(f"Teléfono: {usuario.Telefono or 'N/A'}")
        print(f"Dirección: {usuario.Direccion or 'N/A'}")
        print(f"Estado: {usuario.Estado}")
        print(f"Fecha de registro: {usuario.FechaRegistro}")
        print("-" * 80)

    @staticmethod
    def solicitar_datos_usuario():
        """Solicita los datos para crear/actualizar un usuario"""
        print("\n" + "=" * 60)
        print("DATOS DEL USUARIO")
        print("=" * 60)

        datos = {}
        datos['numero_carnet'] = input("Número de carnet: ")
        datos['nombre'] = input("Nombre: ")
        datos['apellido'] = input("Apellido: ")
        datos['email'] = input("Email: ")
        datos['telefono'] = input("Teléfono (opcional): ") or None
        datos['direccion'] = input("Dirección (opcional): ") or None

        return datos

    @staticmethod
    def mostrar_lista_prestamos(prestamos):
        """Muestra una lista de préstamos"""
        if not prestamos:
            print("\nNo se encontraron préstamos.")
            return

        print("\n" + "=" * 120)
        print(f"{'ID':<5} {'Usuario':<25} {'Libro':<35} {'Préstamo':<12} {'Devolución':<12} {'Estado':<10} {'Días':<8}")
        print("-" * 120)

        for prestamo in prestamos:
            fecha_prestamo = prestamo.FechaPrestamo.strftime('%Y-%m-%d')
            fecha_devolucion = prestamo.FechaDevolucionEsperada.strftime('%Y-%m-%d')
            dias = prestamo.dias_restantes if prestamo.esta_activo else 0

            estado_dias = ""
            if prestamo.esta_activo:
                if dias < 0:
                    estado_dias = f"{abs(dias)} atraso"
                else:
                    estado_dias = f"{dias} quedan"

            print(f"{prestamo.PrestamoID:<5} "
                  f"{prestamo.usuario.nombre_completo[:24]:<25} "
                  f"{prestamo.libro.Titulo[:34]:<35} "
                  f"{fecha_prestamo:<12} {fecha_devolucion:<12} "
                  f"{prestamo.Estado:<10} {estado_dias:<8}")

    @staticmethod
    def mostrar_mensaje_exito(mensaje):
        """Muestra un mensaje de éxito"""
        print(f"\n[OK] {mensaje}")

    @staticmethod
    def mostrar_mensaje_error(mensaje):
        """Muestra un mensaje de error"""
        print(f"\n[ERROR] {mensaje}")

    @staticmethod
    def mostrar_mensaje_info(mensaje):
        """Muestra un mensaje informativo"""
        print(f"\n[INFO] {mensaje}")

    @staticmethod
    def confirmar_accion(mensaje):
        """Solicita confirmación para una acción"""
        respuesta = input(f"\n{mensaje} (s/n): ").lower()
        return respuesta == 's'

    @staticmethod
    def pausar():
        """Pausa la ejecución esperando entrada del usuario"""
        input("\nPresione Enter para continuar...")

    @staticmethod
    def limpiar_pantalla():
        """Limpia la pantalla (simulado con líneas en blanco)"""
        print("\n" * 2)

    @staticmethod
    def solicitar_id(mensaje="Ingrese el ID"):
        """Solicita un ID al usuario"""
        try:
            return int(input(f"{mensaje}: "))
        except ValueError:
            print("[ERROR] Debe ingresar un número válido")
            return None

    @staticmethod
    def solicitar_texto(mensaje):
        """Solicita un texto al usuario"""
        return input(f"{mensaje}: ").strip()
