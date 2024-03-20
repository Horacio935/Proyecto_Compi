import ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['Nombre', 'NUMEROS', 'COMILLAS', 'ESPACIO', 'IGUALACION', 'DIFERENCIA',
          'MML', 'MMR', 'MMIL', 'MMIR', 'OPCI', 'OPCII', 'Asignacion', 'INVALIDO',
          'TEXTO', 'PARENTIZQ', 'PARENTDER'
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
    'oicini': 'LLAVEIZQ',
    'nif': 'LLAVEDER',
    'sam': 'MAS',
    'sonem': 'MENOS',
    'ivid': 'DIVISION',
    'itlum': 'MULTIPLICACION',
    'ton': 'NEGACION'
}

# Obtener solo los valores del diccionario reservadas
valores_reservadas = list(reservadas.values())

# Concatenar la lista tokens con los valores del diccionario reservadas
tokens += valores_reservadas

tokens = tokens + list(reservadas.values())

t_ESPACIO = '\s+'
t_Asignacion = r'='
t_MML = r'<'
t_MMR = r'>'
t_MMIL = r'<='
t_MMIR = r'>='
t_DIFERENCIA = r'!='
t_IGUALACION = r'=='
t_OPCI = r'&&'
t_OPCII = r'\|\|'
t_COMILLAS = r'"|"'
t_PARENTIZQ = r'\('
t_PARENTDER = r'\)'

tabla_simbolos = []  # Inicializamos la tabla de símbolos vacía

def agregar_simbolo(token, tipo, ambito, visibilidad, tamaño, posicion, rol):
    tabla_simbolos.append({'Token': token, 'Tipo': tipo, 'Ambito': ambito, 'Visibilidad': visibilidad,
                           'Tamaño': tamaño, 'Posicion': posicion, 'Rol': rol})

def t_Nombre(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value, 'Nombre')  # Asigna el tipo según las palabras reservadas
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, 'Identificador')
    return t


def t_COMENTARIO(t):
    r'\#.*'
    pass


def t_TEXTO(t):
	r'"[a-zA-Z0-9_\s]*"'
    #agregar_simbolo(t.value, 'TEXTO', 'Global', 'Publico', 0, t.lexpos, 'Texto')
	return t

def t_NUMEROS(t):
     r'\d+\.?\d+'
     t.value = float(t.value)
    # Agregar el símbolo a la tabla
     agregar_simbolo(str(t.value), 'NUMEROS', 'Global', 'Publico', 0, t.lexpos, 'Numero')
     return t

def t_error(t):
    error = f'caracter ilegal "{t.value[0]}" en la linea {t.lineno}, posicion {t.lexpos}'
    with open('bitacora_errores.html', 'a') as f:
        f.write(f'<p>{error}</p>\n')
    print(error)
    t.lexer.skip(1)
     
      
def generar_bitacora(tokens):
    archivo_bitacora = 'bitacora_tokens.html'
    with open(archivo_bitacora, 'w') as f:
        f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Bitacora de Tokens</title>\n</head>\n<body>\n')
        f.write('<table border="1">\n')
        f.write('<tr><th>Token</th><th>Valor</th><th>Línea</th><th>Posición</th></tr>\n')
        for tok in tokens:
            f.write(f'<tr><td align = "center">{tok.type}</td><td align = "center">{tok.value}</td><td align = "center">{tok.lineno}</td><td align = "center">{tok.lexpos}</td></tr>\n')
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
    ficheros = []
    respuesta = False

    while not respuesta:
        nombreArchivo = input('\nRuta completa del archivo: ')
        if os.path.exists(nombreArchivo):
            respuesta = True
        else:
            print("Ruta de archivo inválida. Inténtalo de nuevo.")

    print(f"Has escogido \"{nombreArchivo}\" \n")
    return nombreArchivo


directorio = ''
archivo = buscarFicheros(directorio, extensiones=['.txt', '.rb'])
test = os.path.join(directorio, archivo)
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

tokens_analizados = []
while True:
    tok = analizador.token()
    if not tok:
        break
    tokens_analizados.append(tok)
    print(tok)

generar_bitacora_simbolos(tabla_simbolos)

generar_bitacora(tokens_analizados)

#C:\Users\lopez\OneDrive\Escritorio\UMG\7mo Semestre\Compiladores\ProyectoFinal\tests\prueba2.rb  
