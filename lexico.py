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

t_ESPACIO = '\s+'
#t_Asignacion = r'=' #Operador Comparativo
#t_MML = r'<' #Operador Comparativo
#t_MMR = r'>' #Operador Comparativo
#t_MMIL = r'<=' #Operador Comparativo
#t_MMIR = r'>=' #Operador Comparativo
#t_DIFERENCIA = r'!=' #Operador Logico
#t_IGUALACION = r'==' #Operador Comparativo
#t_OPCI = r'&&' #Operador Logico
#t_OPCII = r'\|\|' #Operador Logico
#t_COMILLAS = r'"|"' #Simbolo
#t_PARENTIZQ = r'\(' #Operador Logico
#t_PARENTDER = r'\)' #Operador Logico
#t_COMA = r',' #Simbolo

tabla_simbolos = []  # Se inicializa la tabla de símbolos vacía

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
    # Agregar el símbolo a la tabla con el rol correspondiente
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, rol)
    return t

def t_COMENTARIO(t):
    r'\#.*'
    pass

def t_TEXTO(t):
    r'"[a-zA-Z0-9_\s]*"'
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, 'TEXTO', 'Global', 'Publico', 0, t.lexpos, 'Texto')
    return t

def t_Asignacion(t):
    r'='
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, 'Operador Comparativo')
    return t

def t_MML(t):
    r'<'
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, 'Operador Comparativo')
    return t

def t_MMR(t):
    r'>'
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, 'Operador Comparativo')
    return t

def t_MMIL(t):
    r'<='
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, 'Operador Comparativo')
    return t

def t_MMIR(t):
    r'>='
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, 'Operador Comparativo')
    return t

def t_DIFERENCIA(t):
    r'!='
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, 'Operador Logico')
    return t

def t_IGUALACION(t):
    r'=='
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, 'Operador Comparativo')
    return t

def t_OPCI(t):
    r'&&'
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, 'Operador Logico')
    return t

def t_OPCII(t):
    r'\|\|'
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, 'Operador Logico')
    return t

def t_COMILLAS(t):
    r'"|"'
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, 'Simbolos')
    return t

def t_PARENTIZQ(t):
    r'\('
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, 'Operador Logico')
    return t

def t_PARENTDER(t):
    r'\)'
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, 'Operador Logico')
    return t

def t_COMA(t):
    r','
    # Agregar el símbolo a la tabla
    agregar_simbolo(t.value, t.type, 'Global', 'Publico', 0, t.lexpos, 'Simbolo')
    return t

def t_NUMEROS(t):
     r'\d+\.?\d+'
     t.value = float(t.value)
    # Agregar el símbolo a la tabla
     agregar_simbolo(str(t.value), 'NUMEROS', 'Global', 'Publico', 0, t.lexpos, 'Numero')
     return t

#def t_error(t):
 #   error = f'caracter ilegal "{t.value[0]}" en la linea {t.lineno}, posicion {t.lexpos}'
    
 #   with open('bitacora_errores.html', 'a') as f:
  #      f.write(f'<p>{error}</p>\n')
  #  print(error)
  #  t.lexer.skip(1)

def t_error(t):
    #T.value el caracter no definido, t.lineno numero de linea, t.lexpos posicion del caracter invalido
    error = f'caracter ilegal "{t.value[0]}" en la linea {t.lineno}, posicion {t.lexpos}'
    #Abre (o crea bitacora_errores.html si no existe), 'a' significa que va a añadir los siguientes errores que se encuentren
    with open('bitacora_errores.html', 'a') as f:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f'<p>{error} - {current_time}</p>\n')
    print(error)
    #Pasa al siguiente token para que no se quede "trabado" en un bucle
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