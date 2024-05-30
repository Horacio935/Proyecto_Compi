import ply.yacc as yacc
import os
import codecs
import re
#from lexico import generar_tokens
from lexico import tokens
from sys import stdin   
from datetime import datetime

precedencia = {
    
    ('left', 'instruccion'),
    ('left', 'PRINT'),
    ('left', 'MENOS'),
    ('left', 'MAS'),
    ('left', 'DIVISION'),
    ('left', 'MULTIPLICACION'),
    ('left', 'NOMBRE'),
    ('right', 'WHILE'),
    ('right','dec_proc','dec_func')
}

def p_Inicio(p):
    '''Inicio : DEF MAIN APERTINICIO instruccion APERTFIN dec_proc dec_func'''
    p[0] = p[1], p[2], p[3], p[4]
    

def p_instruccion(p):
    '''instruccion : dec_variables instruccion
                    | dec_if instruccion
                    | dec_while instruccion
                    | dec_for instruccion
                    | dec_do_while instruccion
                    | llamar_proc_func instruccion
                    | dec_leer instruccion
                    | dec_imprimir instruccion
                    | empty'''
    if len(p) == 3:
        p[0] = p[1], p[2]
    else:
        p[0] = p[1]
        
def p_dec_variables(p):
    '''dec_variables : T_STRING NOMBRE ASIGNACION TEXTO
                     | T_DOUBLE NOMBRE ASIGNACION NUMEROS
                     | T_DOUBLE NOMBRE ASIGNACION NUMEROS operador_m NUMEROS
                     | T_DOUBLE NOMBRE ASIGNACION NOMBRE
                     | T_DOUBLE NOMBRE ASIGNACION NOMBRE operador_m NUMEROS
                     | T_DOUBLE NOMBRE ASIGNACION NUMEROS operador_m NOMBRE
                     | T_DOUBLE NOMBRE ASIGNACION NOMBRE operador_m NOMBRE'''
                     #| empty'''
    p[0] = p[1], p[2], p[3], *p[4:]
    

def p_dec_if(p):
    '''dec_if : IF opcion_not condicion APERTINICIO instruccion APERTFIN
              | IF opcion_not condicion APERTINICIO instruccion ELSE instruccion APERTFIN'''
#    p[0] = (p[1], p[2], p[3], p[4], p[5], *p[6:]) if len(p) == 7 else p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]
    if len(p) == 6:
        p[0] = p[1], p[2], p[3], p[4], p[5]
    else:
        p[0] = p[1], p[2], p[3], p[4], p[5], p[6]


def p_dec_while(p):
    '''dec_while : WHILE opcion_not condicion APERTINICIO instruccion APERTFIN'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6]
    
    
def p_dec_for(p):
    '''dec_for : FOR inicializacion COMA condicion COMA autoincremento APERTINICIO instruccion APERTFIN'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]

def p_inicializacion_for(p):
    '''inicializacion : NOMBRE ASIGNACION NUMEROS'''
    p[0] = p[1], p[2], p[3]

def p_autoincremento_for(p):
    '''autoincremento : NOMBRE MAS MAS
                      | NOMBRE MAS NUMEROS'''
    p[0] = p[1], p[2], p[3] if len(p) == 4 else p[1], p[2], p[3]
    
    ##DECLARACION DO-WHILE
def p_dec_do_while(p):
    '''dec_do_while : DO APERTINICIO instruccion APERTFIN WHILE opcion_not condicion '''
    p[0] = p[1], p[2], p[3], p[4], p[5]
    
    
def p_dec_proc(p):
    '''dec_proc : DEF NOMBRE recibir APERTINICIO instruccion APERTFIN
                | empty'''
    if len(p) == 7:
        p[0] = p[1], p[2], p[3], p[4], p[5], p[6]
    else:
        p[0] = p[1]
    
def p_dec_func(p):
    '''dec_func : DEF NOMBRE recibir APERTINICIO instruccion RETURN NOMBRE APERTFIN
                | empty'''
    if len(p) == 8:
        p[0] = p[1], p[2], p[3], p[4], p[5], p[6], p[7]
    else:
        p[0] = p[1]

def p_recibir_proc_func(p):
    '''recibir : T_STRING NOMBRE
               | T_DOUBLE NOMBRE'''
    p[0] = p[1], p[2]

    ##LLAMAR PROCEDIMIENTO Y FUNCION
def p_llamar_proc_func(p):
    '''llamar_proc_func : NOMBRE IGUALACION NOMBRE'''
    p[0] = p[1], p[2]
    #, p[3], p[4]
    
    
        ##LEER Y ESCRIBIR
def p_dec_leer(p):
    '''dec_leer : READ NOMBRE'''
    p[0] = p[1], p[2]
    
    
def p_dec_imprimir(p):
    '''dec_imprimir : T_PRINT ASIGNACION expresion
                    | T_PRINT ASIGNACION expresion MAS expresion'''
    if len(p) == 4:
        p[0] = p[1], p[2], p[3]
    else:
        p[0] = p[1], p[2], p[3], p[4], p[5]
