
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'SLR'

_lr_signature = 'APERTFIN APERTFIN APERTINICIO APERTINICIO ASIGNACION COMA COMILLAS DEF DEF DIFERENCIA DIVISION DIVISION DO DO ELSE ELSE ESPACIO FOR FOR IF IF IGUALACION INVALIDO MAIN MAIN MAS MAS MENOS MENOS MMIL MMIR MML MMR MULTIPLICACION MULTIPLICACION NEGACION NEGACION NOMBRE NUMEROS OPCI OPCII PARENTDER PARENTIZQ READ READ RETURN RETURN TEXTO T_DOUBLE T_DOUBLE T_PRINT T_PRINT T_STRING T_STRING WHILE WHILEInicio : DEF MAIN APERTINICIO instruccion APERTFIN dec_proc dec_funcinstruccion : dec_variables instruccioninstruccion : dec_if instruccioninstruccion : dec_while instruccioninstruccion : dec_for instruccioninstruccion : dec_do_while instruccioninstruccion : llamar_proc_func instruccioninstruccion : dec_leer instruccioninstruccion : dec_imprimir instruccioninstruccion : emptydec_variables : T_STRING NOMBRE ASIGNACION TEXTOdec_variables : T_DOUBLE NOMBRE ASIGNACION NUMEROSdec_variables : T_DOUBLE NOMBRE ASIGNACION NOMBREdec_variables : T_DOUBLE NOMBRE ASIGNACION NUMEROS operador_m NUMEROSdec_variables : T_DOUBLE NOMBRE ASIGNACION NOMBRE operador_m NUMEROSdec_variables : T_DOUBLE NOMBRE ASIGNACION NUMEROS operador_m NOMBREdec_variables : T_DOUBLE NOMBRE ASIGNACION NOMBRE operador_m NOMBREdec_if : IF opcion_not condicion APERTINICIO instruccion APERTFINdec_if : IF opcion_not condicion APERTINICIO instruccion ELSE instruccion APERTFINdec_while : WHILE opcion_not condicion APERTINICIO instruccion APERTFINdec_for : FOR inicializacion COMA condicion COMA autoincremento APERTINICIO instruccion APERTFINinicializacion : NOMBRE ASIGNACION NUMEROSautoincremento : NOMBRE MAS MASautoincremento : NOMBRE MAS NUMEROSdec_do_while : DO APERTINICIO instruccion APERTFIN WHILE opcion_not condicion dec_proc : DEF NOMBRE recibir APERTINICIO instruccion APERTFINdec_proc : emptydec_func : DEF NOMBRE recibir APERTINICIO instruccion RETURN NOMBRE APERTFINdec_func : emptyrecibir : T_STRING NOMBRErecibir : T_DOUBLE NOMBREllamar_proc_func : NOMBRE IGUALACION NOMBREdec_leer : READ NOMBREdec_imprimir : T_PRINT ASIGNACION expresiondec_imprimir : T_PRINT ASIGNACION expresion operador_m expresionoperador_m : MENOSoperador_m : MASoperador_m : DIVISIONoperador_m : MULTIPLICACIONcondicion : expresion comparador expresion comparador condicioncondicion : emptyexpresion : TEXTOexpresion : NUMEROSexpresion : NOMBREcomparador : IGUALACIONcomparador : DIFERENCIAcomparador : MMLcomparador : MMRcomparador : MMILcomparador : MMIRcomparador : OPCIcomparador : OPCIIcomparador : emptyopcion_not : NEGACIONopcion_not : emptyempty :'
    
