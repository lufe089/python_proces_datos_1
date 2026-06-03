"""
utils.py - Funciones de la Sesión 1.

Contiene las funciones desarrolladas durante la Sesión 1 del curso
Python Intermedio para Análisis de Datos 

Instrucciones:
  - Completa cada función reemplazando el bloque # TODO.
  - No borres el docstring: describe qué debe hacer la función.
  - Sigue PEP 8: snake_case, 4 espacios, nombres descriptivos.
  - Llama cada función desde main.py para verificar la salida.

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
    {
        "nit": "900123456",
        "nombre": "Empresa ABC S.A.S.",
        "municipio": "Bogota",
        "periodo": "202401",
        "valor": 1_500_000,
        "estado": "ACTIVO",
    },
    {
        "nit": "800234567",
        "nombre": "Comercial XYZ Ltda.",
        "municipio": "Medellin",
        "periodo": "202401",
        "valor": 850_000,
        "estado": "ACTIVO",
    },
    {
        "nit": "700345678",
        "nombre": "Servicios LMN S.A.S.",
        "municipio": "Cali",
        "periodo": "202401",
        "valor": 0,
        "estado": "INACTIVO",
    },
    {
        "nit": "600456789",
        "nombre": "Industrias PQR S.A.",
        "municipio": "Barranquilla",
        "periodo": "202401",
        "valor": 2_300_000,
        "estado": "ACTIVO",
    },
    {
        "nit": "500567890",
        "nombre": "Distribuidora STU Ltda.",
        "municipio": "Bogota",
        "periodo": "202402",
        "valor": 950_000,
        "estado": "PENDIENTE",
    },
    {
        "nit": "400678901",
        "nombre": "Inversiones VWX S.A.S.",
        "municipio": "Medellin",
        "periodo": "202402",
        "valor": 3_200_000,
        "estado": "ACTIVO",
    },
    {
        "nit": "300789012",
        "nombre": "Transportes YZA Ltda.",
        "municipio": "Cali",
        "periodo": "202402",
        "valor": 450_000,
        "estado": "SUSPENDIDO",
    },
    {
        "nit": "200890123",
        "nombre": "Construcciones BCD S.A.",
        "municipio": "Barranquilla",
        "periodo": "202402",
        "valor": 1_100_000,
        "estado": "ACTIVO",
    },
]


# ---------------------------------------------------------------------------
# FUNCIONES Y PROCEDIMIENTOS
# Trabajan con tipos simples: str, int, float, bool.
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
    # TODO:
    # 1. Multiplica valor_base por tasa.
    # 2. Retorna el resultado.
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
        formatear_reporte_valor(
            "900123456",
            "Empresa ABC S.A.S.",
            1_500_000,
            "ACTIVO",
        )
        -> "NIT 900123456 | Empresa ABC S.A.S. | $1,500,000 | ACTIVO"
    """
    # TODO:
    # 1. Construye una cadena usando f-string.
    # 2. Incluye nit, nombre, valor y estado en el formato indicado.
    # 3. Usa :, dentro del f-string para mostrar separador de miles.
    # 4. Retorna la cadena.
    pass


def mostrar_resultado(etiqueta, valor):
    """
    Procedimiento: imprime un resultado con formato de moneda.

    Args:
        etiqueta (str): Descripción del resultado.
        valor (float): Valor numérico a mostrar.
    """
    # TODO:
    # 1. Imprime la etiqueta recibida.
    # 2. Imprime el valor con símbolo $ y separadores de miles.
    # 3. Recuerda que este procedimiento no necesita return.
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
    # TODO:
    # 1. Construye una cadena multilínea usando f-string.
    # 2. Usa nombre.upper() para mostrar el nombre en mayúsculas.
    # 3. Usa municipio.upper() para mostrar el municipio en mayúsculas.
    # 4. Formatea valor con separadores de miles.
    # 5. Retorna la ficha completa como str.
    pass


# ---------------------------------------------------------------------------
# ENCADENAMIENTO DE FUNCIONES
# Trabajan con str y bool; no usan diccionarios.
# ---------------------------------------------------------------------------

