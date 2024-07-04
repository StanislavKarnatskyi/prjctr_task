def from_lower_to_upper():
    with open('lowercase_text.txt', 'r') as lowercase_text, open('uppercase_text.txt', 'w') as uppercase_text:
        lower_text = lowercase_text.read()
        uppercase_text.write(lower_text.upper())
