import ply.lex as lex
import re
import codecs
import os
import sys

tokens = ['Nombre','NUMEROS', 'sam','sonem','ivid','itlum',
          'oicini','nif','COMILLAS','ESPACIO','IGUALACION','DIFERENCIA',
          'MAYORMENOR','MAYORMENORI','OPCION','Asignacion'
]

reservadas = {
    'main':'niam',
    'if':'fi',
    'else':'esle',
    'while':'elihw',
    'for':'rof',
    'do':'od',
    'return':'ranroter',
    'print':'rimirpmi',
    'read':'reel',
    'def':'fed'
}

tokens = tokens+list(reservadas.values())

t_ESPACIO = '\t'
t_sam = r'\+' 
t_sonem = r'\-'
t_ivid = r'/'
t_itlum = r'\*'
t_oicini = r'\{'
t_nif = r'\}'
t_Asignacion = r'='
t_MAYORMENOR = r'<|>'
t_MAYORMENORI = r'<=|>='
t_DIFERENCIA = r'=!|!='
t_IGUALACION = r'=='
t_OPCION = r'&&|\|\|'
t_COMILLAS = r'"|"'


#def t_Nombre(t):
#    r'[a-zA-Z_][a-zA-Z0-9_]*'
#   if t.value.upper() in reservadas:
#        t_value = t.value.upper()
#       t.type = t.value

#    return t

def t_Nombre(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservadas.get(t.value.upper(), 'ID')  # Asigna el tipo según las palabras reservadas de Ruby
    return t


def t_COMMENT(t):
	r'\#.*'
	pass

def t_NUMEROS(t):
     r'\d+(\.\d+)?'
     t.value = float(t.value)
     return t

def t_error(t):
	print ("caracter ilegal '%$'" % t.value[0])
	t.lexer.skip(1)

def buscarFicheros(directorio):
      ficheros =  []
      numArchivo = ''
      respuesta = False
      cont = 1

      for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

        for file in files:
              print (str(cont)+". "+file)
              cont = cont+1

        while respuesta == False:
              numArchivo = input('\nNumero del test: ')
              for file in files:
                   if file == files[int(numArchivo)-1]:
                         respuesta = True
                         break
                   
        print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])


        return files[int(numArchivo)-1]
      
directorio = 'directorio = C:/Users/lopez/OneDrive/Escritorio/UMG/7mo Semestre/Compiladores/ProyectoFinal'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

analizador.input(cadena)

while True:
      tok = analizador.token()
      if not tok : break
      print (tok)