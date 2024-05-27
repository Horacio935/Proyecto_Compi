class LL1Parser:
    def __init__(self):
        self.rules = {
            'E': [['T', "E'"]],
            "E'": [['+', 'T', "E'"], ['e']],  # Cambiado 'ε' por 'e'
            'T': [['F', "T'"]],
            "T'": [['*', 'F', "T'"], ['e']],  # Cambiado 'ε' por 'e'
            'F': [['id'], ['(', 'E', ')']]
        }

        self.first = {
            'E': ['id', '('],
            "E'": ['+', 'e'],  # Cambiado 'ε' por 'e'
            'T': ['id', '('],
            "T'": ['*', 'e'],  # Cambiado 'ε' por 'e'
            'F': ['id', '(']
        }

        self.follow = {
            'E': [')', '$'],
            "E'": [')', '$'],
            'T': ['+', ')', '$'],
            "T'": ['+', ')', '$'],
            'F': ['+', '*', ')', '$']
        }

        self.parse_table = {
            ('E', 'id'): ['T', "E'"],
            ('E', '('): ['T', "E'"],
            ("E'", '+'): ['+', 'T', "E'"],
            ("E'", ')'): ['e'],  # Cambiado 'ε' por 'e'
            ("E'", '$'): ['e'],  # Cambiado 'ε' por 'e'
            ('T', 'id'): ['F', "T'"],
            ('T', '('): ['F', "T'"],
            ("T'", '+'): ['e'],  # Cambiado 'ε' por 'e'
            ("T'", '*'): ['*', 'F', "T'"],
            ("T'", ')'): ['e'],  # Cambiado 'ε' por 'e'
            ("T'", '$'): ['e'],  # Cambiado 'ε' por 'e'
            ('F', 'id'): ['id'],
            ('F', '('): ['(', 'E', ')']
        }

    def parse(self, tokens):
        stack = ['$', 'E']
        index = 0

        while stack:
            top = stack.pop()
            token = tokens[index]

            if top == 'e':
                continue

            if top == token:
                index += 1
                if token == '$':
                    return True
            elif top in self.rules:
                rule = self.parse_table.get((top, token))
                if rule:
                    for symbol in reversed(rule):
                        stack.append(symbol)
                else:
                    return False
            else:
                return False
        return False

    def save_to_html(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('<html><head><style>')
            f.write('table { border-collapse: collapse; width: 50%; }')  # Ajustar ancho de la tabla
            f.write('th, td { border: 1px solid black; text-align: center; padding: 4px; width: 60px; }')  # Ajustar ancho de las celdas
            f.write('th { background-color: #f2f2f2; }')
            f.write('</style></head><body>\n')
            f.write('<h1>First Sets</h1>\n')
            f.write('<table>\n')
            for non_terminal, first_set in self.first.items():
                f.write(f'<tr><td>{non_terminal}</td><td>{", ".join(first_set)}</td></tr>\n')
            f.write('</table>\n')

            f.write('<h1>Follow Sets</h1>\n')
            f.write('<table>\n')
            for non_terminal, follow_set in self.follow.items():
                f.write(f'<tr><td>{non_terminal}</td><td>{", ".join(follow_set)}</td></tr>\n')
            f.write('</table>\n')

            f.write('<h1>LL(1) Parsing Table</h1>\n')
            terminals = ['id', '+', '*', '(', ')', '$']
            f.write('<table>\n')
            f.write('<tr><th></th>')
            for terminal in terminals:
                f.write(f'<th>{terminal}</th>')
            f.write('</tr>\n')

            non_terminals = ['E', "E'", 'T', "T'", 'F']
            for non_terminal in non_terminals:
                f.write(f'<tr><th>{non_terminal}</th>')
                for terminal in terminals:
                    production = self.parse_table.get((non_terminal, terminal), [])
                    if production:
                        production_str = ' '.join(production)
                    else:
                        production_str = ''
                    f.write(f'<td>{production_str}</td>')
                f.write('</tr>\n')
            f.write('</table>\n')

            f.write('</body></html>\n')

def main():
    parser = LL1Parser()
    input_string = input("Ingrese una cadena de entrada: ").strip()
    tokens = input_string.split()

    if tokens[-1] != '$':
        tokens.append('$')

    if parser.parse(tokens):
        print("Cadena válida.")
    else:
        print("Cadena no válida.")

    parser.save_to_html('ll1_table.html')
    print("Tablas de First, Follow y la tabla LL1 se han guardado en 'll1_table.html'.")

if __name__ == "__main__":
    main()


