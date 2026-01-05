# main.py
# Aplicación principal del sistema de biblioteca usando patrón MVC

from controllers import LibroController, UsuarioController, PrestamoController
from views import ConsoleView

class BibliotecaApp:
    """Aplicación principal del sistema de biblioteca"""

    def __init__(self):
        # Inicializar controladores
        self.libro_controller = LibroController()
        self.usuario_controller = UsuarioController()
        self.prestamo_controller = PrestamoController()

        # Inicializar vista
        self.view = ConsoleView()

    def ejecutar(self):
        """Ejecuta la aplicación principal"""
        print("=" * 80)
        print("BIENVENIDO AL SISTEMA DE GESTIÓN DE BIBLIOTECA")
        print("=" * 80)

        while True:
            opcion = self.view.mostrar_menu_principal()

            if opcion == '1':
                self.menu_libros()
            elif opcion == '2':
                self.menu_usuarios()
            elif opcion == '3':
                self.menu_prestamos()
            elif opcion == '4':
                self.menu_reportes()
            elif opcion == '5':
                print("\n¡Hasta luego!")
                break
            else:
                self.view.mostrar_mensaje_error("Opción inválida")
                self.view.pausar()

    def menu_libros(self):
        """Menú de gestión de libros"""
        while True:
            opcion = self.view.mostrar_menu_libros()

            if opcion == '1':
                # Listar todos los libros
                libros = self.libro_controller.obtener_todos()
                self.view.mostrar_lista_libros(libros)
                self.view.pausar()

            elif opcion == '2':
                # Buscar libro
                termino = self.view.solicitar_texto("Ingrese término de búsqueda")
                libros = self.libro_controller.buscar(termino)
                self.view.mostrar_lista_libros(libros)
                self.view.pausar()

            elif opcion == '3':
                # Agregar nuevo libro
                try:
                    datos = self.view.solicitar_datos_libro()
                    exito, mensaje, libro_id = self.libro_controller.crear(datos)

                    if exito:
                        self.view.mostrar_mensaje_exito(mensaje)
                    else:
                        self.view.mostrar_mensaje_error(mensaje)
                except ValueError as e:
                    self.view.mostrar_mensaje_error(f"Error en los datos: {e}")
                except Exception as e:
                    self.view.mostrar_mensaje_error(f"Error inesperado: {e}")

                self.view.pausar()

            elif opcion == '4':
                # Actualizar libro
                libro_id = self.view.solicitar_id("ID del libro a actualizar")
                if libro_id:
                    libro = self.libro_controller.obtener_por_id(libro_id)

                    if libro:
                        self.view.mostrar_detalle_libro(libro)
                        if self.view.confirmar_accion("¿Desea actualizar este libro?"):
                            try:
                                datos = self.view.solicitar_datos_libro()
                                # Convertir claves a formato del modelo
                                datos_modelo = {
                                    'Titulo': datos['titulo'],
                                    'ISBN': datos['isbn'],
                                    'AutorID': datos['autor_id'],
                                    'CategoriaID': datos['categoria_id'],
                                    'Editorial': datos['editorial'],
                                    'NumeroPaginas': datos['numero_paginas'],
                                    'CopiasTotal': datos['copias'],
                                    'Descripcion': datos['descripcion']
                                }
                                exito, mensaje = self.libro_controller.actualizar(libro_id, datos_modelo)

                                if exito:
                                    self.view.mostrar_mensaje_exito(mensaje)
                                else:
                                    self.view.mostrar_mensaje_error(mensaje)
                            except Exception as e:
                                self.view.mostrar_mensaje_error(f"Error: {e}")
                    else:
                        self.view.mostrar_mensaje_error("Libro no encontrado")

                self.view.pausar()

            elif opcion == '5':
                # Eliminar libro
                libro_id = self.view.solicitar_id("ID del libro a eliminar")
                if libro_id:
                    libro = self.libro_controller.obtener_por_id(libro_id)

                    if libro:
                        self.view.mostrar_detalle_libro(libro)

                        if self.view.confirmar_accion("¿Está seguro de eliminar este libro?"):
                            exito, mensaje = self.libro_controller.eliminar(libro_id)

                            if exito:
                                self.view.mostrar_mensaje_exito(mensaje)
                            else:
                                self.view.mostrar_mensaje_error(mensaje)
                    else:
                        self.view.mostrar_mensaje_error("Libro no encontrado")

                self.view.pausar()

            elif opcion == '6':
                # Ver libros disponibles
                libros = self.libro_controller.obtener_disponibles()
                print("\n[LIBROS DISPONIBLES]")
                self.view.mostrar_lista_libros(libros)
                self.view.pausar()

            elif opcion == '7':
                break
            else:
                self.view.mostrar_mensaje_error("Opción inválida")
                self.view.pausar()

    def menu_usuarios(self):
        """Menú de gestión de usuarios"""
        while True:
            opcion = self.view.mostrar_menu_usuarios()

            if opcion == '1':
                # Listar todos los usuarios
                usuarios = self.usuario_controller.obtener_todos()
                self.view.mostrar_lista_usuarios(usuarios)
                self.view.pausar()

            elif opcion == '2':
                # Buscar usuario por carnet
                carnet = self.view.solicitar_texto("Ingrese número de carnet")
                usuario = self.usuario_controller.obtener_por_carnet(carnet)

                if usuario:
                    self.view.mostrar_detalle_usuario(usuario)
                else:
                    self.view.mostrar_mensaje_error("Usuario no encontrado")

                self.view.pausar()

            elif opcion == '3':
                # Agregar nuevo usuario
                try:
                    datos = self.view.solicitar_datos_usuario()
                    exito, mensaje, usuario_id = self.usuario_controller.crear(datos)

                    if exito:
                        self.view.mostrar_mensaje_exito(mensaje)
                    else:
                        self.view.mostrar_mensaje_error(mensaje)
                except Exception as e:
                    self.view.mostrar_mensaje_error(f"Error: {e}")

                self.view.pausar()

            elif opcion == '4':
                # Actualizar usuario
                usuario_id = self.view.solicitar_id("ID del usuario a actualizar")
                if usuario_id:
                    usuario = self.usuario_controller.obtener_por_id(usuario_id)

                    if usuario:
                        self.view.mostrar_detalle_usuario(usuario)
                        if self.view.confirmar_accion("¿Desea actualizar este usuario?"):
                            try:
                                datos = self.view.solicitar_datos_usuario()
                                # Convertir claves a formato del modelo
                                datos_modelo = {
                                    'NumeroCarnet': datos['numero_carnet'],
                                    'Nombre': datos['nombre'],
                                    'Apellido': datos['apellido'],
                                    'Email': datos['email'],
                                    'Telefono': datos['telefono'],
                                    'Direccion': datos['direccion']
                                }
                                exito, mensaje = self.usuario_controller.actualizar(usuario_id, datos_modelo)

                                if exito:
                                    self.view.mostrar_mensaje_exito(mensaje)
                                else:
                                    self.view.mostrar_mensaje_error(mensaje)
                            except Exception as e:
                                self.view.mostrar_mensaje_error(f"Error: {e}")
                    else:
                        self.view.mostrar_mensaje_error("Usuario no encontrado")

                self.view.pausar()

            elif opcion == '5':
                # Activar/Desactivar usuario
                usuario_id = self.view.solicitar_id("ID del usuario")
                if usuario_id:
                    usuario = self.usuario_controller.obtener_por_id(usuario_id)

                    if usuario:
                        self.view.mostrar_detalle_usuario(usuario)
                        accion = "desactivar" if usuario.Estado == 'Activo' else "activar"

                        if self.view.confirmar_accion(f"¿Desea {accion} este usuario?"):
                            if usuario.Estado == 'Activo':
                                exito, mensaje = self.usuario_controller.desactivar(usuario_id)
                            else:
                                exito, mensaje = self.usuario_controller.activar(usuario_id)

                            if exito:
                                self.view.mostrar_mensaje_exito(mensaje)
                            else:
                                self.view.mostrar_mensaje_error(mensaje)
                    else:
                        self.view.mostrar_mensaje_error("Usuario no encontrado")

                self.view.pausar()

            elif opcion == '6':
                # Ver préstamos de un usuario
                usuario_id = self.view.solicitar_id("ID del usuario")
                if usuario_id:
                    usuario = self.usuario_controller.obtener_por_id(usuario_id)

                    if usuario:
                        prestamos = self.usuario_controller.obtener_prestamos_activos(usuario_id)
                        print(f"\nPréstamos activos de {usuario.nombre_completo}:")
                        self.view.mostrar_lista_prestamos(prestamos)
                    else:
                        self.view.mostrar_mensaje_error("Usuario no encontrado")

                self.view.pausar()

            elif opcion == '7':
                break
            else:
                self.view.mostrar_mensaje_error("Opción inválida")
                self.view.pausar()

    def menu_prestamos(self):
        """Menú de gestión de préstamos"""
        while True:
            opcion = self.view.mostrar_menu_prestamos()

            if opcion == '1':
                # Crear nuevo préstamo
                try:
                    libro_id = self.view.solicitar_id("ID del libro")
                    usuario_id = self.view.solicitar_id("ID del usuario")

                    if libro_id and usuario_id:
                        dias = self.view.solicitar_texto("Días de préstamo (Enter para 14 días)")
                        dias = int(dias) if dias else 14

                        exito, mensaje, prestamo_id = self.prestamo_controller.crear_prestamo(
                            libro_id, usuario_id, dias
                        )

                        if exito:
                            self.view.mostrar_mensaje_exito(mensaje)
                        else:
                            self.view.mostrar_mensaje_error(mensaje)
                except ValueError:
                    self.view.mostrar_mensaje_error("Datos inválidos")
                except Exception as e:
                    self.view.mostrar_mensaje_error(f"Error: {e}")

                self.view.pausar()

            elif opcion == '2':
                # Devolver libro
                prestamo_id = self.view.solicitar_id("ID del préstamo")
                if prestamo_id:
                    if self.view.confirmar_accion("¿Confirma la devolución del libro?"):
                        exito, mensaje, multa = self.prestamo_controller.devolver_libro(prestamo_id)

                        if exito:
                            self.view.mostrar_mensaje_exito(mensaje)
                            if multa > 0:
                                self.view.mostrar_mensaje_info(f"Multa a pagar: ${multa:.2f}")
                        else:
                            self.view.mostrar_mensaje_error(mensaje)

                self.view.pausar()

            elif opcion == '3':
                # Listar préstamos activos
                prestamos = self.prestamo_controller.obtener_prestamos_activos()
                print("\n[PRÉSTAMOS ACTIVOS]")
                self.view.mostrar_lista_prestamos(prestamos)
                self.view.pausar()

            elif opcion == '4':
                # Listar préstamos vencidos
                prestamos = self.prestamo_controller.obtener_prestamos_vencidos()
                print("\n[PRÉSTAMOS VENCIDOS]")
                self.view.mostrar_lista_prestamos(prestamos)
                self.view.pausar()

            elif opcion == '5':
                break
            else:
                self.view.mostrar_mensaje_error("Opción inválida")
                self.view.pausar()

    def menu_reportes(self):
        """Menú de reportes y estadísticas"""
        print("\n" + "=" * 60)
        print("REPORTES Y ESTADÍSTICAS")
        print("=" * 60)

        # Obtener estadísticas usando los controllers
        libros = self.libro_controller.obtener_todos()
        usuarios = self.usuario_controller.obtener_todos()
        prestamos = self.prestamo_controller.obtener_prestamos_activos()
        prestamos_vencidos = self.prestamo_controller.obtener_prestamos_vencidos()

        print(f"\n[RESUMEN GENERAL]")
        print(f"  Total de libros: {len(libros)}")
        print(f"  Libros disponibles: {len(self.libro_controller.obtener_disponibles())}")
        print(f"  Total de usuarios activos: {len(usuarios)}")
        print(f"  Préstamos activos: {len(prestamos)}")
        print(f"  Préstamos vencidos: {len(prestamos_vencidos)}")

        # Libros con más préstamos (simplificado)
        print(f"\n[LIBROS MÁS PRESTADOS]")
        libros_con_prestamos = {}
        for libro in libros:
            if libro.prestamos:
                libros_con_prestamos[libro.Titulo] = len(libro.prestamos)

        for titulo, total in sorted(libros_con_prestamos.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {titulo}: {total} préstamo(s)")

        self.view.pausar()


if __name__ == "__main__":
    try:
        app = BibliotecaApp()
        app.ejecutar()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario. ¡Hasta luego!")
    except Exception as e:
        print(f"\n[ERROR FATAL] {e}")
        print("El programa se cerrará.")
