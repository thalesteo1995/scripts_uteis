"""
    Description:

    Download de arquivos utilizando a biblioteca requests.

    - Baixa um conjunto de arquivos de chuva diária do produto
    MERGE do CPTEC (http://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/DAILY/);
    - Aqui o script foi escrito para realizar o Download dos
    dados diários (.grib2) do mês de Dezembro de 2021;
    - Os dados baixados serão salvos no diretório: Saida/MERGE

    Author:           @Thales
    Created:          2022-01-15
"""

import requests
from pathlib import Path


def main():
    DIR_MERGE = Path("Saida/MERGE")
    Path(DIR_MERGE).mkdir(exist_ok=True, parents=True)

    for dia in range(1, 32):
        dia = (str(dia)).zfill(2)
        url_file = f"http://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/DAILY/2021/12/MERGE_CPTEC_202112{dia}.grib2"
        filename = f"MERGE_CPTEC_{2021}{12}{dia}.grib2"

        r = requests.get(url_file)
        f = open(DIR_MERGE/filename, 'wb')
        if r.status_code == 200:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
            f.close()

        print(f"Baixado arquivo **{filename}**")

if __name__ == "__main__":
    main()