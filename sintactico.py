import ply.yacc as yacc
import os
import codecs
import re
from lexico import tokens
from sys import stdin

precedencia = {
    #('left', 'Instruccion'),
    ('left', 't_sonem'),
    ('left', 't_sam'),
    ('left', 't_ivid'),
    ('left', 't_itlum')
}


def p_Inicio(p):
    '''Inicio : def main APERTINICIO instruccion APERTFIN dec_proc dec_func'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6], p[7]

    ##INSTRUCCIONES
def p_instruccion1(p):
    '''instruccion : dec_variables instruccion'''
    p[0] = p[1], p[2]
    
def p_instruccion2(p):
    '''instruccion : dec_if instruccion'''
    p[0] = p[1], p[2]
    
def p_instruccion3(p):
    '''instruccion : dec_while instruccion'''
    p[0] = p[1], p[2]

def p_instruccion4(p):
    '''instruccion : dec_for instruccion'''
    p[0] = p[1], p[2]

def p_instruccion5(p):
    '''instruccion : dec_do_while instruccion'''
    p[0] = p[1], p[2]

def p_instruccion6(p):
    '''instruccion : llamar_proc instruccion'''
    p[0] = p[1], p[2]

def p_instruccion7(p):
    '''instruccion : llamar_func instruccion'''
    p[0] = p[1], p[2]

def p_instruccion8(p):
    '''instruccion : dec_leer instruccion'''
    p[0] = p[1], p[2]

def p_instruccion9(p):
    '''instruccion : dec_imprimir instruccion'''
    p[0] = p[1], p[2]

def p_instruccion10(p):
    '''instruccion : empty'''
    p[0] = p[1]
    


    ##VARIABLES
def p_dec_variables1(p):
    '''dec_variables : t_string Nombre IGUALACION TEXTO'''
    p[0] = p[1], p[2], p[3], p[4]

def p_dec_variables2(p):
    '''dec_variables : t_double Nombre IGUALACION NUMEROS'''
    p[0] = p[1], p[2], p[3], p[4]

def p_dec_variables3(p):
    '''dec_variables : t_double Nombre IGUALACION NUMEROS operador_m NUMEROS'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6]
    
def p_dec_variables4(p):
    '''dec_variables : t_double Nombre IGUALACION Nombre'''
    p[0] = p[1], p[2], p[3], p[4]

def p_dec_variables5(p):
    '''dec_variables : t_double Nombre IGUALACION Nombre operador_m NUMEROS'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6]

def p_dec_variables6(p):
    '''dec_variables : t_double Nombre IGUALACION NUMEROS operador_m Nombres'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6]

#def p_dec_variables7(p):
#    '''dec_variables : t_double Nombre IGUALACION Nombre operador_m NUMEROS'''
#    p[0] = p[1], p[2], p[3], p[4], p[5], p[6]

def p_dec_variables8(p):
    '''dec_variables : t_double Nombre IGUALACION Nombre operador_m Nombre'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6]

def p_dec_variables9(p):
    '''dec_variables : empty'''
    p[0] = p[1]
    

    ##DECLARACION DE IF
def p_dec_if1(p):
    '''dec_if : if opcion_not condicion APERTINICIO instruccion APERTFIN'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6]

def p_dec_if2(p):
    '''dec_if : if opcion_not condicion APERTINICIO instruccion else instruccion APERTFIN'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8]

    ##DECLARACION DE WHILE
def p_dec_while(p):
    '''dec_while : while opcion_not condicion APERTINICIO instruccion APERTFIN'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6]


    ##DECLARACION FOR
def p_dec_for(p):
    '''dec_for : for inicializacion COMA condicion coma autoincremento APERTINICIO instruccion APERTFIN'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]

def p_inicializacion_for(p):
    '''inicializacion : Nombre IGUALACION NUMEROS'''
    p[0] = p[1], p[2], p[3]

def p_autoincremento_for1(p):
    '''autoincremento : Nombre MAS MAS'''
    p[0] = p[1], p[2], p[3]

def p_autoincremento_for2(p):
    '''autoincremento : Nombre MAS NUMEROS'''
    p[0] = p[1], p[2], p[3]


    ##DECLARACION DO-WHILE
def p_dec_do_while(p):
    '''dec_do_while : do instruccion while opcion_not condicion'''
    p[0] = p[1], p[2], p[3], p[4], p[5]

    ##DECLARACION PROCEDIMIENTO Y FUNCION
def p_dec_proc(p):
    '''dec_proc : def Nombre recibir APERTINICIO instruccion APERTFIN'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6]
    
