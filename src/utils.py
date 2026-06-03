"""
utils.py - Funciones de la Sesión 1.

Contiene las funciones desarrolladas durante la Sesión 1 del curso
Python Intermedio para Análisis de Datos - DIAN 2026.

Instrucciones:
  - Completa cada función reemplazando el bloque # TODO
  - No borres el docstring: describe qué debe hacer la función
  - Sigue PEP 8: snake_case, 4 espacios, nombres descriptivos
  - Llama cada función desde main.py para verificar la salida

Autora/Autor: [Tu nombre]
Fecha: [Fecha de la sesión]
"""


# ---------------------------------------------------------------------------
# Datos de práctica.
# Se introduce formalmente en la sección Diccionarios.
# Los ejercicios de Funciones, Encadenamiento, Condicionales y Ciclos
# trabajan con valores escalares y listas simples.
# ---------------------------------------------------------------------------

DECLARACIONES = [
    {"nit": "900123456", "nombre": "Empresa ABC S.A.S.",      "municipio": "Bogota",       "periodo": "202401", "valor": 1_500_000, "estado": "ACTIVO"},
    {"nit": "800234567", "nombre": "Comercial XYZ Ltda.",     "municipio": "Medellin",     "periodo": "202401", "valor": 850_000,   "estado": "ACTIVO"},
    {"nit": "700345678", "nombre": "Servicios LMN S.A.S.",    "municipio": "Cali",         "periodo": "202401", "valor": 0,         "estado": "INACTIVO"},
    {"nit": "600456789", "nombre": "Industrias PQR S.A.",     "municipio": "Barranquilla", "periodo": "202401", "valor": 2_300_000, "estado": "ACTIVO"},
    {"nit": "500567890", "nombre": "Distribuidora STU Ltda.", "municipio": "Bogota",       "periodo": "202402", "valor": 950_000,   "estado": "PENDIENTE"},
    {"nit": "400678901", "nombre": "Inversiones VWX S.A.S.",  "municipio": "Medellin",     "periodo": "202402", "valor": 3_200_000, "estado": "ACTIVO"},
    {"nit": "300789012", "nombre": "Transportes YZA Ltda.",   "municipio": "Cali",         "periodo": "202402", "valor": 450_000,   "estado": "SUSPENDIDO"},
    {"nit": "200890123", "nombre": "Construcciones BCD S.A.", "municipio": "Barranquilla", "periodo": "202402", "valor": 1_100_000, "estado": "ACTIVO"},
]


# ---------------------------------------------------------------------------
# FUNCIONES Y PROCEDIMIENTOS
# Trabajan con tipos simples: str, int, float, bool
# ---------------------------------------------------------------------------

def calcular_iva(valor_base, tasa=0.19):
    """
    Calcula el IVA sobre un valor base.

    Args:
        valor_base (float): Monto antes de impuestos.
        tasa (float): Tasa de IVA. Por defecto 0.19 (19%).

    Returns:
        float: Valor del IVA.

    Ejemplos:
        calcular_iva(1_000_000)        -> 190000.0
        calcular_iva(1_000_000, 0.05)  -> 50000.0
    """
    # TODO: multiplica valor_base por tasa y retorna el resultado
    pass


def formatear_reporte_valor(nit, nombre, valor, estado):
    """
    Genera una línea de reporte con los campos principales de una declaración.

    Args:
        nit (str): NIT del contribuyente.
        nombre (str): Nombre o razón social.
        valor (float): Valor declarado.
        estado (str): Estado del registro.

    Returns:
        str: Cadena con formato "NIT XXXXXXXXX | Nombre | $valor | ESTADO".

    Ejemplo:
        formatear_reporte_valor("900123456", "Empresa ABC S.A.S.", 1_500_000, "ACTIVO")
        -> "NIT 900123456 | Empresa ABC S.A.S. | $1,500,000 | ACTIVO"
    """
    # TODO: construye y retorna la cadena usando un f-string
    # Usa :, para el separador de miles en el valor
    pass


def mostrar_resultado(etiqueta, valor):
    """
    Procedimiento: imprime un resultado con formato de moneda.

    Args:
        etiqueta (str): Descripción del resultado.
        valor (float): Valor numérico a mostrar.
    """
    # TODO: imprime "  etiqueta: $valor" con separadores de miles
    pass