def limpiar_nit(nit):
    """
    Elimina guiones y puntos de un NIT.

    Args:
        nit (str): NIT posiblemente con guiones o puntos.

    Returns:
        str: NIT sin guiones ni puntos.

    Ejemplo:
        limpiar_nit("900-123-456")  -> "900123456"
        limpiar_nit("900.123.456")  -> "900123456"
    """
    # TODO:
    # 1. Usa .replace("-", "") para quitar guiones.
    # 2. Usa .replace(".", "") para quitar puntos.
    # 3. Retorna el NIT limpio.
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
    # TODO:
    # 1. Guarda en una variable el resultado de limpiar_nit(nit).
    # 2. Verifica que el NIT limpio contenga solo dígitos con .isdigit().
    # 3. Verifica que su longitud esté entre 9 y 10 caracteres.
    # 4. Retorna True solo si ambas condiciones se cumplen.
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
    # TODO:
    # 1. Usa .strip() para quitar espacios al inicio y al final.
    # 2. Usa .upper() para convertir a mayúsculas.
    # 3. Usa .replace("  ", " ") para reemplazar espacios dobles.
    # 4. Encadena los métodos en una sola expresión y retorna.
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
    # TODO:
    # 1. Limpia el NIT usando limpiar_nit(nit).
    # 2. Valida el NIT usando validar_nit(nit).
    # 3. Si es válido, retorna "NIT X: válido".
    # 4. Si no es válido, retorna "NIT X: INVÁLIDO".
    # 5. Usa el NIT limpio en el mensaje.
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
    # TODO:
    # 1. Guarda el NIT original en una variable, para usarlo si es inválido.
    # 2. Limpia el NIT usando limpiar_nit(nit).
    # 3. Valida el NIT usando validar_nit(nit).
    # 4. Si es válido, retorna el mensaje con el NIT limpio.
    # 5. Si no es válido, retorna el mensaje de rechazo con el NIT original.
    pass


# ---------------------------------------------------------------------------
# CONDICIONALES
# Trabajan con tipos simples: str, int, float, bool.
# ---------------------------------------------------------------------------

def esta_al_dia(dias_mora):
    """
    Determina si un contribuyente está al día.

    Args:
        dias_mora (int): Días de atraso. 0 = sin mora.

    Returns:
        bool: True si dias_mora == 0.
    """
    # TODO:
    # 1. Si dias_mora es igual a 0, retorna True.
    # 2. En cualquier otro caso, retorna False.
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
    # TODO:
    # 1. Si pago_voluntario es True, calcula el valor con 10% de descuento.
    # 2. Si pago_voluntario es False, conserva el valor original.
    # 3. Retorna el valor que corresponda.
    pass


def asignar_prioridad(valor, tiene_historial_incumplimiento):
    """
    Asigna prioridad de atención.

    Reglas:
    - valor > 1.000.000 AND tiene historial -> "ALTA"
    - solo una condición cumplida           -> "MEDIA"
    - ninguna                               -> "BAJA"

    Returns:
        str: 'ALTA', 'MEDIA' o 'BAJA'.
    """
    # TODO:
    # 1. Si valor > 1_000_000 y tiene_historial_incumplimiento es True,
    #    retorna "ALTA".
    # 2. Si solo una de las dos condiciones se cumple, retorna "MEDIA".
    # 3. Si ninguna condición se cumple, retorna "BAJA".
    pass


def evaluar_pago(estado, valor):
    """
    Evalúa si un registro está en orden usando un condicional anidado.

    Returns:
        str: 'En regla', 'Activo con valor insuficiente',
             'Registro inactivo' o 'Requiere revisión manual'.
    """
    # TODO:
    # 1. Primero evalúa el estado.
    # 2. Si estado es "ACTIVO", evalúa el valor dentro de ese bloque.
    # 3. Si valor >= 100_000, retorna "En regla".
    # 4. Si valor < 100_000, retorna "Activo con valor insuficiente".
    # 5. Si estado es "INACTIVO", retorna "Registro inactivo".
    # 6. Para cualquier otro estado, retorna "Requiere revisión manual".
    pass


def clasificar_contribuyente(valor):
    """
    Clasifica al contribuyente en cinco categorías.

    Categorías:
        GRANDE   : más de 5.000.000
        MEDIANO  : entre 1.000.001 y 5.000.000
        PEQUEÑO  : entre 100.001 y 1.000.000
        MÍNIMO   : entre 1 y 100.000
        SIN VALOR: 0

    Returns:
        str: Categoría del contribuyente.
    """
    # TODO:
    # 1. Usa if, elif y else para evaluar los rangos de mayor a menor.
    # 2. Si valor > 5_000_000, retorna "GRANDE".
    # 3. Si valor > 1_000_000, retorna "MEDIANO".
    # 4. Si valor > 100_000, retorna "PEQUEÑO".
    # 5. Si valor > 0, retorna "MÍNIMO".
    # 6. En cualquier otro caso, retorna "SIN VALOR".
    pass


def calcular_sancion_basica(dias_mora, valor_base):
    """
    Calcula la sanción según días de mora.

    Tasas: 0d=0%, 1-30d=1%, 31-60d=3%, 61-90d=5%, >90d=10%

    Returns:
        float: Valor de la sanción.
    """
    # TODO:
    # 1. Define una variable tasa.
    # 2. Si dias_mora == 0, la tasa es 0.
    # 3. Si dias_mora está entre 1 y 30, la tasa es 0.01.
    # 4. Si dias_mora está entre 31 y 60, la tasa es 0.03.
    # 5. Si dias_mora está entre 61 y 90, la tasa es 0.05.
    # 6. Si dias_mora es mayor que 90, la tasa es 0.10.
    # 7. Retorna valor_base * tasa.
    pass