_lr_action_items = {'DEF':([0,4,6,7,8,9,10,11,12,13,18,19,24,36,39,42,46,47,52,58,69,80,96,99,101,110,111,115,117,120,123,],[2,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,45,-56,-56,-56,63,-27,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-26,]),'$end':([1,4,6,7,8,9,10,11,12,13,18,19,24,36,39,42,46,47,52,58,64,65,69,80,96,99,101,110,111,115,117,120,123,132,],[0,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-27,-56,-56,-1,-29,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-26,-28,]),'MAIN':([2,],[3,]),'APERTINICIO':([3,4,6,7,8,9,10,11,12,13,18,19,21,24,36,37,38,39,42,46,51,52,53,54,55,56,57,58,69,71,72,73,74,75,76,77,78,79,80,89,96,99,101,102,103,104,110,111,113,115,117,119,120,127,128,],[4,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,42,-56,-56,-54,-55,-56,-56,-56,69,-56,-41,-42,-43,-44,80,-56,-56,-45,-46,-47,-48,-49,-50,-51,-52,-53,-56,101,-56,-56,-56,-30,-31,117,-56,-56,120,-56,-56,-40,-56,-23,-24,]),'T_STRING':([4,6,7,8,9,10,11,12,13,18,19,24,36,37,38,39,42,43,46,49,52,53,54,55,56,58,61,62,66,67,68,69,71,72,73,74,75,76,77,78,79,80,92,96,99,100,101,105,106,107,108,109,110,111,112,115,117,119,120,122,125,130,],[15,15,15,15,15,15,15,15,15,-56,-56,-56,-56,-54,-55,-56,15,-33,-56,-32,-56,-41,-42,-43,-44,-56,-34,90,-11,-13,-12,15,-45,-46,-47,-48,-49,-50,-51,-52,-53,15,90,-56,-56,-35,15,-17,-15,-16,-14,-18,15,-56,-20,-56,15,-40,15,-25,-19,-21,]),'T_DOUBLE':([4,6,7,8,9,10,11,12,13,18,19,24,36,37,38,39,42,43,46,49,52,53,54,55,56,58,61,62,66,67,68,69,71,72,73,74,75,76,77,78,79,80,92,96,99,100,101,105,106,107,108,109,110,111,112,115,117,119,120,122,125,130,],[17,17,17,17,17,17,17,17,17,-56,-56,-56,-56,-54,-55,-56,17,-33,-56,-32,-56,-41,-42,-43,-44,-56,-34,91,-11,-13,-12,17,-45,-46,-47,-48,-49,-50,-51,-52,-53,17,91,-56,-56,-35,17,-17,-15,-16,-14,-18,17,-56,-20,-56,17,-40,17,-25,-19,-21,]),'IF':([4,6,7,8,9,10,11,12,13,18,19,24,36,37,38,39,42,43,46,49,52,53,54,55,56,58,61,66,67,68,69,71,72,73,74,75,76,77,78,79,80,96,99,100,101,105,106,107,108,109,110,111,112,115,117,119,120,122,125,130,],[18,18,18,18,18,18,18,18,18,-56,-56,-56,-56,-54,-55,-56,18,-33,-56,-32,-56,-41,-42,-43,-44,-56,-34,-11,-13,-12,18,-45,-46,-47,-48,-49,-50,-51,-52,-53,18,-56,-56,-35,18,-17,-15,-16,-14,-18,18,-56,-20,-56,18,-40,18,-25,-19,-21,]),'WHILE':([4,6,7,8,9,10,11,12,13,18,19,24,36,37,38,39,42,43,46,49,52,53,54,55,56,58,61,66,67,68,69,71,72,73,74,75,76,77,78,79,80,83,96,99,100,101,105,106,107,108,109,110,111,112,115,117,119,120,122,125,130,],[19,19,19,19,19,19,19,19,19,-56,-56,-56,-56,-54,-55,-56,19,-33,-56,-32,-56,-41,-42,-43,-44,-56,-34,-11,-13,-12,19,-45,-46,-47,-48,-49,-50,-51,-52,-53,19,99,-56,-56,-35,19,-17,-15,-16,-14,-18,19,-56,-20,-56,19,-40,19,-25,-19,-21,]),'FOR':([4,6,7,8,9,10,11,12,13,18,19,24,36,37,38,39,42,43,46,49,52,53,54,55,56,58,61,66,67,68,69,71,72,73,74,75,76,77,78,79,80,96,99,100,101,105,106,107,108,109,110,111,112,115,117,119,120,122,125,130,],[20,20,20,20,20,20,20,20,20,-56,-56,-56,-56,-54,-55,-56,20,-33,-56,-32,-56,-41,-42,-43,-44,-56,-34,-11,-13,-12,20,-45,-46,-47,-48,-49,-50,-51,-52,-53,20,-56,-56,-35,20,-17,-15,-16,-14,-18,20,-56,-20,-56,20,-40,20,-25,-19,-21,]),'DO':([4,6,7,8,9,10,11,12,13,18,19,24,36,37,38,39,42,43,46,49,52,53,54,55,56,58,61,66,67,68,69,71,72,73,74,75,76,77,78,79,80,96,99,100,101,105,106,107,108,109,110,111,112,115,117,119,120,122,125,130,],[21,21,21,21,21,21,21,21,21,-56,-56,-56,-56,-54,-55,-56,21,-33,-56,-32,-56,-41,-42,-43,-44,-56,-34,-11,-13,-12,21,-45,-46,-47,-48,-49,-50,-51,-52,-53,21,-56,-56,-35,21,-17,-15,-16,-14,-18,21,-56,-20,-56,21,-40,21,-25,-19,-21,]),'NOMBRE':([4,6,7,8,9,10,11,12,13,15,17,18,19,20,22,24,34,36,37,38,39,42,43,44,45,46,49,50,52,53,54,55,56,58,61,63,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,87,88,90,91,93,94,96,98,99,100,101,105,106,107,108,109,110,111,112,115,117,119,120,122,125,129,130,],[16,16,16,16,16,16,16,16,16,33,35,-56,-56,41,43,-56,49,56,-54,-55,56,16,-33,56,62,-56,-32,67,-56,-41,-42,-43,-44,56,-34,92,-11,-13,-12,16,56,-45,-46,-47,-48,-49,-50,-51,-52,-53,16,56,-36,-37,-38,-39,102,103,105,107,-56,114,-56,-35,16,-17,-15,-16,-14,-18,16,56,-20,56,16,-40,16,-25,-19,131,-21,]),'READ':([4,6,7,8,9,10,11,12,13,18,19,24,36,37,38,39,42,43,46,49,52,53,54,55,56,58,61,66,67,68,69,71,72,73,74,75,76,77,78,79,80,96,99,100,101,105,106,107,108,109,110,111,112,115,117,119,120,122,125,130,],[22,22,22,22,22,22,22,22,22,-56,-56,-56,-56,-54,-55,-56,22,-33,-56,-32,-56,-41,-42,-43,-44,-56,-34,-11,-13,-12,22,-45,-46,-47,-48,-49,-50,-51,-52,-53,22,-56,-56,-35,22,-17,-15,-16,-14,-18,22,-56,-20,-56,22,-40,22,-25,-19,-21,]),'T_PRINT':([4,6,7,8,9,10,11,12,13,18,19,24,36,37,38,39,42,43,46,49,52,53,54,55,56,58,61,66,67,68,69,71,72,73,74,75,76,77,78,79,80,96,99,100,101,105,106,107,108,109,110,111,112,115,117,119,120,122,125,130,],[23,23,23,23,23,23,23,23,23,-56,-56,-56,-56,-54,-55,-56,23,-33,-56,-32,-56,-41,-42,-43,-44,-56,-34,-11,-13,-12,23,-45,-46,-47,-48,-49,-50,-51,-52,-53,23,-56,-56,-35,23,-17,-15,-16,-14,-18,23,-56,-20,-56,23,-40,23,-25,-19,-21,]),'APERTFIN':([4,5,6,7,8,9,10,11,12,13,14,18,19,24,25,26,27,28,29,30,31,32,36,37,38,39,42,43,46,49,52,53,54,55,56,58,60,61,66,67,68,69,71,72,73,74,75,76,77,78,79,80,95,96,97,99,100,101,105,106,107,108,109,110,111,112,115,116,117,118,119,120,122,125,126,130,131,],[-56,24,-56,-56,-56,-56,-56,-56,-56,-56,-10,-56,-56,-56,-2,-3,-4,-5,-6,-7,-8,-9,-56,-54,-55,-56,-56,-33,-56,-32,-56,-41,-42,-43,-44,-56,83,-34,-11,-13,-12,-56,-45,-46,-47,-48,-49,-50,-51,-52,-53,-56,109,-56,112,-56,-35,-56,-17,-15,-16,-14,-18,-56,-56,-20,-56,123,-56,125,-40,-56,-25,-19,130,-21,132,]),'COMA':([4,6,7,8,9,10,11,12,13,18,19,24,36,39,40,42,46,52,53,54,55,56,58,69,71,72,73,74,75,76,77,78,79,80,81,82,96,99,101,110,111,115,117,119,120,],[-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,58,-56,-56,-56,-41,-42,-43,-44,-56,-56,-45,-46,-47,-48,-49,-50,-51,-52,-53,-56,98,-22,-56,-56,-56,-56,-56,-56,-56,-40,-56,]),'TEXTO':([4,6,7,8,9,10,11,12,13,18,19,24,36,37,38,39,42,44,46,48,52,54,55,56,58,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,87,88,96,99,101,110,111,115,117,120,],[-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,54,-54,-55,54,-56,54,-56,66,-56,-42,-43,-44,54,-56,54,-45,-46,-47,-48,-49,-50,-51,-52,-53,-56,54,-36,-37,-38,-39,-56,-56,-56,-56,54,54,-56,-56,]),'NUMEROS':([4,6,7,8,9,10,11,12,13,18,19,24,36,37,38,39,42,44,46,50,52,54,55,56,58,59,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,87,88,93,94,96,99,101,110,111,115,117,120,121,],[-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,-56,55,-54,-55,55,-56,55,-56,68,-56,-42,-43,-44,55,82,-56,55,-45,-46,-47,-48,-49,-50,-51,-52,-53,-56,55,-36,-37,-38,-39,106,108,-56,-56,-56,-56,55,55,-56,-56,128,]),'ELSE':([4,6,7,8,9,10,11,12,13,14,18,19,24,25,26,27,28,29,30,31,32,36,37,38,39,42,43,46,49,52,53,54,55,56,58,61,66,67,68,69,71,72,73,74,75,76,77,78,79,80,95,96,99,100,101,105,106,107,108,109,110,111,112,115,117,119,120,122,125,130,],[-56,-56,-56,-56,-56,-56,-56,-56,-56,-10,-56,-56,-56,-2,-3,-4,-5,-6,-7,-8,-9,-56,-54,-55,-56,-56,-33,-56,-32,-56,-41,-42,-43,-44,-56,-34,-11,-13,-12,-56,-45,-46,-47,-48,-49,-50,-51,-52,-53,-56,110,-56,-56,-35,-56,-17,-15,-16,-14,-18,-56,-56,-20,-56,-56,-40,-56,-25,-19,-21,]),'RETURN':([4,6,7,8,9,10,11,12,13,14,18,19,24,25,26,27,28,29,30,31,32,36,37,38,39,42,43,46,49,52,53,54,55,56,58,61,66,67,68,69,71,72,73,74,75,76,77,78,79,80,96,99,100,101,105,106,107,108,109,110,111,112,115,117,119,120,122,124,125,130,],[-56,-56,-56,-56,-56,-56,-56,-56,-56,-10,-56,-56,-56,-2,-3,-4,-5,-6,-7,-8,-9,-56,-54,-55,-56,-56,-33,-56,-32,-56,-41,-42,-43,-44,-56,-34,-11,-13,-12,-56,-45,-46,-47,-48,-49,-50,-51,-52,-53,-56,-56,-56,-35,-56,-17,-15,-16,-14,-18,-56,-56,-20,-56,-56,-40,-56,-25,129,-19,-21,]),'IGUALACION':([16,52,54,55,56,96,],[34,71,-42,-43,-44,71,]),'NEGACION':([18,19,99,],[37,37,37,]),'ASIGNACION':([23,33,35,41,],[44,48,50,59,]),'DIFERENCIA':([52,54,55,56,96,],[72,-42,-43,-44,72,]),'MML':([52,54,55,56,96,],[73,-42,-43,-44,73,]),'MMR':([52,54,55,56,96,],[74,-42,-43,-44,74,]),'MMIL':([52,54,55,56,96,],[75,-42,-43,-44,75,]),'MMIR':([52,54,55,56,96,],[76,-42,-43,-44,76,]),'OPCI':([52,54,55,56,96,],[77,-42,-43,-44,77,]),'OPCII':([52,54,55,56,96,],[78,-42,-43,-44,78,]),'MENOS':([54,55,56,61,67,68,],[-42,-43,-44,85,85,85,]),'MAS':([54,55,56,61,67,68,114,121,],[-42,-43,-44,86,86,86,121,127,]),'DIVISION':([54,55,56,61,67,68,],[-42,-43,-44,87,87,87,]),'MULTIPLICACION':([54,55,56,61,67,68,],[-42,-43,-44,88,88,88,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Inicio':([0,],[1,]),'instruccion':([4,6,7,8,9,10,11,12,13,42,69,80,101,110,117,120,],[5,25,26,27,28,29,30,31,32,60,95,97,116,118,124,126,]),'dec_variables':([4,6,7,8,9,10,11,12,13,42,69,80,101,110,117,120,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'dec_if':([4,6,7,8,9,10,11,12,13,42,69,80,101,110,117,120,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'dec_while':([4,6,7,8,9,10,11,12,13,42,69,80,101,110,117,120,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'dec_for':([4,6,7,8,9,10,11,12,13,42,69,80,101,110,117,120,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'dec_do_while':([4,6,7,8,9,10,11,12,13,42,69,80,101,110,117,120,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'llamar_proc_func':([4,6,7,8,9,10,11,12,13,42,69,80,101,110,117,120,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'dec_leer':([4,6,7,8,9,10,11,12,13,42,69,80,101,110,117,120,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'dec_imprimir':([4,6,7,8,9,10,11,12,13,42,69,80,101,110,117,120,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'empty':([4,6,7,8,9,10,11,12,13,18,19,24,36,39,42,46,52,58,69,80,96,99,101,110,111,115,117,120,],[14,14,14,14,14,14,14,14,14,38,38,47,53,53,14,65,79,53,14,14,79,38,14,14,53,53,14,14,]),'opcion_not':([18,19,99,],[36,39,115,]),'inicializacion':([20,],[40,]),'dec_proc':([24,],[46,]),'condicion':([36,39,58,111,115,],[51,57,81,119,122,]),'expresion':([36,39,44,58,70,84,111,115,],[52,52,61,52,96,100,52,52,]),'dec_func':([46,],[64,]),'comparador':([52,96,],[70,111,]),'operador_m':([61,67,68,],[84,93,94,]),'recibir':([62,92,],[89,104,]),'autoincremento':([98,],[113,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Inicio","S'",1,None,None,None),
  ('Inicio -> DEF MAIN APERTINICIO instruccion APERTFIN dec_proc dec_func','Inicio',7,'p_Inicio','sintactico.py',25),
  ('instruccion -> dec_variables instruccion','instruccion',2,'p_instruccion','sintactico.py',32),
  ('instruccion -> dec_if instruccion','instruccion',2,'p_instruccion2','sintactico.py',36),
  ('instruccion -> dec_while instruccion','instruccion',2,'p_instruccion3','sintactico.py',40),
  ('instruccion -> dec_for instruccion','instruccion',2,'p_instruccion4','sintactico.py',44),
  ('instruccion -> dec_do_while instruccion','instruccion',2,'p_instruccion5','sintactico.py',48),
  ('instruccion -> llamar_proc_func instruccion','instruccion',2,'p_instruccion6','sintactico.py',52),
  ('instruccion -> dec_leer instruccion','instruccion',2,'p_instruccion7','sintactico.py',56),
  ('instruccion -> dec_imprimir instruccion','instruccion',2,'p_instruccion8','sintactico.py',60),
  ('instruccion -> empty','instruccion',1,'p_instruccionEmpty','sintactico.py',64),
  ('dec_variables -> T_STRING NOMBRE ASIGNACION TEXTO','dec_variables',4,'p_dec_variables','sintactico.py',70),
  ('dec_variables -> T_DOUBLE NOMBRE ASIGNACION NUMEROS','dec_variables',4,'p_dec_variables2','sintactico.py',74),
  ('dec_variables -> T_DOUBLE NOMBRE ASIGNACION NOMBRE','dec_variables',4,'p_dec_variables3','sintactico.py',78),
  ('dec_variables -> T_DOUBLE NOMBRE ASIGNACION NUMEROS operador_m NUMEROS','dec_variables',6,'p_dec_variables4','sintactico.py',82),
  ('dec_variables -> T_DOUBLE NOMBRE ASIGNACION NOMBRE operador_m NUMEROS','dec_variables',6,'p_dec_variables5','sintactico.py',86),
  ('dec_variables -> T_DOUBLE NOMBRE ASIGNACION NUMEROS operador_m NOMBRE','dec_variables',6,'p_dec_variables6','sintactico.py',90),
  ('dec_variables -> T_DOUBLE NOMBRE ASIGNACION NOMBRE operador_m NOMBRE','dec_variables',6,'p_dec_variables7','sintactico.py',94),
  ('dec_if -> IF opcion_not condicion APERTINICIO instruccion APERTFIN','dec_if',6,'p_dec_if','sintactico.py',100),
  ('dec_if -> IF opcion_not condicion APERTINICIO instruccion ELSE instruccion APERTFIN','dec_if',8,'p_dec_if2','sintactico.py',104),
  ('dec_while -> WHILE opcion_not condicion APERTINICIO instruccion APERTFIN','dec_while',6,'p_dec_while','sintactico.py',110),
  ('dec_for -> FOR inicializacion COMA condicion COMA autoincremento APERTINICIO instruccion APERTFIN','dec_for',9,'p_dec_for','sintactico.py',115),
  ('inicializacion -> NOMBRE ASIGNACION NUMEROS','inicializacion',3,'p_inicializacion_for','sintactico.py',119),
  ('autoincremento -> NOMBRE MAS MAS','autoincremento',3,'p_autoincremento_for','sintactico.py',123),
  ('autoincremento -> NOMBRE MAS NUMEROS','autoincremento',3,'p_autoincremento_for2','sintactico.py',127),
  ('dec_do_while -> DO APERTINICIO instruccion APERTFIN WHILE opcion_not condicion','dec_do_while',7,'p_dec_do_while','sintactico.py',132),
  ('dec_proc -> DEF NOMBRE recibir APERTINICIO instruccion APERTFIN','dec_proc',6,'p_dec_proc','sintactico.py',137),
  ('dec_proc -> empty','dec_proc',1,'p_dec_proceEmpty','sintactico.py',141),
  ('dec_func -> DEF NOMBRE recibir APERTINICIO instruccion RETURN NOMBRE APERTFIN','dec_func',8,'p_dec_func','sintactico.py',145),
  ('dec_func -> empty','dec_func',1,'p_dec_funcEmpty','sintactico.py',149),
  ('recibir -> T_STRING NOMBRE','recibir',2,'p_recibir_proc_func','sintactico.py',154),
  ('recibir -> T_DOUBLE NOMBRE','recibir',2,'p_recibir_proc_func2','sintactico.py',158),
  ('llamar_proc_func -> NOMBRE IGUALACION NOMBRE','llamar_proc_func',3,'p_llamar_proc_func','sintactico.py',163),
  ('dec_leer -> READ NOMBRE','dec_leer',2,'p_dec_leer','sintactico.py',168),
  ('dec_imprimir -> T_PRINT ASIGNACION expresion','dec_imprimir',3,'p_dec_imprimir','sintactico.py',173),
  ('dec_imprimir -> T_PRINT ASIGNACION expresion operador_m expresion','dec_imprimir',5,'p_dec_imprimir2','sintactico.py',177),
  ('operador_m -> MENOS','operador_m',1,'p_operador_m','sintactico.py',183),
  ('operador_m -> MAS','operador_m',1,'p_operador_m2','sintactico.py',187),
  ('operador_m -> DIVISION','operador_m',1,'p_operador_m3','sintactico.py',191),
  ('operador_m -> MULTIPLICACION','operador_m',1,'p_operador_m4','sintactico.py',195),
  ('condicion -> expresion comparador expresion comparador condicion','condicion',5,'p_condicion','sintactico.py',199),
  ('condicion -> empty','condicion',1,'p_condicionEmpty','sintactico.py',203),
  ('expresion -> TEXTO','expresion',1,'p_expresion','sintactico.py',208),
  ('expresion -> NUMEROS','expresion',1,'p_expresion2','sintactico.py',212),
  ('expresion -> NOMBRE','expresion',1,'p_expresion3','sintactico.py',216),
  ('comparador -> IGUALACION','comparador',1,'p_comparador','sintactico.py',221),
  ('comparador -> DIFERENCIA','comparador',1,'p_comparador2','sintactico.py',225),
  ('comparador -> MML','comparador',1,'p_comparador3','sintactico.py',229),
  ('comparador -> MMR','comparador',1,'p_comparador4','sintactico.py',233),
  ('comparador -> MMIL','comparador',1,'p_comparador5','sintactico.py',237),
  ('comparador -> MMIR','comparador',1,'p_comparador6','sintactico.py',241),
  ('comparador -> OPCI','comparador',1,'p_comparador7','sintactico.py',245),
  ('comparador -> OPCII','comparador',1,'p_comparador8','sintactico.py',249),
  ('comparador -> empty','comparador',1,'p_comparadorEmpty','sintactico.py',253),
  ('opcion_not -> NEGACION','opcion_not',1,'p_opcion_not','sintactico.py',258),
  ('opcion_not -> empty','opcion_not',1,'p_opcion_notEmpty','sintactico.py',262),
  ('empty -> <empty>','empty',0,'p_empty','sintactico.py',267),
]