def generar_ficha_contribuyente(nit, nombre, municipio, periodo, valor, estado):
    """
    Genera una ficha formal de contribuyente como texto multilínea.

    Recibe seis parámetros escalares. El nombre y municipio se muestran
    en mayúsculas usando .upper() directamente.

    Args:
        nit (str): NIT del contribuyente.
        nombre (str): Nombre o razón social.
        municipio (str): Municipio de registro.
        periodo (str): Período en formato YYYYMM.
        valor (float): Valor declarado.
        estado (str): Estado del registro.

    Returns:
        str: Texto con la ficha en recuadro.

    Ejemplo de salida:
        ╔══════════════════════════════════════╗
        ║  FICHA DE CONTRIBUYENTE              ║
        ╠══════════════════════════════════════╣
          NIT        : 900123456
          Nombre     : EMPRESA ABC S.A.S.
          Municipio  : BOGOTA
          Periodo    : 202401
          Valor      : $1,500,000
          Estado     : ACTIVO
        ╚══════════════════════════════════════╝
    """
    # TODO: construye la cadena multilínea usando f-strings
    # Usa nombre.upper() y municipio.upper() para normalizar
    pass


# ---------------------------------------------------------------------------
# ENCADENAMIENTO DE FUNCIONES
# Trabajan con str y bool; no usan dicts
# ---------------------------------------------------------------------------

def limpiar_nit(nit):
    """
    Elimina guiones y puntos de un NIT.

    Args:
        nit (str): NIT posiblemente con guiones o puntos.

    Returns:
        str: NIT solo con dígitos.

    Ejemplo:
        limpiar_nit("900-123-456")  -> "900123456"
        limpiar_nit("900.123.456")  -> "900123456"
    """
    # TODO: usa .replace("-", "") y .replace(".", "")
    pass


def validar_nit(nit):
    """
    Valida que un NIT tenga el formato correcto.

    Llama a limpiar_nit() internamente antes de validar.
    Un NIT válido: solo dígitos, entre 9 y 10 caracteres.

    Args:
        nit (str): NIT a validar.

    Returns:
        bool: True si es válido, False si no.

    Ejemplo:
        validar_nit("900123456")    -> True
        validar_nit("900-123-456")  -> True  (se limpia antes)
        validar_nit("ABC123")       -> False
    """
    # TODO: llama limpiar_nit(), verifica .isdigit() y len() entre 9 y 10
    pass


def normalizar_texto(texto):
    """
    Limpia y normaliza una cadena de texto con encadenamiento de métodos.

    Aplica en cadena: .strip() → .upper() → .replace("  ", " ")

    Args:
        texto (str): Texto a normalizar.

    Returns:
        str: Texto normalizado.

    Ejemplo:
        normalizar_texto("  bogotá d.c.  ")   -> "BOGOTÁ D.C."
        normalizar_texto("  empresa  abc  ")  -> "EMPRESA ABC"
    """
    # TODO: encadena los tres métodos en una sola expresión y retorna
    pass


def procesar_nit(nit):
    """
    Limpia un NIT y retorna un mensaje con el resultado de la validación.

    Llama a limpiar_nit() y luego a validar_nit() internamente.

    Args:
        nit (str): NIT a procesar.

    Returns:
        str: Mensaje con el NIT limpio y si es válido o no.

    Ejemplo:
        procesar_nit("900-123-456")  -> "NIT 900123456: válido"
        procesar_nit("ABC-123")      -> "NIT ABC123: INVÁLIDO"
    """
    # TODO: llama limpiar_nit(), luego validar_nit(), construye el mensaje
    pass


def pipeline_nit(nit):
    """
    Encadena limpiar, validar y formatear un NIT en un informe de texto.

    Args:
        nit (str): NIT original, puede tener guiones.

    Returns:
        str: Informe del procesamiento.

    Ejemplo:
        pipeline_nit("900-123-456")  -> "NIT 900123456 — apto para procesamiento"
        pipeline_nit("ABC-123")      -> "NIT ABC-123 — rechazado: formato inválido"
    """
    # TODO: llama limpiar_nit(), luego valida, luego retorna el mensaje según resultado
    pass


# ---------------------------------------------------------------------------
# CONDICIONALES
# Trabajan con tipos simples: str, int, float, bool
# ---------------------------------------------------------------------------

def esta_al_dia(dias_mora):
    """
    Determina si un contribuyente está al día.

    Args:
        dias_mora (int): Días de atraso. 0 = sin mora.

    Returns:
        bool: True si dias_mora == 0.
    """
    # TODO: if/else simple
    pass


