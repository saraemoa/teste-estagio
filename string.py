def verificar_String(string):
    contagem = string.lower().count('a')

    if contagem > 1:
        print(f"A letra 'a' aparece {contagem} vezes na string.")
    elif contagem == 1:
        print(f"A letra 'a' aparece {contagem} vez na string.")
    else:
        print("A letra 'a' não aparece na string.")

texto = str(input("Informe uma frase: "))
verificar_String(texto)
