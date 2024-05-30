import ply.yacc as yacc
import os
import graphviz
import codecs
import re
#from lexico import generar_tokens
from lexico import tokens
from sys import stdin   
from datetime import datetime
from semantico import *
from tabla_simbolos import HashTable, tabla_simbolos

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
    #print(type(p[1]), p[2], p[3], p[4], p[5], p[6], p[7])
    p[0] = Inicio(DEF(p[1]), MAIN(p[2]), APERTINICIO(p[3]), p[4], APERTFIN(p[5]), p[6], p[7], "Inicio")
    


def p_instruccion(p):
    '''instruccion : dec_variables instruccion'''
    p[0] = instruccion(p[1], p[2], "Instruccion")

def p_instruccion2(p):
    '''instruccion : dec_if instruccion'''
    p[0] = instruccion2(p[1], p[2], "Instruccion")

def p_instruccion3(p):
    '''instruccion : dec_while instruccion'''
    p[0] = instruccion3(p[1], p[2], "Instruccion")

def p_instruccion4(p):
    '''instruccion : dec_for instruccion'''
    p[0] = instruccion4(p[1], p[2], "Instruccion")

def p_instruccion5(p):
    '''instruccion : dec_do_while instruccion'''
    p[0] = instruccion5(p[1], p[2], "Instruccion")

def p_instruccion6(p):
    '''instruccion : llamar_proc_func instruccion'''
    p[0] = instruccion6(p[1], p[2], "Instruccion")

def p_instruccion7(p):
    '''instruccion : dec_leer instruccion'''
    p[0] = instruccion7(p[1], p[2], "Instruccion")

def p_instruccion8(p):
    '''instruccion : dec_imprimir instruccion'''
    p[0] = instruccion8(p[1], p[2], "Instruccion")

def p_instruccionEmpty(p):
    '''instruccion : empty'''
    p[0] = Null()


        
def p_dec_variables(p):
    '''dec_variables : T_STRING NOMBRE ASIGNACION TEXTO'''
    p[0] = dec_variables(T_STRING(p[1]), NOMBRE(p[2]), ASIGNACION(p[3]), TEXTO(p[4]), "dec_variables")

def p_dec_variables2(p):
    '''dec_variables : T_DOUBLE NOMBRE ASIGNACION NUMEROS'''
    p[0] = dec_variables2(T_DOUBLE(p[1]), NOMBRE(p[2]), ASIGNACION(p[3]), NUMEROS(p[4]), "dec_variables")

def p_dec_variables3(p):
    '''dec_variables : T_DOUBLE NOMBRE ASIGNACION NOMBRE'''
    p[0] = dec_variables3(T_DOUBLE(p[1]), NOMBRE(p[2]), ASIGNACION(p[3]), NOMBRE(p[4]), "dec_variables")

def p_dec_variables4(p):
    '''dec_variables : T_DOUBLE NOMBRE ASIGNACION NUMEROS operador_m NUMEROS'''
    p[0] = dec_variables4(T_DOUBLE(p[1]), NOMBRE(p[2]), ASIGNACION(p[3]), NUMEROS(p[4]), p[5], NUMEROS(p[6]), "dec_variables")

def p_dec_variables5(p):
    '''dec_variables : T_DOUBLE NOMBRE ASIGNACION NOMBRE operador_m NUMEROS'''
    p[0] = dec_variables5(T_DOUBLE(p[1]), NOMBRE(p[2]), ASIGNACION(p[3]), NOMBRE(p[4]), p[5], NUMEROS(p[6]), "dec_variables")

def p_dec_variables6(p):
    '''dec_variables : T_DOUBLE NOMBRE ASIGNACION NUMEROS operador_m NOMBRE'''
    p[0] = dec_variables6(T_DOUBLE(p[1]), NOMBRE(p[2]), ASIGNACION(p[3]), NUMEROS(p[4]), p[5], NOMBRE(p[6]), "dec_variables")

def p_dec_variables7(p):
    '''dec_variables : T_DOUBLE NOMBRE ASIGNACION NOMBRE operador_m NOMBRE'''
    p[0] = dec_variables7(T_DOUBLE(p[1]), NOMBRE(p[2]), ASIGNACION(p[3]), NOMBRE(p[4]), p[5], NOMBRE(p[6]), "dec_variables")



def p_dec_if(p):
    '''dec_if : IF opcion_not condicion APERTINICIO instruccion APERTFIN'''
    p[0] = dec_if(IF(p[1]), p[2], p[3], APERTINICIO(p[4]), p[5], APERTFIN(p[6]), "dec_if")

def p_dec_if2(p):
    '''dec_if : IF opcion_not condicion APERTINICIO instruccion ELSE instruccion APERTFIN'''
    p[0] = dec_if2(IF(p[1]), p[2], p[3], APERTINICIO(p[4]), p[5], ELSE(p[6]), p[7], APERTFIN(p[8]), "dec_if")



