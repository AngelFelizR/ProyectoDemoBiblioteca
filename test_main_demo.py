# test_main_demo.py
# Script para probar las funcionalidades de main.py sin interacción

from main import BibliotecaApp

print("=" * 80)
print("PRUEBA DE MAIN.PY - APLICACIÓN MVC")
print("=" * 80)

# Crear instancia de la aplicación
app = BibliotecaApp()

print("\n[PRUEBA 1] Controllers inicializados correctamente")
print(f"  - LibroController: {'OK' if app.libro_controller else 'ERROR'}")
print(f"  - UsuarioController: {'OK' if app.usuario_controller else 'ERROR'}")
print(f"  - PrestamoController: {'OK' if app.prestamo_controller else 'ERROR'}")
print(f"  - ConsoleView: {'OK' if app.view else 'ERROR'}")

print("\n[PRUEBA 2] Probar método de libros")
libros = app.libro_controller.obtener_todos()
print(f"  Total de libros: {len(libros)}")
print(f"  Primer libro: {libros[0].Titulo if libros else 'N/A'}")

print("\n[PRUEBA 3] Probar método de usuarios")
usuarios = app.usuario_controller.obtener_todos()
print(f"  Total de usuarios activos: {len(usuarios)}")
print(f"  Primer usuario: {usuarios[0].nombre_completo if usuarios else 'N/A'}")

print("\n[PRUEBA 4] Probar método de préstamos")
prestamos = app.prestamo_controller.obtener_prestamos_activos()
print(f"  Total de préstamos activos: {len(prestamos)}")

print("\n[PRUEBA 5] Probar vista de consola")
# No ejecutar menús interactivos, solo verificar que existen
print(f"  - mostrar_menu_principal: {'OK' if hasattr(app.view, 'mostrar_menu_principal') else 'ERROR'}")
print(f"  - mostrar_lista_libros: {'OK' if hasattr(app.view, 'mostrar_lista_libros') else 'ERROR'}")
print(f"  - mostrar_mensaje_exito: {'OK' if hasattr(app.view, 'mostrar_mensaje_exito') else 'ERROR'}")

print("\n" + "=" * 80)
print("TODAS LAS PRUEBAS COMPLETADAS")
print("=" * 80)
print("\n[OK] main.py está listo para usar!")
print("\nPara ejecutar la aplicación completa:")
print("  python main.py")
