"""
    Description:

    - Construindo um dataframe com pandas;
    - Salvando dataframe em um arquivo txt.

    Author:           @Thales
    Created:          2022-01-15
"""

from pandas import DataFrame
from pathlib import Path

def main():
    DIR_OUTPUT = Path("Saida/usuarios")
    Path(DIR_OUTPUT).mkdir(exist_ok=True, parents=True)

    lst_users = [("user01", "user01@mail.com"), ("user02", "user02@mail.com"),
                 ("user03", "user03@mail.com"), ("user04", "user04@mail.com"),
                 ("user05", "user05@mail.com"), ("user06", "user06@mail.com")]

    print("-" * 40)
    print(" == Iniciando criação de Dataframe == ")
    print("-" * 40)

    df_users = DataFrame({})
    for user in lst_users:
        d = {'users': [user[0]], 'email': [user[1]]}
        df = DataFrame(data=d)
        df_users = df_users.append(df, ignore_index=True)

    print(df_users)
    filename_output = DIR_OUTPUT / "usuarios.txt"
    df_users.to_csv(filename_output, index=False, sep=';')

    print("-" * 40)
    print(" == Script finalizado com Sucesso!!! == ")
    print("-" * 40)

if __name__ == "__main__":
    main()