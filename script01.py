"""
    Description:

    Utilizando a biblioteca tqdm para produzir uma barra
    de progresso que facilite acompanhar a execução do script.

    - Simularemos a execução de uma lista de tarefas;
    - A medida em que as tarefas forem executadas uma
    barra de progresso será mostrada no Terminal

    Author:           @Thales
    Created:          2022-01-15
"""

from tqdm import tqdm

def main():
    lst_tarefas = list(range(1, 101))

    barra_progresso = tqdm(total=len(lst_tarefas))
    for tarefa in lst_tarefas:
        print(f"Executando Tarefa {tarefa}")
        barra_progresso.update()
    barra_progresso.close()

if __name__ == "__main__":
    main()