def p_dec_func(p):
    '''dec_func : def Nombre recibir APERTINICIO instruccion retorno Nombre APERTFIN'''
    p[0] = p[1], p[2], p[3], p[4], p[5], p[6]

def p_recibir_proc_func1(p):
    '''recibir : t_string Nombre'''
    p[0] = p[1], p[2]

def p_recibir_proc_func2(p):
    '''recibir : t_double Nombre'''
    p[0] = p[1], p[2]


    ##LLAMAR PROCEDIMIENTO Y FUNCION
def p_llamar_proc(p):
    '''llamar_proc : Nombre PARENTIZQ Nombre PARENTDER'''
    p[0] = p[1], p[2], p[4], p[4]

def p_llamar_func(p):
    '''llamar_func : Nombre PARENTIZQ Nombre PARENTDER'''
    p[0] = p[1], p[2], p[4], p[4]


    ##LEER Y ESCRIBIR
def p_dec_leer(p):
    '''dec_leer : read Nombre'''
    p[0] = p[1], p[2]

def p_dec_imprimir1(p):
    '''dec_imprimir : print Nombre'''
    p[0] = p[1], p[2]
    
def p_dec_imprimir2(p):
    '''dec_imprimir : print TEXTO'''
    p[0] = p[1], p[2]
    
def p_dec_imprimir3(p):
    '''dec_imprimir : print concat'''
    p[0] = p[1], p[2]

def p_concatenacion1(p):
    '''concat : TEXTO MAS Nombre concat'''
    p[0] = p[1], p[2], p[3], p[4]

def p_concatenacion2(p):
    '''concat : Nombre MAS TEXTO concat'''
    p[0] = p[1], p[2], p[3], p[4]

def p_concatenacion3(p):
    '''concat : empty'''
    p[0] = p[1]
    


    ##CONDICION
def p_condicion1(p):
    '''condicion : expresion comparador expresion comparador condicion'''
    p[0] = p[1], p[2], p[3], p[4], p[5]

def p_condicion2(p):
    '''condicion : empty'''
    p[0] = p[1]
    pass

def p_expresion1(p):
    '''expresion : nombre'''
    p[0] = p[1]

def p_expresion2(p):
    '''expresion : NUMEROS'''
    p[0] = p[1]

def p_expresion3(p):
    '''expresion : TEXTO'''
    p[0] = p[1]

    ##Operadores Matematicos
def p_operadorM1(p):
    '''operador_m : t_sonem'''
    p[0] = p[1]
    
def p_operadorM2(p):
    '''operador_m : t_sam'''
    p[0] = p[1]
    
def p_operadorM3(p):
    '''operador_m : t_ivid'''
    p[0] = p[1]
    
def p_operadorM4(p):
    '''operador_m : t_itlum''' 
    p[0] = p[1]           
    
    
    ##cOMPARADORES
def p_comparador1(p):
    '''comparador : igualacion'''
    p[0] = p[1]

def p_comparador2(p):
    '''comparador : diferencia'''
    p[0] = p[1]

def p_comparador3(p):
    '''comparador : MML'''
    p[0] = p[1]

def p_comparador4(p):
    '''comparador : MMR'''
    p[0] = p[1]
    
def p_comparador5(p):
    '''comparador : MMIL'''
    p[0] = p[1]

def p_comparador6(p):
    '''comparador : MMIR'''
    p[0] = p[1]

def p_comparador7(p):
    '''comparador : OPI'''
    p[0] = p[1]

def p_comparador8(p):
    '''comparador : OPII'''
    p[0] = p[1]    
    
def p_comparador9(p):
    '''comparador : empty'''
    p[0] = p[1]
    
    
    
##Epsilon
def p_empty(p):
    'empty :'
    p[0] = p[1]
    pass


##Erro
def p_error(p):
    print("Error de sintaxis", p)
    

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

parser = yacc.yacc()
resultado = parser.pase(cadena)

print (resultado)

