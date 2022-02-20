"""
    Description:
    - Realiza a leitura de um arquivo NetcDf;
    - Extrai a série temporal completa para um
    ponto de grade específico do arquivo;
    - Aplica o teste de Mann Kendall na série;
    - Imprime na tela o resultado do teste.

    Observação: nesse script também criei uma função
    (convert_dimension_lon) para converter a dimensão
    de longitude de 0° a 360° para -180° a 180°
    do arquivo aberto.

    Author:           @Thales
    Created:          2022-02-20
"""

import xarray as xr
import pymannkendall as mk

def main():

    file_input = 'Entrada/precip.mon.mean.nc'
    nc = xr.open_dataset(file_input)["precip"]
    nc = convert_dimension_lon(nc, "lon")
    nc = nc.sel(lat=-23.5, lon=-46.6, method="nearest")
    lst_prec_med_mensal = list(nc.data)

    alpha = 0.05
    trend_mk = mk.original_test(lst_prec_med_mensal, alpha=alpha)
    result_trend = trend_mk.trend

    print(f"Trend: **{result_trend}**")

    if trend_mk.p < alpha:
        print("Significant evidence of trend in the data")

    elif trend_mk.p >= alpha:
        print("No significant evidence of trend in the data")


def convert_dimension_lon(dataset_input: object, name_dimension_lon_dataset: str):
    """Realiza a transformação da dimensão de longitude
    de um dataset de 0° a 360° para -180° a 180°

    Args:
        dataset_input (object): dataset aberto
        name_dimension_lon_dataset (str): nome da dimsensao de
        longitude do arquivo aberto

    Returns:
        Dataset com as dimensões de longitude convertidas para -180° a 180°
    """
    dataset_input[name_dimension_lon_dataset] = (
        (dataset_input[name_dimension_lon_dataset] + 180.0) % 360.0
        ) - 180.0
    dataset_output = dataset_input.sortby(dataset_input[name_dimension_lon_dataset])
    return dataset_output


if __name__ == "__main__":
    main()
