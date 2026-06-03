# main.py
# Sistema de análisis de declaraciones - DIAN 2026
#
# Punto de entrada del proyecto.
# Ejecutar con: python main.py
#
# Instrucciones:
#   - Este archivo ya funciona: ejecuta python main.py y verás el menú.
#   - Cada opción del menú tiene el código comentado con # TODO.
#   - A medida que implementes cada función en src/utils.py,
#     descomenta las líneas correspondientes en ejecutar_opcion().
#   - Agrega las importaciones al bloque de imports al principio de
#     ejecutar_opcion() cuando descomentes una función nueva.

from src.utils import DECLARACIONES


def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n" + "=" * 52)
    print("  Análisis de declaraciones - DIAN 2026")
    print("=" * 52)
    print("  1. Calcular IVA de un valor")
    print("  2. Validar un NIT")
    print("  3. Clasificar un valor declarado")
    print("  4. Ver ficha de un contribuyente")
    print("  5. Filtrar declaraciones por estado")
    print("  6. Buscar declaración por NIT")
    print("  7. Estadísticas del sistema")
    print("  8. Análisis por período")
    print("  0. Salir")
    print("=" * 52)


def ejecutar_opcion(opcion):
    """
    Ejecuta la acción correspondiente a la opción elegida.

    A medida que implementes cada función en src/utils.py,
    descomenta el bloque correspondiente y agrega el import
    al inicio de esta función.
    """

    if opcion == "1":
        # TODO: descomentar cuando implementes calcular_iva_detallado
        # from src.utils import calcular_iva_detallado
        # try:
        #     valor = float(input("  Ingrese el valor base: $").replace(",", ""))
        #     resultado = calcular_iva_detallado(valor)
        #     print(f"  Valor base : ${resultado['valor_base']:,}")
        #     print(f"  IVA (19%)  : ${resultado['iva']:,.0f}")
        #     print(f"  Total      : ${resultado['total']:,.0f}")
        # except ValueError:
        #     print("  Error: ingresa un número válido.")
        print("  (función pendiente: calcular_iva_detallado)")

    elif opcion == "2":
        # TODO: descomentar cuando implementes validar_nit
        # from src.utils import validar_nit
        # nit = input("  Ingrese el NIT: ").strip()
        # es_valido = validar_nit(nit)
        # estado = "válido ✓" if es_valido else "INVÁLIDO ✗"
        # print(f"  NIT '{nit}': {estado}")
        print("  (función pendiente: validar_nit)")

    elif opcion == "3":
        # TODO: descomentar cuando implementes clasificar_contribuyente
        # from src.utils import clasificar_contribuyente
        # try:
        #     valor = float(input("  Ingrese el valor: $").replace(",", ""))
        #     categoria = clasificar_contribuyente(valor)
        #     print(f"  ${valor:,.0f} → {categoria}")
        # except ValueError:
        #     print("  Error: ingresa un número válido.")
        print("  (función pendiente: clasificar_contribuyente)")

    elif opcion == "4":
        # TODO: descomentar cuando implementes generar_ficha_contribuyente
        # from src.utils import generar_ficha_contribuyente, indexar_por_nit
        # nit = input("  Ingrese el NIT: ").strip()
        # indice = indexar_por_nit(DECLARACIONES)
        # if nit in indice:
        #     d = indice[nit]
        #     print(generar_ficha_contribuyente(
        #         d["nit"], d["nombre"], d["municipio"],
        #         d["periodo"], d["valor"], d["estado"]
        #     ))
        # else:
        #     print(f"  NIT {nit} no encontrado.")
        print("  (función pendiente: generar_ficha_contribuyente)")

    elif opcion == "5":
        # TODO: descomentar cuando implementes filtrar_por_estado
        # from src.utils import filtrar_por_estado
        # estado = input("  Estado (ACTIVO/INACTIVO/PENDIENTE/SUSPENDIDO): ").strip().upper()
        # resultado = filtrar_por_estado(DECLARACIONES, estado)
        # if resultado:
        #     print(f"\n  Declaraciones con estado {estado}:")
        #     for d in resultado:
        #         print(f"    {d['nit']}: {d['nombre']} (${d['valor']:,})")
        # else:
        #     print(f"  No hay registros con estado {estado}.")
        print("  (función pendiente: filtrar_por_estado)")

    elif opcion == "6":
        # TODO: descomentar cuando implementes buscar_por_nit
        # from src.utils import buscar_por_nit
        # nit = input("  Ingrese el NIT: ").strip()
        # resultado = buscar_por_nit(DECLARACIONES, nit)
        # if resultado:
        #     print(f"  Nombre  : {resultado['nombre']}")
        #     print(f"  Municipio: {resultado['municipio']}")
        #     print(f"  Valor   : ${resultado['valor']:,}")
        #     print(f"  Estado  : {resultado['estado']}")
        # else:
        #     print(f"  NIT {nit} no encontrado.")
        print("  (función pendiente: buscar_por_nit)")

    elif opcion == "7":
        # TODO: descomentar cuando implementes calcular_estadisticas
        # from src.utils import calcular_estadisticas
        # stats = calcular_estadisticas(DECLARACIONES)
        # print("\n  Estadísticas del sistema:")
        # for clave, valor in stats.items():
        #     if isinstance(valor, float) or isinstance(valor, int):
        #         print(f"    {clave}: {valor:,}")
        #     else:
        #         print(f"    {clave}: {valor}")
        print("  (función pendiente: calcular_estadisticas)")

    elif opcion == "8":
        # TODO: implementar submenú de análisis por período
        # Ejercicio avanzado de menús: crea una función ejecutar_menu_periodo()
        # y llámala aquí.
        print("  (submenú pendiente: análisis por período)")

    elif opcion == "0":
        print("\n  Hasta luego.\n")

    else:
        print("  Opción no válida. Intenta de nuevo.")


def main():
    """Función principal: ejecuta el menú hasta que el usuario elija salir."""
    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("  Seleccione una opción: ").strip()
        ejecutar_opcion(opcion)


if __name__ == "__main__":
    main()
