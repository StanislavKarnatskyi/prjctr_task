with open('lowercase_text.txt', 'r') as lowercase_text, open('uppercase_text.txt', 'w') as uppercase_text:
    text = lowercase_text.read()
    uppercase_text.write(text.upper())

print(uppercase_text)