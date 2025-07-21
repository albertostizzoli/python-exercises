# LE REGEX IN PYTHON

# 1): Scrivere una regex per trovare tutte le occorrenze di "cat" in una stringa.

import re

text = "The cat chased the other cat."
matches = re.findall(r'cat', text)
print(matches)

# 2): Scrivere una regex per verificare se una stringa contiene solo lettere maiuscole.

import re

text = "HELLO"
is_upper = bool(re.fullmatch(r'[A-Z]+', text))
print(is_upper)

# 3): Scrivere una regex per dividere una stringa in base agli spazi.

import re

text = "Split this string by spaces"
parts = re.split(r'\s+', text)
print(parts)

# 4): Scrivere una regex che estrae i numeri da una stringa.

import re

text = "There are 12 apples and 30 oranges"
numbers = re.findall(r'\d+', text)
print(numbers)

# 5): Scrivere una regex per trovare tutti i punti esclamativi in una stringa.

import re

text = "Wow! I can't believe it! It really works!"
exclamations = re.findall(r'!', text)
print(exclamations)

# 6): Scrivere una regex per validare un indirizzo email.

import re

email = "example@domain.com"
is_valid = bool(re.fullmatch(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', email))
print(is_valid)

# 7): Scrivere una regex che verifica se una stringa è un URL valido.

import re

url = "https://www.example.com"
is_url = bool(re.fullmatch(r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', url))
print(is_url)

# 8): Scrivere una regex che identifica le date nel formato "gg/mm/aaaa".

import re

text = "Today's date is 15/07/2024."
dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
print(dates)

# 9): Scrivere una regex per rimuovere tutti i tag HTML da una stringa.

import re

html = "<html><head><title>Title</title></head><body>Content</body></html>"
clean_text = re.sub(r'<[^>]+>', '', html)
print(clean_text)

# 10): Scrivere una regex per verificare se una stringa è un numero esadecimale valido.

import re

hex_number = "1A3F"
is_hex = bool(re.fullmatch(r'\b[0-9A-F]+\b', hex_number))
print(is_hex)

# 11): Scrivere una regex che estrae le parole che iniziano e finiscono con una vocale.

import re

text = "Argentina is an area where apricots grow."
words = re.findall(r'\b[aeiouAEIOU][a-z]*[aeiouAEIOU]\b', text)
print(words)

# 12): Scrivere una regex che cattura i numeri di telefono nel formato internazionale (+39 0123 456789).

import re

text = "My phone number is +39 0123 456789."
phones = re.findall(r'\+\d{2} \d{4} \d{6}', text)
print(phones)

# 13): Scrivere una regex che identifica le frasi che contengono almeno tre parole in maiuscolo.

import re

text = "This is a TEST string with CAPITAL words and SOME more."
sentences = re.findall(r'\b(?:[A-Z][a-z]*\s){2,}[A-Z][a-z]*\b', text)
print(sentences)

# 14): Scrivere una regex che verifica se una stringa contiene un indirizzo IPv4 valido.

import re

ip = "192.168.1.1"
is_valid_ip = bool(re.fullmatch(r'(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)', ip))
print(is_valid_ip)

# Scrivere una regex che verifica la presenza di parole con caratteri ripetuti consecutivamente (es. "letter" o "balloon").

import re

text = "This room seems too quiet and still."
repeated_chars = re.findall(r'\b\w*([a-zA-Z])\1\w*\b', text)
print(repeated_chars)