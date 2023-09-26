def contains_on(word):
    if "on" in word:
        return True
    else:
        return False

# Ejemplo de uso
word1 = "dragon"
word2 = "python"
print(f"La palabra '{word1}' contiene 'on': {contains_on(word1)}")
print(f"La palabra '{word2}' contiene 'on': {contains_on(word2)}")