#def p_dec_imprimir(p):
#    '''dec_imprimir : PRINT ASIGNACION imprimir'''
#    p[0] = p[1], p[2], p[3]

#def p_imprimir(p):
#    '''imprimir : NOMBRE
#                | TEXTO
##                | NOMBRE MAS TEXTO imprimir
#                | TEXTO MAS NOMBRE imprimir
#                | empty'''
#    if len(p) == 2:
#        p[0] = p[1]
#    elif len(p) == 4:
##        if p[2].lower() == 'sam': # Verifica si 'MAS' es igual a 'mas'
#            p[0] = (p[1], p[2], p[3], p[4])  # Utiliza 'MAS' tal cual
#        else:
#            p[0] = (p[3], p[2], p[1])
    
    
def p_operador_m(p):
    '''operador_m : MENOS
                  | MAS
                  | DIVISION
                  | MULTIPLICACION'''
    p[0] = p[1]
    
    
def p_condicion(p):
    '''condicion : expresion comparador expresion comparador condicion
                   | empty'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1], p[2], p[3], p[4], p[5]
        

def p_expresion(p):
    '''expresion : TEXTO
                  | NUMEROS
                  | NOMBRE'''
    p[0] = p[1]
    
    
def p_comparador(p):
    '''comparador : IGUALACION
                    | DIFERENCIA
                    | MML
                    | MMR
                    | MMIL
                    | MMIR
                    | OPCI
                    | OPCII
                    | empty'''
    p[0] = p[1]
    
    
def p_opcion_not(p):
    '''opcion_not : NEGACION
                    | empty'''
    p[0] = p[1]
    
##Epsilon
def p_empty(p):
    'empty :'
    p[0]
    pass

##Erro
def contar_lineas_hasta_posicion(texto, posicion):
    # Contador de líneas
    num_lineas = 1
    # Iterar sobre el texto hasta la posición del error
    for i in range(posicion):
        if texto[i] == '\n':
            num_lineas += 1
    return num_lineas

def p_error(p):
    error_message = ""
    if p:
        # Obtener el número de línea en base a la posición del token
        num_linea = contar_lineas_hasta_posicion(p.lexer.lexdata, p.lexpos)
        error_message = f"Error de sintaxis en línea {num_linea}: No se esperaba el token '{p.value}'"
        print(error_message)
    else:
        error_message = "Error de sintaxis: La entrada está incompleta o incorrecta"
        print(error_message)
    # Obtener la fecha y hora actual
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Generar el contenido HTML para el error dentro de una fila de la tabla
    error_html = f"<tr><td>{current_datetime}</td><td>No se esperaba el token '{p.value}'</td><td>{num_linea}</td></tr>"
    # Verificar si el archivo HTML ya existe
    file_exists = os.path.isfile("bitacora_errores_sin.html")
    # Si el archivo no existe, escribir el contenido inicial del HTML con la tabla
    if not file_exists:
        with open("bitacora_errores_sin.html", "w") as error_file:
            error_file.write("<html><head><title>Bitácora de Errores Sintácticos</title></head><body><table border='1'><tr><th>Fecha y Hora</th><th>Error Sintáctico</th><th>Numero de linea</th></tr>")
   
    # Escribir el contenido HTML en el archivo bitacora_errores_sin.html
    with open("bitacora_errores_sin.html", "a") as error_file:
        error_file.write(error_html)

# Agregar el cierre de la tabla y del HTML al final del programa
def cerrar_bitacora():
    with open("bitacora_errores_sin.html", "a") as error_file:
        error_file.write("</table></body></html>")

#def buscar_archivo():
#    respuesta = False

#    ot respuesta:
#        nombre_archivo = input('\nRuta completa del archivo: ')
#        if os.path.exists(nombre_archivo):
#            respuesta = True
#        else:
#            print("Ruta de archivo inválida. Inténtalo de nuevo.")

#    print(f"Has escogido \"{nombre_archivo}\" \n")
#    return nombre_archivo

#directorio = ''
#archivo = buscar_archivo()
#with codecs.open(archivo, "r", "utf-8") as fp:
#    cadena = fp.read()

#tokens_analizados = generar_tokens(cadena)



#parser = yacc.yacc()
#resultado = parser.parse(cadena)

#print(resultado)

def buscarFicheros(ruta, extensiones=['.txt', '.rb']):
    ficheros = []
    respuesta = False

#    for base, dirs, files in os.walk(ruta):
#        ficheros.extend(files)

#        for idx, file in enumerate(files):
#            if file.endswith(tuple(extensiones)):
#                print(f"{idx + 1}. {file}")

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

parser = yacc.yacc('SLR')
resultado = parser.parse(cadena)
print (resultado)


#C:\Users\lopez\OneDrive\Escritorio\UMG\7mo Semestre\Compiladores\ProyectoFinal\tests\prueba1.rb  