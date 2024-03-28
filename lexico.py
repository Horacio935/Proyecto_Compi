import ply.lex as lex
import re
import codecs
import os
import sys
from datetime import datetime

tokens = ['Nombre', 'NUMEROS', 'COMILLAS', 'ESPACIO', 'IGUALACION', 'DIFERENCIA',
          'MML', 'MMR', 'MMIL', 'MMIR', 'OPCI', 'OPCII', 'Asignacion', 'INVALIDO',
          'TEXTO', 'PARENTIZQ', 'PARENTDER', 'COMA',
]

reservadas = {
    'niam': 'main',
    'fi': 'if',
    'esle': 'else',
    'elihw': 'while',
    'rof': 'for',
    'od': 'do',
    'ranroter': 'return',
    'rimirpmi': 'print',
    'reel': 'read',
    'fed': 'def',
    'oicini': 'APERTINICIO',
    'nif': 'APERTFIN',
    'sam': 'MAS',
    'sonem': 'MENOS',
    'ivid': 'DIVISION',
    'itlum': 'MULTIPLICACION',
    'ton': 'NEGACION',
    'elbuod':'t_double',
    'gnirts':'t_string'
}

# Obtiene solo los valores del diccionario reservadas
valores_reservadas = list(reservadas.values())

# Concatenar la lista tokens con los valores del diccionario reservadas, es decir añade las PR a la lista de tokens
tokens += valores_reservadas

tokens = tokens + list(reservadas.values())

tabla_simbolos = []  # Se inicializa la tabla de símbolos vacía

# Crea la tabla hash para almacenar la información de los tokens
tabla_hash = {}

# Declarar variables globales
pos_en_linea = 0
numero_linea_real = 0

def calcular_posicion_en_linea(lexpos, lexer_lexdata):
    global pos_en_linea  # Indicar que se va a modificar la variable global
    pos_en_linea = lexpos - lexer_lexdata.rfind('\n', 0, lexpos)

def calcular_numero_linea_real(lexpos, lexer_lexdata, numero_linea):
    global numero_linea_real  # Indicar que se va a modificar la variable global
    lineas_hasta_antes_del_token = lexer_lexdata[:lexpos].count('\n')
    numero_linea_real = numero_linea + lineas_hasta_antes_del_token + 0

# Define la función para agregar un token a la tabla hash
def agregar_a_tabla_hash(token, tipo, tamaño, posición, rol):
    tabla_hash[token] = {'Tipo': tipo, 'Tamaño': tamaño, 'Posición': posición, 'Rol': rol}

def agregar_simbolo(token, tipo, ambito, visibilidad, tamaño, posicion, rol):
    if tipo == 'TEXTO':
        tamaño = len(token)
    elif tipo == 'NUMEROS':
        tamaño = len(str(token))  # Convertir el número a cadena y calcular su longitud
    elif tipo == 'Nombre':
        tamaño = len(token)
    elif tipo == 'Asignacion':
        tamaño = len(token)
    elif tipo == 'MML':
        tamaño = len(token)
    elif tipo == 'MMR':
        tamaño = len(token)
    elif tipo == 'MMIL':
        tamaño = len(token)
    elif tipo == 'MMIR':
        tamaño = len(token)
    elif tipo == 'DIFERENCIA':
        tamaño = len(token)
    elif tipo == 'IGUALACION':
        tamaño = len(token)
    elif tipo == 'OPCI':
        tamaño = len(token)
    elif tipo == 'OPCII':
        tamaño = len(token)
    elif tipo == 'COMILLAS':
        tamaño = len(token)
    elif tipo == 'PARENTIZQ':
        tamaño = len(token)
    elif tipo == 'PARENTDER':
        tamaño = len(token)
    elif tipo == 'COMA':
        tamaño = len(token)
    elif tipo in valores_reservadas:
        tamaño = len(token)
    agregar_a_tabla_hash(token, tipo, tamaño, posicion, rol)
    tabla_simbolos.append({'Token': token, 'Tipo': tipo, 'Ambito': ambito, 'Visibilidad': visibilidad,
                           'Tamaño': tamaño, 'Posicion': posicion, 'Rol': rol})