# ---------------------------------------------------------------------------
# CICLOS CON LISTAS SIMPLES (str, float)
# No usan DECLARACIONES todavía.
# ---------------------------------------------------------------------------

def imprimir_nits_validos(nits):
    """
    Imprime los NITs válidos de una lista, numerados desde 1.

    Args:
        nits (list): Lista de NITs como cadenas de texto.
    """
    # TODO:
    # 1. Crea una variable contador que empiece en 1.
    # 2. Recorre la lista nits con un for.
    # 3. Para cada NIT, llama validar_nit(nit).
    # 4. Si el NIT es válido, imprímelo con el número del contador.
    # 5. Aumenta el contador solo cuando imprimas un NIT válido.
    # 6. Este procedimiento no necesita return.
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
    # TODO:
    # 1. Crea variables para total, cantidad y maximo.
    # 2. Recorre cada valor de la lista con un for.
    # 3. Suma cada valor al total.
    # 4. Actualiza el máximo cuando encuentres un valor mayor.
    # 5. Calcula el promedio al final.
    # 6. Retorna total, promedio y maximo.
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
    # TODO:
    # 1. Crea una lista vacía llamada periodos.
    # 2. Usa un for para recorrer los años desde anio_inicio hasta anio_fin.
    # 3. Usa un for interno para recorrer los meses desde 1 hasta meses_por_anio.
    # 4. Construye cada código con formato YYYYMM.
    # 5. Usa :02d para que el mes tenga dos dígitos.
    # 6. Agrega cada código a la lista periodos.
    # 7. Retorna la lista.
    pass


def buscar_primer_valido(nits):
    """
    Busca el primer NIT válido en una lista usando ciclo while.

    Args:
        nits (list): Lista de NITs como cadenas.

    Returns:
        str | None: El primer NIT válido, o None si no hay ninguno.
    """
    # TODO:
    # 1. Crea una variable indice que empiece en 0.
    # 2. Mientras indice sea menor que len(nits), revisa el NIT actual.
    # 3. Si validar_nit(nit_actual) retorna True, retorna ese NIT.
    # 4. Si no es válido, aumenta indice en 1.
    # 5. Si termina el ciclo sin encontrar uno válido, retorna None.
    pass


def sumar_hasta_limite(valores, limite):
    """
    Acumula valores mientras el total no supere el límite usando while.

    Args:
        valores (list): Lista de floats.
        limite (float): Límite de acumulación.

    Returns:
        tuple: (cantidad_procesada, total_acumulado)
    """
    # TODO:
    # 1. Crea total = 0, cantidad = 0 e indice = 0.
    # 2. Mientras indice sea menor que len(valores), revisa el siguiente valor.
    # 3. Si total + siguiente_valor supera limite, detén el ciclo con break.
    # 4. Si no lo supera, suma el valor al total y aumenta cantidad.
    # 5. Avanza el indice en cada vuelta del ciclo.
    # 6. Retorna cantidad y total.
    pass


def encontrar_primer_sobre_umbral(valores, umbral):
    """
    Retorna el primer valor que supere el umbral usando while.

    Args:
        valores (list): Lista de floats.
        umbral (float): Umbral de comparación.

    Returns:
        float | None: Primer valor sobre el umbral, o None.
    """
    # TODO:
    # 1. Crea una variable indice que empiece en 0.
    # 2. Mientras indice sea menor que len(valores), revisa el valor actual.
    # 3. Si el valor actual es mayor que umbral, retorna ese valor.
    # 4. Si no lo es, aumenta indice en 1.
    # 5. Si termina el ciclo sin encontrar un valor mayor, retorna None.
    pass


def validar_secuencia_periodos(periodos):
    """
    Verifica que una lista de períodos esté en orden consecutivo.

    Args:
        periodos (list): Lista de cadenas en formato YYYYMM.

    Returns:
        tuple: (es_valida: bool, indice_salto: int | None)
    """
    # TODO:
    # 1. Recorre la lista comparando cada período con el siguiente.
    # 2. Para cada período, separa el año y el mes.
    # 3. Calcula cuál debería ser el siguiente período:
    #    - si el mes es menor que 12, el siguiente mes es mes + 1;
    #    - si el mes es 12, el siguiente período es enero del año siguiente.
    # 4. Compara el siguiente período real con el período esperado.
    # 5. Si no coinciden, retorna False y el índice donde ocurre el salto.
    # 6. Si no hay saltos, retorna True y None.
    pass


