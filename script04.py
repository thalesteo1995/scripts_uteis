"""
    Description:
    Realiza a contagem do tempo de execução de um
    trecho do código.

    Author:           @Thales
    Created:          2022-01-15
"""

import time

def main():
    start = time.time()
    function()
    end = time.time()
    print(f"Tempo de Execução da Função: {end - start} s")

def function():
    for x in range(1, 100000):
        y = x + 1
        result = x**2 + y**2
        print(f"O resultado é: {result}")

if __name__ == "__main__":
    main()