def t_Nombre(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    # Asigna el tipo según las palabras reservadas
    t.type = reservadas.get(t.value, 'Nombre')
    # Verifica si el tipo del token es un operador lógico y ajusta el "rol" en la tabla de simbolos
    if t.value in ['sam', 'sonem', 'ivid', 'itlum', 'ton']:
        rol = 'Operadores Comparativos'
    else:
        rol = 'Identificador'
    if t.value in ['niam', 'fi', 'esle', 'elihw', 'rof' ,'od' ,'ranroter' ,'rimirpmi' ,'reel' ,'fed' ,'oicini' ,'nif' ,'elbuod' ,'gnirts']:
        rol = 'Palabra Reservada'
    else:
        rol = 'Identificador'

    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)

    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, pos_en_linea, rol)
    return t

def t_COMENTARIO(t):
    r'\#.*'
    pass

def t_ESPACIO(t):
    r'\s+'
    pass

def t_TEXTO(t):
    r'"[a-zA-Z0-9_\s]*"'
    # Agregar el símbolo a la tabla
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    agregar_simbolo(t.value, 'TEXTO', 'Global', 'Publico', 0, pos_en_linea, 'Texto')
    return t 

def t_Asignacion(t):
    r'='
    # Agregar el símbolo a la tabla
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, pos_en_linea, 'Operador Comparativo')
    return t

def t_MML(t):
    r'<'
    # Agregar el símbolo a la tabla
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, pos_en_linea, 'Operador Comparativo')
    return t

def t_MMR(t):
    r'>'
    # Agregar el símbolo a la tabla
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    agregar_simbolo(t.value, t.type, 'Local', 'Privado', 0, pos_en_linea, 'Operador Comparativo')
    return t

def t_MMIL(t):
    r'<='
    # Agregar el símbolo a la tabla
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, pos_en_linea, 'Operador Comparativo')
    return t

def t_MMIR(t):
    r'>='
    # Agregar el símbolo a la tabla
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, pos_en_linea, 'Operador Comparativo')
    return t

def t_DIFERENCIA(t):
    r'!='
    # Agregar el símbolo a la tabla
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, pos_en_linea, 'Operador Logico')
    return t

def t_IGUALACION(t):
    r'=='
    # Agregar el símbolo a la tabla
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, pos_en_linea, 'Operador Comparativo')
    return t

def t_OPCI(t):
    r'&&'
    # Agregar el símbolo a la tabla
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, pos_en_linea, 'Operador Logico')
    return t

def t_OPCII(t):
    r'\|\|'
    # Agregar el símbolo a la tabla
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, pos_en_linea, 'Operador Logico')
    return t

def t_COMILLAS(t):
    r'"|"'
    # Agregar el símbolo a la tabla
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, pos_en_linea, 'Simbolos')
    return t

def t_PARENTIZQ(t):
    r'\('
    # Agregar el símbolo a la tabla
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, pos_en_linea, 'Operador Logico')
    return t

def t_PARENTDER(t):
    r'\)'
    # Agregar el símbolo a la tabla
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, pos_en_linea, 'Operador Logico')
    return t

def t_COMA(t):
    r','
    # Agregar el símbolo a la tabla
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, pos_en_linea, 'Simbolo')
    return t

def t_NUMEROS(t):
     r'\d+\.?\d+'
     t.value = float(t.value)
    # Agregar el símbolo a la tabla
     calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
     agregar_simbolo(str(t.value), 'NUMEROS', 'Global', 'Publico', 0, pos_en_linea, 'Numero')
     return t

def t_error(t):
    # T.value contiene el caracter no definido, t.lineno contiene el número de línea, t.lexpos contiene la posición del caracter inválido
    error = f'Caracter ilegal "{t.value[0]}"'

    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    calcular_numero_linea_real(t.lexpos, t.lexer.lexdata, numero_linea)
    # Abre (o crea bitacora_errores.html si no existe). 'a' significa que va a añadir los siguientes errores que se encuentren
    with open('bitacora_errores.html', 'a') as f:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write('<table border="1" style="width:50%">\n')  # Añade un estilo para que la tabla ocupe el 100% del ancho disponible
        # Escribe el encabezado de la tabla solo si es la primera vez
        if os.path.getsize('bitacora_errores.html') == 0:
            f.write('<tr><th align = "center" style="width:25%">Error</th><th align = "center" style="width:25%">Línea</th><th align = "center" style="width:25%">Posición</th><th align = "center" style="width:25%">Hora y Fecha</th></tr>\n')
        f.write(f'<tr><td align = "center" style="width:25%">{error}</td><td align = "center" style="width:25%">{numero_linea_real}</td><td align = "center" style="width:25%">{pos_en_linea}</td><td align = "center" style="width:25%">{current_time}</td></tr>\n')
        f.write('</table>\n')
    
    print(error)
    # Pasa al siguiente token para que no se quede "trabado" en un bucle
    t.lexer.skip(1)
     