def p_dec_while(p):
    '''dec_while : WHILE opcion_not condicion APERTINICIO instruccion APERTFIN'''
    p[0] = dec_while(WHILE(p[1]), p[2], p[3], APERTINICIO(p[4]), p[5], APERTFIN(p[6]), "dec_while")
    
    
def p_dec_for(p):
    '''dec_for : FOR inicializacion COMA condicion COMA autoincremento APERTINICIO instruccion APERTFIN'''
    p[0] = dec_for(FOR(p[1]), p[2], COMA(p[3]), p[4], COMA(p[5]), p[6], APERTINICIO(p[7]), p[8], APERTFIN(p[9]), "dec_for")

def p_inicializacion_for(p):
    '''inicializacion : NOMBRE ASIGNACION NUMEROS'''
    p[0] = inicializacion_for(NOMBRE(p[1]), ASIGNACION(p[2]), NUMEROS(p[3]), "inicializacion_for")

def p_autoincremento_for(p):
    '''autoincremento : NOMBRE MAS MAS'''
    p[0] = autoincremento_for(NOMBRE(p[1]), MAS(p[2]), MAS(p[3]), 'autoincremento_for')

def p_autoincremento_for2(p):
    '''autoincremento : NOMBRE MAS NUMEROS'''
    p[0] = autoincremento_for2(NOMBRE(p[1]), MAS(p[2]), NUMEROS(p[3]), 'autoincremento_for')
    
    ##DECLARACION DO-WHILE
def p_dec_do_while(p):
    '''dec_do_while : DO APERTINICIO instruccion APERTFIN WHILE opcion_not condicion '''
    p[0] = dec_do_while(DO(p[1]), APERTINICIO(p[2]), p[3], APERTFIN(p[4]), WHILE(p[5]), p[6], p[7], "dec_do_while")
    
    
def p_dec_proc(p):
    '''dec_proc : DEF NOMBRE recibir APERTINICIO instruccion APERTFIN'''
    p[0] = dec_proc(DEF(p[1]), NOMBRE(p[2]), p[3], APERTINICIO(p[4]), p[5], APERTFIN(p[6]), "dec_proc")

def p_dec_proceEmpty(p):
    '''dec_proc : empty'''
    p[0] = Null()
    
def p_dec_func(p):
    '''dec_func : DEF NOMBRE recibir APERTINICIO instruccion RETURN NOMBRE APERTFIN'''
    p[0] = dec_func(DEF(p[1]), NOMBRE(p[2]), p[3], APERTINICIO(p[4]), p[5], RETURN(p[6]), NOMBRE(p[7]), APERTFIN(p[8]), "dec_func")

def p_dec_funcEmpty(p):
    '''dec_func : empty'''
    p[0] = Null()


def p_recibir_proc_func(p):
    '''recibir : T_STRING NOMBRE'''
    p[0] = recibir_proc_func(T_STRING(p[1]), NOMBRE(p[2]), "recibir_proc_func")

def p_recibir_proc_func2(p):
    '''recibir : T_DOUBLE NOMBRE'''
    p[0] = recibir_proc_func2(T_DOUBLE(p[1]), NOMBRE(p[2]), "recibir_proc_func")

    ##LLAMAR PROCEDIMIENTO Y FUNCION
def p_llamar_proc_func(p):
    '''llamar_proc_func : NOMBRE IGUALACION NOMBRE'''
    p[0] = llamar_proc_func(NOMBRE(p[1]), IGUALACION([2]), NOMBRE(p[3]), "llamar_proc_func")   
    
        ##LEER Y ESCRIBIR
def p_dec_leer(p):
    '''dec_leer : READ NOMBRE'''
    p[0] = dec_leer(READ(p[1]), NOMBRE(p[2]), "dec_leer")
    
   
def p_dec_imprimir(p):
    '''dec_imprimir : T_PRINT ASIGNACION expresion'''
    p[0] = dec_imprimir(T_PRINT(p[1]), ASIGNACION(p[2]), p[3], "dec_imprimir")

def p_dec_imprimir2(p):
    '''dec_imprimir : T_PRINT ASIGNACION expresion operador_m expresion'''
    p[0] = dec_imprimir2(T_PRINT(p[1]), ASIGNACION(p[2]), p[3], p[4], p[5], "dec_imprimir")

    
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     
def p_operador_m(p):
    '''operador_m : MENOS'''
    p[0] = operador_m(MENOS(p[1]), "operador_m")

def p_operador_m2(p):
    '''operador_m : MAS'''
    p[0] = operador_m2(MAS(p[1]), "operador_m")

def p_operador_m3(p):
    '''operador_m : DIVISION'''
    p[0] = operador_m3(DIVISION(p[1]), "operador_m")

def p_operador_m4(p):
    '''operador_m : MULTIPLICACION'''
    p[0] = operador_m4(MULTIPLICACION(p[1]), "operador_m")
    
