import re

patron = r"\b(break|default|func|interface|select|case|defer|go|map|struct|chan|else|goto|package|switch|const|fallthrough|if|range|type|continue|for|import|return|var)\b"

# verificar si una palabra es una keyword
def es_palabra_clave(palabra):
    coincidencia = re.search(patron, palabra)

    # Si hay una coincidencia, devuelve True. De lo contrario, devuelve False.
    return bool(coincidencia)


palabra = input("ingresa palabra a verificar: ")

# Llama a la función y guarda el resultado
resultado = es_palabra_clave(palabra)

# Imprime el resultado
if resultado:
    print(f"La palabra '{palabra}' es una palabra clave de Golang.")
else:
    print(f"La palabra '{palabra}' no es una palabra clave de Golang.")
