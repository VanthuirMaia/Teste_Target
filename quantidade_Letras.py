# Quantidade de Letras A

texto = input("Digite um texto: ") # Solicita ao usuário a entrada do texto

quantidade_a = texto.lower().count('a') # Verifica a existência da letra "a" na string e conta a quantidade dela, a função lower, converte todas as letras em minúscua pra poder contar, e não precisar distinguir quem é maiúscula ou minúscula.

if quantidade_a > 0:
    print(f"A letra 'A' aparece {quantidade_a} vezes no texto.")
else:
    print("A letra 'A' não aparece no texto")