txt = " "
cont = 0
def incrementarContador():
    global cont
    cont +=1
    return "%d" %cont

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, symbol_type, scope, value):
        self.symbols[name] = {
            "type": symbol_type,
            "scope": scope,
            "value": value
        }

    def get_symbol(self, name):
        return self.symbols.get(name, None)
    
    def get_type(self, name):
        symbol = self.get_symbol(name)
        if symbol:
            return symbol["type"]
        return None

    def __str__(self):
        table_str = "Nombre\tTipo\tAlcance\tValor\n"
        for name, info in self.symbols.items():
            table_str += f"{name}\t{info['type']}\t{info['scope']}\t{info['value']}\n"
        return table_str
    
# Crear una instancia global de la tabla de símbolos 
symbol_table = SymbolTable()

class Nodo():
    def __init__(self, tipo, valor=None, hijos=None):
        self.tipo = tipo
        self.valor = valor
        self.hijos = hijos if hijos is not None else []

    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)

    def __repr__(self):
        return f"Nodo(tipo={self.tipo}, valor={self.valor}, hijos={self.hijos})"

class Null(Nodo):
    def __init__(self):
        super().__init__(tipo="Null", valor="nodo_nulo", hijos=[])
        self.type = 'void'

    def imprimir(self, ident):
        print(ident + "nodo nulo")

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\"nodo_nulo\"]\n\t"
        return id