def aplicar_descuento(valor, pago_voluntario):
    """
    Aplica un descuento del 10% si el pago es voluntario.

    Args:
        valor (float): Valor original.
        pago_voluntario (bool): True si el pago es voluntario.

    Returns:
        float: Valor con descuento o valor original.
    """
    # TODO: if/else según pago_voluntario
    pass


def asignar_prioridad(valor, tiene_historial_incumplimiento):
    """
    Asigna prioridad de atención (condicional simple con operadores lógicos).

    Reglas:
    - valor > 1.000.000 AND tiene historial -> "ALTA"
    - solo una condición cumplida           -> "MEDIA"
    - ninguna                               -> "BAJA"

    Returns:
        str: 'ALTA', 'MEDIA' o 'BAJA'.
    """
    # TODO: usa and/or en los condicionales
    pass


def evaluar_pago(estado, valor):
    """
    Evalúa si un registro está en orden (condicional anidado).

    Returns:
        str: 'En regla', 'Activo con valor insuficiente',
             'Registro inactivo' o 'Requiere revisión manual'.
    """
    # TODO: if anidado: primero estado, luego valor dentro de ACTIVO
    pass


def clasificar_contribuyente(valor):
    """
    Clasifica al contribuyente en cinco categorías (condicionales encadenados).

    Categorías:
        GRANDE   : más de 5.000.000
        MEDIANO  : entre 1.000.001 y 5.000.000
        PEQUEÑO  : entre 100.001 y 1.000.000
        MÍNIMO   : entre 1 y 100.000
        SIN VALOR: 0

    Returns:
        str: Categoría del contribuyente.
    """
    # TODO: if/elif/elif/elif/else
    pass


def calcular_sancion_basica(dias_mora, valor_base):
    """
    Calcula la sanción según días de mora (condicionales encadenados).

    Tasas: 0d=0%, 1-30d=1%, 31-60d=3%, 61-90d=5%, >90d=10%

    Returns:
        float: Valor de la sanción.
    """
    # TODO: elif para cada rango, luego calcula tasa * valor_base
    pass


# ---------------------------------------------------------------------------
# CICLOS WITH LISTAS SIMPLES (str, float)
# No usan DECLARACIONES todavía
# ---------------------------------------------------------------------------

def imprimir_nits_validos(nits):
    """
    Imprime los NITs válidos de una lista, numerados desde 1.

    Args:
        nits (list): Lista de NITs como cadenas de texto.
    """
    # TODO: for loop, llama validar_nit(), imprime solo los válidos con enumerate
    pass


def calcular_totales(valores):
    """
    Calcula total, promedio y máximo de una lista de floats.

    No usa sum(), max() ni funciones de statistics.

    Args:
        valores (list): Lista de floats.

    Returns:
        tuple: (total, promedio, maximo)
    """
    # TODO: for loop con acumuladores; divide al final para el promedio
    pass


def generar_periodos_multiple(anio_inicio, anio_fin, meses_por_anio=12):
    """
    Genera códigos de período para varios años consecutivos.

    Args:
        anio_inicio (int): Primer año.
        anio_fin (int): Último año (inclusive).
        meses_por_anio (int): Meses a generar por año. Por defecto 12.

    Returns:
        list: Lista de códigos en formato YYYYMM.

    Ejemplo:
        generar_periodos_multiple(2024, 2025, 3)
        -> ['202401', '202402', '202403', '202501', '202502', '202503']
    """
    # TODO: for externo para años, for interno con range para meses
    pass


def buscar_primer_valido(nits):
    """
    Busca el primer NIT válido en una lista (ciclo while).

    Args:
        nits (list): Lista de NITs como cadenas.

    Returns:
        str | None: El primer NIT válido, o None si no hay ninguno.
    """
    # TODO: while con indice; retorna al encontrar uno válido
    pass


def sumar_hasta_limite(valores, limite):
    """
    Acumula valores mientras el total no supere el límite (ciclo while).

    Args:
        valores (list): Lista de floats.
        limite (float): Límite de acumulación.

    Returns:
        tuple: (cantidad_procesada, total_acumulado)
    """
    # TODO: while que acumula; detiene cuando total + siguiente > limite
    pass


def encontrar_primer_sobre_umbral(valores, umbral):
    """
    Retorna el primer valor que supere el umbral (ciclo while).

    Args:
        valores (list): Lista de floats.
        umbral (float): Umbral de comparación.

    Returns:
        float | None: Primer valor sobre el umbral, o None.
    """
    # TODO: while con indice; retorna al encontrar uno > umbral
    pass


