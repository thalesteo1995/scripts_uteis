# Objetivo
O objetivo deste projeto é disponibilizar scripts
em *python* que são úteis para quem está começando
a trabalhar com essa linguagem de programação.

**Observação**: em python a utilização de ambiente virtual é
bastante útil para evitar conflitos de versões de bibliotecas.
Portanto, aqui também estarei utilizando desse artifício.

Para criar um ambiente virtual (.venv) digite:
`python3 -m venv .venv`
Isso irá criar o diretório .venv

Se estiver utilizando o Linux ou MacOs, ative o ambiente criado(.venv), executando:
`source .venv/bin/activate`

No Windows, basta digitar:
`.venv/Scripts/Activate`

Após ativar o .venv podemos começar a instalar as bibliotecas que serão utilizadas.
***Estarei Gerenciando os Pacotes da minha Aplicação utilizando o pip***

Na documentação https://docs.python.org/pt-br/3/tutorial/venv.html
é possível encontrar maiores detalhes sobre a utilização de Ambiente Virtual.

## script01
Nesse script é mostrado como utilizar uma barra de progesso
para que você consiga acompanhar a execução de seu script.
Após ativar o ambiente virtual, instale a lib **tqdm**.
`pip install tqdm`
