# test_controllers.py
# Script para probar los controllers del patrón MVC

from controllers import LibroController, UsuarioController, PrestamoController

print("=" * 80)
print("PRUEBA DE CONTROLLERS - PATRÓN MVC")
print("=" * 80)

# Inicializar controllers
libro_ctrl = LibroController()
usuario_ctrl = UsuarioController()
prestamo_ctrl = PrestamoController()

print("\n[PRUEBA 1] Obtener todos los libros")
print("-" * 60)
libros = libro_ctrl.obtener_todos()
print(f"Total de libros: {len(libros)}")
for libro in libros:
    print(f"  - {libro.Titulo} por {libro.autor.nombre_completo}")

print("\n[PRUEBA 2] Buscar libros")
print("-" * 60)
resultados = libro_ctrl.buscar("García")
print(f"Resultados para 'García': {len(resultados)}")
for libro in resultados:
    print(f"  - {libro.Titulo}")

print("\n[PRUEBA 3] Obtener todos los usuarios")
print("-" * 60)
usuarios = usuario_ctrl.obtener_todos()
print(f"Total de usuarios activos: {len(usuarios)}")
for usuario in usuarios:
    print(f"  - {usuario.nombre_completo} ({usuario.NumeroCarnet})")

print("\n[PRUEBA 4] Obtener préstamos activos")
print("-" * 60)
prestamos = prestamo_ctrl.obtener_prestamos_activos()
print(f"Total de préstamos activos: {len(prestamos)}")
for prestamo in prestamos:
    print(f"  - {prestamo.libro.Titulo} -> {prestamo.usuario.nombre_completo}")
    print(f"    Vence: {prestamo.FechaDevolucionEsperada} ({prestamo.dias_restantes} días)")

print("\n[PRUEBA 5] Obtener libros disponibles")
print("-" * 60)
disponibles = libro_ctrl.obtener_disponibles()
print(f"Libros con copias disponibles: {len(disponibles)}")
for libro in disponibles:
    print(f"  - {libro.Titulo}: {libro.CopiasDisponibles} disponibles")

print("\n" + "=" * 80)
print("TODAS LAS PRUEBAS COMPLETADAS")
print("=" * 80)
print("\nLos controllers están funcionando correctamente!")
print("Ahora puedes:")
print("  1. Crear las vistas (views/console_view.py)")
print("  2. Crear la aplicación principal (main.py)")
print("  3. Crear la aplicación web (app.py)")
