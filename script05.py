"""
    Description:

    Realiza o plot do Perfil Vertical de Temperatura
    considerando uma longitude fixa.

    Author:           @Thales
    Created:          2022-01-22
"""

import numpy as np
import matplotlib.pyplot as plt
import xarray as xr


def main():

    print("=" * 25)
    print("PLOT DE PERFIL VERTICAL")
    print("=" * 25)

    nc = xr.open_dataset("Entrada/temperatura.nc")['t'] - 273.15
    nc = nc.sel(longitude=300.0)
    nc = nc.sel(latitude=slice(-30.0, -40.0))
    nc = nc.isel(time=0)
    lat, lev = np.meshgrid(nc["latitude"], nc["level"])
    fig, ax = plt.subplots()
    ax.invert_yaxis()
    plt.contourf(lat, lev, nc, cmap='rainbow')
    plt.title('Perfil Vertical Temperatura do Ar (°C)')
    plt.ylabel('Níveis de pressão (hPa)')
    plt.xlabel('Latitude')
    plt.colorbar(ax=ax, shrink=.98)
    plt.savefig("Saida/script05/perfil_vertial.png")

if __name__ == "__main__":
    main()
