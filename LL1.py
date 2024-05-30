import collections

epsilon = 'ε'

# Función para obtener los primeros de una gramática
def compute_firsts(grammar):
    firsts = collections.defaultdict(set)

    def first(symbol):
        if symbol not in grammar:  # Si es un terminal
            return {symbol}
        if not firsts[symbol]:  # Si no está calculado aún
            for production in grammar[symbol]:
                for token in production:
                    token_first = first(token)
                    firsts[symbol].update(token_first - {epsilon})
                    if epsilon not in token_first:
                        break
                else:
                    firsts[symbol].add(epsilon)
        return firsts[symbol]

    for non_terminal in grammar:
        first(non_terminal)
    return firsts

# Función para obtener los siguientes de una gramática
def compute_follows(grammar, firsts):
    follows = collections.defaultdict(set)
    start_symbol = next(iter(grammar))
    follows[start_symbol].add('$')

    while True:
        updated = False
        for head, productions in grammar.items():
            for production in productions:
                trailer = follows[head].copy()
                for symbol in reversed(production):
                    if symbol in grammar:
                        if follows[symbol].update(trailer):
                            updated = True
                        if epsilon in firsts[symbol]:
                            trailer.update(firsts[symbol] - {epsilon})
                        else:
                            trailer = firsts[symbol].copy()
                    else:
                        trailer = {symbol}
        if not updated:
            break

    return follows

# Función para construir la tabla LL1
def build_ll1_table(grammar, firsts, follows):
    table = collections.defaultdict(dict)

    for head, productions in grammar.items():
        for production in productions:
            first_of_production = set()
            for symbol in production:
                first_of_production.update(firsts[symbol])
                if epsilon not in firsts[symbol]:
                    break
            else:
                first_of_production.add(epsilon)
            for terminal in first_of_production - {epsilon}:
                table[head][terminal] = production
            if epsilon in first_of_production:
                for terminal in follows[head]:
                    table[head][terminal] = production
    return table

# Función principal
def main():
    grammar = collections.defaultdict(list)

    print("Ingrese las producciones (por ejemplo, E->T E'). Ingrese una línea vacía para terminar:")
    while True:
        production = input().strip()
        if not production:
            break
        head, bodies = production.split('->')
        head = head.strip()
        for body in bodies.split('|'):
            grammar[head].append(body.strip().split())

    firsts = compute_firsts(grammar)
    follows = compute_follows(grammar, firsts)
    ll1_table = build_ll1_table(grammar, firsts, follows)

    print("\nTabla de Primeros y Siguientes:")
    print(f"{'No Terminal':<12}{'Primero':<20}{'Siguiente'}")
    print('-' * 50)
    for non_terminal in grammar:
        first_set = firsts[non_terminal]
        follow_set = follows[non_terminal]
        print(f"{non_terminal:<12}{str(first_set):<20}{str(follow_set)}")

    print("\nTabla LL1:")
    for non_terminal, rules in ll1_table.items():
        for terminal, production in rules.items():
            print(f"M[{non_terminal}, {terminal}] = {production}")

if __name__ == "__main__":
    main()
