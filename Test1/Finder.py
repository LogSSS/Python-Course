def Task1(input_text):
    return len([word for word in input_text.split() if word.startswith('a') or word.startswith('A')])