class Inicio(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        super().__init__(tipo="Inicio", valor=name, hijos=[son1, son2, son3, son4, son5, son6, son7])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return f'digraph G {{\n\t{txt}}}'

class instruccion(Nodo):
    def __init__(self, son1, son2, name):
        super().__init__(tipo="instruccion", valor=name, hijos=[son1, son2])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class instruccion2(Nodo):
    def __init__(self, son1, son2, name):
        super().__init__(tipo="instruccion2", valor=name, hijos=[son1, son2])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class instruccion3(Nodo):
    def __init__(self, son1, son2, name):
        super().__init__(tipo="instruccion3", valor=name, hijos=[son1, son2])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class instruccion4(Nodo):
    def __init__(self, son1, son2, name):
        super().__init__(tipo="instruccion4", valor=name, hijos=[son1, son2])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class instruccion5(Nodo):
    def __init__(self, son1, son2, name):
        super().__init__(tipo="instruccion5", valor=name, hijos=[son1, son2])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class instruccion6(Nodo):
    def __init__(self, son1, son2, name):
        super().__init__(tipo="instruccion6", valor=name, hijos=[son1, son2])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class instruccion7(Nodo):
    def __init__(self, son1, son2, name):
        super().__init__(tipo="instruccion7", valor=name, hijos=[son1, son2])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

class instruccion8(Nodo):
    def __init__(self, son1, son2, name):
        super().__init__(tipo="instruccion8", valor=name, hijos=[son1, son2])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
        
class dec_variables(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        super().__init__(tipo="dec_variables", valor=name, hijos=[son1, son2, son3, son4])
        self.name = name
        symbol_table.add_symbol(son2.valor, son1.valor, "global", son4.valor)

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class dec_variables2(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        super().__init__(tipo="dec_variables2", valor=name, hijos=[son1, son2, son3, son4])
        self.name = name
        symbol_table.add_symbol(son2.valor, son1.valor, "global", son4.valor)

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class dec_variables3(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        super().__init__(tipo="dec_variables3", valor=name, hijos=[son1, son2, son3, son4])
        self.name = name
        symbol_table.add_symbol(son2.valor, son1.valor, "global", son4.valor)

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class dec_variables4(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        super().__init__(tipo="dec_variables4", valor=name, hijos=[son1, son2, son3, son4, son5, son6])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class dec_variables5(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        super().__init__(tipo="dec_variables5", valor=name, hijos=[son1, son2, son3, son4, son5, son6])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

    
class dec_variables6(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        super().__init__(tipo="dec_variables6", valor=name, hijos=[son1, son2, son3, son4, son5, son6])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class dec_variables7(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        super().__init__(tipo="dec_variables7", valor=name, hijos=[son1, son2, son3, son4, son5, son6])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
 
class dec_if(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        super().__init__(tipo="dec_if", valor=name, hijos=[son1, son2, son3, son4, son5, son6])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class dec_if2(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, name):
        super().__init__(tipo="dec_if2", valor=name, hijos=[son1, son2, son3, son4, son5, son6, son7, son8])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

class dec_while(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        super().__init__(tipo="dec_while", valor=name, hijos=[son1, son2, son3, son4, son5, son6])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
     
class dec_for(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, son9, name):
        super().__init__(tipo="dec_for", valor=name, hijos=[son1, son2, son3, son4, son5, son6, son7, son8, son9])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

class inicializacion_for(Nodo):
    def __init__(self, son1, son2, son3, name):
        super().__init__(tipo="inicializacion_for", valor=name, hijos=[son1, son2, son3])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

class autoincremento_for(Nodo):
    def __init__(self, son1, son2, son3, name):
        super().__init__(tipo="autoincremento_for", valor=name, hijos=[son1, son2, son3])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

    
class autoincremento_for2(Nodo):
    def __init__(self, son1, son2, son3, name):
        super().__init__(tipo="autoincremento_for2", valor=name, hijos=[son1, son2, son3])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
    ##DECLARACION DO-WHILE
class dec_do_while(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, name):
        super().__init__(tipo="dec_do_while", valor=name, hijos=[son1, son2, son3, son4, son5, son6, son7])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

    
class dec_proc(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, name):
        super().__init__(tipo="dec_proc", valor=name, hijos=[son1, son2, son3, son4, son5, son6])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class dec_func(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, son6, son7, son8, name):
        super().__init__(tipo="dec_func", valor=name, hijos=[son1, son2, son3, son4, son5, son6, son7, son8])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id


class recibir_proc_func(Nodo):
    def __init__(self, son1, son2, name):
        super().__init__(tipo="recibir_proc_func", valor=name, hijos=[son1, son2])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

    
class recibir_proc_func2(Nodo):
    def __init__(self, son1, son2, name):
        super().__init__(tipo="recibir_proc_func2", valor=name, hijos=[son1, son2])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

class llamar_proc_func(Nodo):
    def __init__(self, son1, son2, son3, name):
        super().__init__(tipo="llamar_proc_func", valor=name, hijos=[son1, son2, son3])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

        ##LEER Y ESCRIBIR
class dec_leer(Nodo):
    def __init__(self, son1, son2, name):
        super().__init__(tipo="dec_leer", valor=name, hijos=[son1, son2])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

class dec_imprimir(Nodo):
    def __init__(self, son1, son2, son3, name):
        super().__init__(tipo="dec_imprimir", valor=name, hijos=[son1, son2, son3])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class dec_imprimir2(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, name):
        super().__init__(tipo="dec_imprimir2", valor=name, hijos=[son1, son2, son3, son4, son5])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
    
class operador_m(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="operador_m", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
    def verificar_tipos(self):
        tipo1 = symbol_table.get_type(self.operando1.valor) if isinstance(self.operando1, Nodo) and self.operando1.tipo == "NOMBRE" else self.operando1.tipo
        tipo2 = symbol_table.get_type(self.operando2.valor) if isinstance(self.operando2, Nodo) and self.operando2.tipo == "NOMBRE" else self.operando2.tipo
        
        if tipo1 != tipo2:
            raise TypeError(f"Error: Tipos incompatibles para la operación {self.operador}: {tipo1} y {tipo2}")


class operador_m2(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="operador_m2", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

    
class operador_m3(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="operador_m3", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

    
class operador_m4(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="operador_m4", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

    
class condicion(Nodo):
    def __init__(self, son1, son2, son3, son4, son5, name):
        super().__init__(tipo="condicion", valor=name, hijos=[son1, son2, son3, son4, son5])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

class expresion(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="expresion", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class expresion2(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="expresion2", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id 
    
class expresion3(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="expresion3", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

    
class comparador(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="comparador", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

    
class comparador2(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="comparador2", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class comparador3(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="comparador3", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
 
    
class comparador4(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="comparador4", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class comparador5(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="comparador5", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id  
    
class comparador6(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="comparador6", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id 
    
class comparador7(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="comparador7", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id
    
class comparador8(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="comparador8", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id 
    
class opcion_not(Nodo):
    def __init__(self, son1, name):
        super().__init__(tipo="opcion_not", valor=name, hijos=[son1])
        self.name = name

    def imprimir(self, ident):
        for son in self.hijos:
            if isinstance(son, tuple):
                son[0].imprimir(" " + ident)
            else:
                son.imprimir(" " + ident)
        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        traducidos = []
        for son in self.hijos:
            if isinstance(son, tuple):
                traducidos.append(son[0].traducir())
            else:
                traducidos.append(son.traducir())
        txt += f'{id}[label="{self.name}"]\n\t'
        for trad in traducidos:
            txt += f'{id}->{trad}\n\t'
        return id

class DEF(Nodo):
    def __init__(self, name):
        super().__init__(tipo="DEF", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print(ident + "DEF: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\"" + self.name + "\"]\n\t"

        return id

    
class MAIN(Nodo):
    def __init__(self, name):
        super().__init__(tipo="MAIN", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print(ident + "MAIN: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\"" + self.name + "\"]\n\t"

        return id
    
class APERTINICIO(Nodo):
    def __init__(self, name):
        super().__init__(tipo="APERTINICIO", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"APERTINICIO: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class APERTFIN(Nodo):
    def __init__(self, name):
        super().__init__(tipo="APERTFIN", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"APERTFIN: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class T_STRING(Nodo):
    def __init__(self, name):
        super().__init__(tipo="T_STRING", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"APERTFIN: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class NOMBRE(Nodo):
    def __init__(self, name):
        super().__init__(tipo="NOMBRE", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"NOMBRE: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class ASIGNACION(Nodo):
    def __init__(self, name):
        super().__init__(tipo="ASIGNACION", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"ASIGNACION: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class TEXTO(Nodo):
    def __init__(self, name):
        super().__init__(tipo="TEXTO", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"TEXTO: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        # Escapar comillas dobles en el valor de self.name
        safe_name = self.name.replace('"', '\\"')
        txt += id + "[label=\"" + safe_name + "\"]\n\t"

        return id
    
class T_DOUBLE(Nodo):
    def __init__(self, name):
        super().__init__(tipo="T_DOUBLE", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"T_DOUBLE: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class T_PRINT(Nodo):
    def __init__(self, name):
        super().__init__(tipo="T_PRINT", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"T_PRINT: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class NUMEROS(Nodo):
    def __init__(self, name):
        super().__init__(tipo="NUMEROS", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"NUMEROS: "+str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+str(self.name)+"\"]\n\t"

        return id
    
class IF(Nodo):
    def __init__(self, name):
        super().__init__(tipo="IF", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"IF: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class ELSE(Nodo):
    def __init__(self, name):
        super().__init__(tipo="ELSE", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"ELSE: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class WHILE(Nodo):
    def __init__(self, name):
        super().__init__(tipo="WHILE", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"WHILE: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class FOR(Nodo):
    def __init__(self, name):
        super().__init__(tipo="FOR", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"FOR: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class DO(Nodo):
    def __init__(self, name):
        super().__init__(tipo="DO", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"DO: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class RETURN(Nodo):
    def __init__(self, name):
        super().__init__(tipo="RETURN", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"RETURN: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class COMA(Nodo):
    def __init__(self, name):
        super().__init__(tipo="COMA", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"COMA: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class MAS(Nodo):
    def __init__(self, name):
        super().__init__(tipo="MAS", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"MAS: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class MENOS(Nodo):
    def __init__(self, name):
        super().__init__(tipo="MENOS", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"MENOS: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class MULTIPLICACION(Nodo):
    def __init__(self, name):
        super().__init__(tipo="MULTIPLICACION", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"MULTIPLICACION: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class DIVISION(Nodo):
    def __init__(self, name):
        super().__init__(tipo="DIVISION", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"DIVISION: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class IGUALACION(Nodo):
    def __init__(self, name):
        super().__init__(tipo="IGUALACION", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"IGUALACION: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class DIFERENCIA(Nodo):
    def __init__(self, name):
        super().__init__(tipo="DIFERENCIA", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"DIFERENCIA: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
     
class MML(Nodo):
    def __init__(self, name):
        super().__init__(tipo="MML", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"MML: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
     
class MMR(Nodo):
    def __init__(self, name):
        super().__init__(tipo="MMR", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"MMR: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
     
class MMIL(Nodo):
    def __init__(self, name):
        super().__init__(tipo="MMIL", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"MMIL: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
     
class MMIR(Nodo):
    def __init__(self, name):
        super().__init__(tipo="MMIR", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"MMIR: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
     
class OPCI(Nodo):
    def __init__(self, name):
        super().__init__(tipo="OPCI", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"OPCI: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
     
class OPCII(Nodo):
    def __init__(self, name):
        super().__init__(tipo="OPCII", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"OPCII: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class READ(Nodo):
    def __init__(self, name):
        super().__init__(tipo="READ", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"READ: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
     
class NEGACION(Nodo):
    def __init__(self, name):
        super().__init__(tipo="NEGACION", valor=name, hijos=[])
        self.name = name

    def imprimir(self, ident):
        print (ident+"NEGACION: "+self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label=\""+self.name+"\"]\n\t"

        return id
    
class ReglaSemanticaSuma:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def suma(self, var1, var2):
        symbol1 = self.symbol_table.get_symbol(var1)
        symbol2 = self.symbol_table.get_symbol(var2)
        if symbol1 is None:
            raise ValueError(f"Variable '{var1}' no definida en la tabla de símbolos.")
        if symbol2 is None:
            raise ValueError(f"Variable '{var2}' no definida en la tabla de símbolos.")
        if symbol1['type'] != 'elbuod' or symbol2['type'] != 'elbuod':
            raise TypeError("Las variables involucradas en la suma deben ser del tipo 'elbuod' (double).")
        return symbol1['value'] + symbol2['value']
    
    