"""
    Description:
    Cria um registro com cada evento que é executado
    dentro de um loop. Durante a execução desse loop
    a ideia foi mostrar alguns níveis de registros
    que podem ser criados no Python.
    O registro de cada evento é armazenado no arquivo
    app.log no diretório Saida/script06.

    Author:           @Thales
    Created:          2022-02-04
"""

import logging
from datetime import datetime
from pathlib import Path

def main():
    DIR_OUTPUT_LOG=Path("Saida/script06")
    Path(DIR_OUTPUT_LOG).mkdir(exist_ok=True, parents=True)
    logging.basicConfig(filename=f'{DIR_OUTPUT_LOG}/app.log', filemode='w', level=logging.DEBUG)

    lst_tarefas= [f"tarefa{tarefa}" for tarefa in range(1, 20)]
    for tarefa in lst_tarefas:
        now = datetime.now()
        if tarefa == "tarefa15":
            logging.error( f'{now} - erro ao executar a {tarefa}')
        if tarefa == "tarefa1":
            logging.warning( f'{now} algo inesperado na {tarefa}')
        else:
            logging.info( f'{now} - {tarefa} executada')

if __name__ == "__main__":
    main()