def p_condicion(p):
    '''condicion : expresion comparador expresion comparador condicion'''
    p[0] = condicion(p[1], p[2], p[3], p[4], p[5], "condicion")

def p_condicionEmpty(p):
    '''condicion : empty'''
    p[0] = Null()
        

def p_expresion(p):
    '''expresion : TEXTO'''
    p[0] = expresion(TEXTO(p[1]), "expresion")

def p_expresion2(p):
    '''expresion : NUMEROS'''
    p[0] = expresion2(NUMEROS(p[1]), "expresion")

def p_expresion3(p):
    '''expresion : NOMBRE'''
    p[0] = expresion3(NOMBRE(p[1]), "expresion")
    
    
def p_comparador(p):
    '''comparador : IGUALACION'''
    p[0] = comparador(IGUALACION(p[1]), "comparador")

def p_comparador2(p):
    '''comparador : DIFERENCIA'''
    p[0] = comparador2(DIFERENCIA(p[1]), "comparador")

def p_comparador3(p):
    '''comparador : MML'''
    p[0] = comparador3(MML(p[1]), "comparador")

def p_comparador4(p):
    '''comparador : MMR'''
    p[0] = comparador4(MMR(p[1]), "comparador")

def p_comparador5(p):
    '''comparador : MMIL'''
    p[0] = comparador5(MMIL(p[1]), "comparador")

def p_comparador6(p):
    '''comparador : MMIR'''
    p[0] = comparador6(MMIR(p[1]), "comparador")

def p_comparador7(p):
    '''comparador : OPCI'''
    p[0] = comparador7(OPCI(p[1]), "comparador")

def p_comparador8(p):
    '''comparador : OPCII'''
    p[0] = comparador8(OPCII(p[1]), "comparador")

def p_comparadorEmpty(p):
    '''comparador : empty'''
    p[0] = Null()
    
    
def p_opcion_not(p):
    '''opcion_not : NEGACION'''
    p[0] = opcion_not(NEGACION(p[1]), "opcion_not")

def p_opcion_notEmpty(p):
    '''opcion_not : empty'''
    p[0] = Null()
    
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

def traducir(result):
	graphFile = open('graphviztrhee.vz','w')
	graphFile.write(result.traducir())
	graphFile.close()
	print ("El programa traducido se guardo en \"graphviztrhee.vz\"")

def AST_png(file_path, output_path):
    # Leer el contenido del archivo .vz
    with open(file_path, 'r') as file:
        dot_source = file.read()
    
    # Crear un objeto Digraph
    dot = graphviz.Source(dot_source)
    
    # Renderizar el gráfico en formato PNG
    dot.format = 'png'
    dot.render(output_path, cleanup=True)
    print(f"Se genero el arbol sintactico como AST.png")

def AST_html(image_path, html_path):
    # Crear el contenido HTML
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AST</title>
    </head>
    <body>
        <h1>Abstract Syntax Tree (AST)</h1>
        <img src="{image_path}" alt="AST">
    </body>
    </html>
    '''
    # Escribir el contenido HTML en el archivo
    with open(html_path, 'w') as file:
        file.write(html_content)
    print(f"Se guardo el AST en AST.html")

def generar_tabla_html(symbol_table, output_file):
    # Abrir el archivo HTML para escritura
    with open(output_file, 'w') as f:
        # Escribir el encabezado HTML y el inicio de la tabla
        f.write('<!DOCTYPE html>\n<html>\n<head>\n<title>Tabla de Símbolos Variables</title>\n</head>\n<body>\n')
        f.write('<h1>Tabla de Símbolos Variables</h1>\n')
        f.write('<table border="1">\n')
        f.write('<tr><th>Nombre</th><th>Tipo</th><th>Alcance</th><th>Valor</th></tr>\n')

        # Iterar sobre los símbolos y escribir cada fila de la tabla
        for name, info in symbol_table.symbols.items():
            f.write(f'<tr><td>{name}</td><td>{info["type"]}</td><td>{info["scope"]}</td><td>{info["value"]}</td></tr>\n')

        # Cerrar la tabla y el HTML
        f.write('</table>\n</body>\n</html>')

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

parser = yacc.yacc('SLR')
resultado = parser.parse(cadena)
print (resultado)

resultado.imprimir(" ")
#print result.traducir()
traducir(resultado)

AST_png('graphviztrhee.vz', 'AST')
AST_html('AST.png', 'AST.html')

#print(symbol_table)
generar_tabla_html(symbol_table, 'tabla_simbolos_variables.html')
regla_semantica = ReglaSemanticaSuma(symbol_table)


#C:\Users\lopez\OneDrive\Escritorio\UMG\7mo Semestre\Compiladores\ProyectoFinal\tests\prueba1.rb
#C:\Users\lopez\OneDrive\Escritorio\UMG\7mo Semestre\Compiladores\ProyectoFinal\tests\prueba4.rb