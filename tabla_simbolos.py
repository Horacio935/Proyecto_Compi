# tabla_simbolos.py
class HashTable:
    def __init__(self, size=1000):
        self.size = size
        self.table = [None] * size
        self.counter = 0

    def hash_function(self, key):
        bucket = self.counter % self.size
        self.counter += 1
        return bucket

    def add_element(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, existing_value) in enumerate(self.table[index]):
                if existing_key == key:
                    self.table[index][i] = (key, value)  # Actualizar el valor si la clave ya existe
                    break
            else:
                self.table[index].append((key, value))  # Agregar el nuevo elemento

    def get_value(self, key):
        for bucket in self.table:
            if bucket is not None:
                for existing_key, existing_value in bucket:
                    if existing_key == key:
                        return existing_value
        raise KeyError(f"Key '{key}' not found in hash table")

    def __repr__(self):
        return repr(self.table)

# Crear una instancia global de la tabla de símbolos
tabla_simbolos = HashTable(size=1000)