def generar_bitacora(tokens):
    archivo_bitacora = 'bitacora_tokens.html'
    with open(archivo_bitacora, 'w') as f:
        f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Bitacora de Tokens</title>\n</head>\n<body>\n')
        f.write('<table border="1">\n')
        f.write('<tr><th>Token</th><th>Valor</th><th>Línea</th><th>Posición</th></tr>\n')
        for tok in tokens:
            calcular_posicion_en_linea(tok.lexpos, tok.lexer.lexdata)
            calcular_numero_linea_real(tok.lexpos, tok.lexer.lexdata, numero_linea)
            f.write(f'<tr><td align = "center">{tok.type}</td><td align = "center">{tok.value}</td><td align = "center">{numero_linea_real}</td><td align = "center">{pos_en_linea}</td></tr>\n')
        f.write('</table>\n')
        f.write('</body>\n</html>\n')
    print(f'Se ha generado la bitácora de tokens en el archivo "{archivo_bitacora}"')


def generar_bitacora_simbolos(tabla_simbolos):
    archivo_simbolos = 'tabla_simbolos.html'
    with open(archivo_simbolos, 'w') as f:
        f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Tabla de Símbolos</title>\n</head>\n<body>\n')
        f.write('<h2>Tabla de Símbolos</h2>\n')
        f.write('<table border="1">\n')
        f.write('<tr><th>Token</th><th>Tipo</th><th>Ambito</th><th>Visibilidad</th><th>Tamaño</th><th>Posicion</th><th>Rol</th></tr>\n')
        for simbolo in tabla_simbolos:
            f.write(f'<tr><td>{simbolo["Token"]}</td><td>{simbolo["Tipo"]}</td><td>{simbolo["Ambito"]}</td>'
                    f'<td>{simbolo["Visibilidad"]}</td><td>{simbolo["Tamaño"]}</td><td>{simbolo["Posicion"]}</td>'
                    f'<td>{simbolo["Rol"]}</td></tr>\n')
        f.write('</table>\n')
        f.write('</body>\n</html>\n')
    print(f'Se ha generado la tabla de símbolos en el archivo "{archivo_simbolos}"')

def buscarFicheros(ruta, extensiones=['.txt', '.rb']):
    respuesta = False

    while not respuesta:
        nombreArchivo = input('\nRuta completa del archivo: ')
        if os.path.exists(nombreArchivo):
            respuesta = True
        else:
            print("Ruta de archivo inválida. Inténtalo de nuevo.")

    print(f"Has escogido \"{nombreArchivo}\" \n")
    return nombreArchivo

def imprimir_token(t, numero_linea):
    # Calcular la posición del token en la línea usando la función auxiliar
    calcular_posicion_en_linea(t.lexpos, t.lexer.lexdata)
    # Calcular numero_linea_real usando la función auxiliar anteriormente definida
    calcular_numero_linea_real(t.lexpos, t.lexer.lexdata, numero_linea)
    # Mostrar el token con el número de línea real y la posición en la línea
    print(f"LexToken({t.type}, '{t.value}', {numero_linea_real}, {pos_en_linea})")
    # Agregar el token a la tabla hash
    agregar_a_tabla_hash(t.value, t.type, len(str(t.value)), pos_en_linea, 'Rol')
    
    # Verificar si se ha analizado el último token para imprimir la tabla hash
    if t == tokens_analizados[-1]:
        imprimir_tabla_hash()

def imprimir_tabla_hash():
    print("Tabla Hash de Tokens Analizados:")
    for token, info in tabla_hash.items():
        print(f"Token: {token}, Tipo: {info['Tipo']}, Tamaño: {info['Tamaño']}, Posición: {info['Posición']}, Rol: {info['Rol']}")

directorio = ''
archivo = buscarFicheros(directorio, extensiones=['.txt', '.rb'])
test = os.path.join(directorio, archivo)
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()
analizador.input(cadena)

tokens_analizados = []
numero_linea = 1
while True:
    tok = analizador.token()
    if not tok:
        break
    tokens_analizados.append(tok)
    imprimir_token(tok, numero_linea)

generar_bitacora_simbolos(tabla_simbolos)

generar_bitacora(tokens_analizados)
#C:\Users\lopez\OneDrive\Escritorio\UMG\7mo Semestre\Compiladores\ProyectoFinal\tests\prueba2.rb  