def validar_secuencia_periodos(periodos):
    """
    Verifica que una lista de períodos esté en orden consecutivo (ciclo while).

    Args:
        periodos (list): Lista de cadenas en formato YYYYMM.

    Returns:
        tuple: (es_valida: bool, indice_salto: int | None)
    """
    # TODO: while que compara cada elemento con el siguiente
    # Convierte YYYYMM a número entero para comparar
    pass


# ---------------------------------------------------------------------------
# LISTAS (operaciones con listas de str y float)
# No usan DECLARACIONES todavía
# ---------------------------------------------------------------------------

def agregar_unico(lista, elemento):
    """
    Agrega un elemento a la lista solo si no está ya.

    Args:
        lista (list): Lista a modificar.
        elemento: Elemento a agregar.

    Returns:
        list: Lista actualizada.
    """
    # TODO: if elemento not in lista: lista.append(elemento)
    pass


def filtrar_valores_en_rango(valores, minimo, maximo):
    """
    Retorna los valores entre mínimo y máximo inclusive.

    No modifica la lista original.

    Args:
        valores (list): Lista de floats.
        minimo (float): Límite inferior (inclusive).
        maximo (float): Límite superior (inclusive).

    Returns:
        list: Valores dentro del rango.
    """
    # TODO: for loop que agrega a una nueva lista cuando minimo <= v <= maximo
    pass


def ordenar_valores(valores, descendente=True):
    """
    Retorna una nueva lista ordenada usando burbuja.

    No usa .sort() ni sorted().

    Args:
        valores (list): Lista de floats.
        descendente (bool): True = mayor a menor.

    Returns:
        list: Lista ordenada.
    """
    # TODO: copia la lista primero, luego aplica burbuja
    pass


# ---------------------------------------------------------------------------
# DICCIONARIOS
# Aquí llega DECLARACIONES. A partir de este punto los ejercicios la usan.
# ---------------------------------------------------------------------------

def indexar_por_nit(declaraciones):
    """
    Construye un índice de declaraciones por NIT.

    Args:
        declaraciones (list): Lista de declaraciones (DECLARACIONES).

    Returns:
        dict: Claves = NITs, valores = diccionarios de declaración.

    Ejemplo:
        indice = indexar_por_nit(DECLARACIONES)
        indice["600456789"]["nombre"]  -> "Industrias PQR S.A."
    """
    # TODO: for loop que agrega cada declaracion usando d["nit"] como clave
    pass


def construir_resumen_por_estado(declaraciones):
    """
    Agrupa conteo y total de valor por estado.

    Args:
        declaraciones (list): Lista de declaraciones.

    Returns:
        dict: {'ACTIVO': {'conteo': 5, 'total_valor': 9150000}, ...}
    """
    # TODO: for loop; si el estado no está en el dict, inícialo primero
    pass


def agrupar_por_municipio(declaraciones):
    """
    Agrupa las declaraciones por municipio.

    Args:
        declaraciones (list): Lista de declaraciones.

    Returns:
        dict: Claves = municipios, valores = listas de declaraciones.
    """
    # TODO: for loop; si el municipio no está, crea la lista vacía primero
    pass


def listar_activos(declaraciones):
    """
    Imprime los registros ACTIVOS numerados (usa DECLARACIONES).

    Args:
        declaraciones (list): Lista de declaraciones.
    """
    # TODO: for loop con enumerate, imprime solo los ACTIVO
    pass


def calcular_estadisticas(declaraciones):
    """
    Calcula estadísticas sobre el conjunto de declaraciones.

    Args:
        declaraciones (list): Lista de declaraciones.

    Returns:
        dict: total_registros, total_activos, suma_valores,
              promedio_valor (activos), valor_maximo.
    """
    # TODO: un solo for loop que acumule todos los valores necesarios
    pass


def filtrar_por_estado(declaraciones, estado):
    """
    Retorna solo los registros con el estado indicado.

    Args:
        declaraciones (list): Lista de declaraciones.
        estado (str): Estado a filtrar.

    Returns:
        list: Declaraciones con ese estado.
    """
    # TODO: for loop que agrega a nueva lista cuando coincide el estado
    pass


def buscar_por_nit(declaraciones, nit_buscado):
    """
    Busca la primera declaración con el NIT indicado (ciclo while).

    Args:
        declaraciones (list): Lista de declaraciones.
        nit_buscado (str): NIT a buscar.

    Returns:
        dict | None: Primera declaración encontrada, o None.
    """
    # TODO: while con indice; accede a d["nit"] para comparar
    pass
