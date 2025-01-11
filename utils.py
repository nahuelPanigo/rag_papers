
import json
import unicodedata
import re


def read_json(filename):
    with open(filename) as f:
        data = json.load(f)
    return data


def remove_accents(text):
    # Normaliza el texto para descomponer los caracteres acentuados
    text = unicodedata.normalize('NFD', text)
    # Elimina los caracteres diacríticos (acentos)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    # Normaliza el texto nuevamente a la forma compuesta
    text = unicodedata.normalize('NFC', text)
    return text

def normalize_text(text):
    # Convertir a minúsculas
    text = text.lower()
    # Reemplazar saltos de línea y tabulaciones con espacios
    text = re.sub(r'[\n\t]', ' ', text)
    # Reemplazar múltiples espacios con un solo espacio
    text = re.sub(r'\s+', ' ', text).strip()
    text = remove_accents(text)
    return text