# ---------------------------------------------------------------------------
# LISTAS (operaciones con listas de str y float)
# No usan DECLARACIONES todavía.
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
    # TODO:
    # 1. Revisa si elemento no está en lista.
    # 2. Si no está, agrégalo usando lista.append(elemento).
    # 3. Retorna la lista.
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
    # TODO:
    # 1. Crea una lista vacía para guardar el resultado.
    # 2. Recorre cada valor de valores con un for.
    # 3. Si minimo <= valor <= maximo, agrégalo a la nueva lista.
    # 4. Retorna la nueva lista.
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
    # TODO:
    # 1. Crea una copia de valores para no modificar la lista original.
    # 2. Usa dos ciclos anidados.
    # 3. Compara pares de valores.
    # 4. Si están en el orden incorrecto, intercámbialos.
    # 5. Si descendente es True, ordena de mayor a menor.
    # 6. Si descendente es False, ordena de menor a mayor.
    # 7. Retorna la copia ordenada.
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
    # TODO:
    # 1. Crea un diccionario vacío llamado indice.
    # 2. Recorre cada declaración.
    # 3. Obtén el NIT de la declaración con declaracion["nit"].
    # 4. Usa ese NIT como clave del diccionario.
    # 5. Guarda la declaración completa como valor.
    # 6. Retorna el diccionario indice.
    pass


def construir_resumen_por_estado(declaraciones):
    """
    Agrupa conteo y total de valor por estado.

    Args:
        declaraciones (list): Lista de declaraciones.

    Returns:
        dict: {'ACTIVO': {'conteo': 5, 'total_valor': 9150000}, ...}
    """
    # TODO:
    # 1. Crea un diccionario vacío llamado resumen.
    # 2. Recorre cada declaración.
    # 3. Obtén el estado y el valor de la declaración.
    # 4. Si el estado no existe en resumen, crea una entrada con:
    #    {"conteo": 0, "total_valor": 0}.
    # 5. Aumenta el conteo en 1.
    # 6. Suma el valor al total_valor.
    # 7. Retorna el diccionario resumen.
    pass


def agrupar_por_municipio(declaraciones):
    """
    Agrupa las declaraciones por municipio.

    Args:
        declaraciones (list): Lista de declaraciones.

    Returns:
        dict: Claves = municipios, valores = listas de declaraciones.
    """
    # TODO:
    # 1. Crea un diccionario vacío llamado agrupacion.
    # 2. Recorre cada declaración.
    # 3. Obtén el municipio.
    # 4. Si el municipio no existe como clave, crea una lista vacía.
    # 5. Agrega la declaración completa a la lista de ese municipio.
    # 6. Retorna el diccionario agrupacion.
    pass


def listar_activos(declaraciones):
    """
    Imprime los registros ACTIVOS numerados.

    Args:
        declaraciones (list): Lista de declaraciones.
    """
    # TODO:
    # 1. Crea una variable contador que empiece en 1.
    # 2. Recorre cada declaración.
    # 3. Si declaracion["estado"] es "ACTIVO", imprime sus datos principales.
    # 4. Aumenta el contador solo cuando imprimas un registro activo.
    # 5. Este procedimiento no necesita return.
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
    # TODO:
    # 1. Crea acumuladores para total_registros, total_activos y suma_valores.
    # 2. Crea una variable para valor_maximo.
    # 3. Recorre cada declaración.
    # 4. Aumenta total_registros en cada vuelta.
    # 5. Suma declaracion["valor"] a suma_valores.
    # 6. Si el estado es "ACTIVO", aumenta total_activos.
    # 7. Actualiza valor_maximo cuando encuentres un valor mayor.
    # 8. Calcula promedio_valor usando solo los registros activos.
    # 9. Retorna un diccionario con las estadísticas solicitadas.
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
    # TODO:
    # 1. Crea una lista vacía para guardar el resultado.
    # 2. Recorre cada declaración.
    # 3. Compara declaracion["estado"] con el parámetro estado.
    # 4. Si coinciden, agrega la declaración a la lista resultado.
    # 5. Retorna la lista resultado.
    pass


def buscar_por_nit(declaraciones, nit_buscado):
    """
    Busca la primera declaración con el NIT indicado usando while.

    Args:
        declaraciones (list): Lista de declaraciones.
        nit_buscado (str): NIT a buscar.

    Returns:
        dict | None: Primera declaración encontrada, o None.
    """
    # TODO:
    # 1. Crea una variable indice que empiece en 0.
    # 2. Mientras indice sea menor que len(declaraciones), revisa una declaración.
    # 3. Compara declaracion["nit"] con nit_buscado.
    # 4. Si coinciden, retorna la declaración completa.
    # 5. Si no coinciden, aumenta indice en 1.
    # 6. Si termina el ciclo sin encontrar el NIT, retorna None.
    pass
