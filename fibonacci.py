# Fibonacci

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

def main():
    try:
        numero = int(input("Informe um número para verificar se pertence a sequência Fibonacci: "))

        if fibonacci(numero):
            print(f"O número {numero} pertence a sequência de Fibonacci.")
        else:
            print(f"O número {numero} NÃO pertence a sequência de Finonacci")
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()