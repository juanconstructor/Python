import re
from collections import Counter

def analyze_text(text):
    # Eliminar espacios en blanco al inicio y al final del texto
    text = text.strip()

    # Dividir el texto en palabras
    words = re.findall(r'\w+', text.lower())

    # Contar el número de palabras
    num_words = len(words)

    # Contar la frecuencia de cada palabra
    word_freq = Counter(words)

    # Contar el número de caracteres
    num_chars = len(text)

    return num_words, word_freq, num_chars

text = input("Ingresa el texto a analizar: ")
num_words, word_freq, num_chars = analyze_text(text)

print("Número de palabras:", num_words)
print("Frecuencia de palabras:", word_freq)
print("Número de caracteres:", num_chars)