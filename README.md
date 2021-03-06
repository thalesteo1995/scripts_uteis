# Objetivo
O objetivo deste projeto é disponibilizar scripts
em *python* que são úteis para quem está começando
a trabalhar com essa linguagem de programação.
Os scripts compartilhados no repositório serão
focados para manipulação e análise de
dados, principalmente meteorológicos.

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

## script02
O script02.py realiza o Download de arquivos de chuva do tipo .grib
do ftp do CPTEC. Para executar essa tarefa é utilizado aqui
a biblioteca requests.
Portanto, caso ainda não tenha instalado esse pacote em seu
ambiente de trabalho (.venv), faça a sua instalação:
`pip install requests`.

**Desafio**: um desafio interessante é reescrever esse código de modo
a deixá-lo genérico para baixar os arquivos diários de vários meses.
- Dica: faça um loop aninhado, de tal modo que durante cada iteração
a variável **url_file*** seja montada a partir do mês, dia e ano. No
script02.py o mês e ano estão fixos na url.
## script03
No script03.py é construído um dataframe a partir de
uma lista de tuplas. Em seguida, o dataframe gerado é salvo em
um arquivo txt.
## script04
Calcula o tempo de execução de um trecho do código.
## script05
Realiza o plot de uma seção transversal vertical da temperatura do ar.
A figura gerada é salva em: Saida/script05
***OBS***: Dependendo do arquivo de input o nome das dimensões
(time, latitude, longitude, level) e da variável (t) vão se alterar.
## script06
Realiza o registro (log) dos eventos que foram executados dentro do script.
O registro desses eventos são armazenados no arquivo app.log do
diretório Saida/script06. A utlização de log é importante pois ajuda
a identifcar processos que falharam dentro do código.
No script06.py são criados três tipos de registros: error, warning e info.
Uma descrição detalhada desses registros podem ser obtidos em:
https://rollbar.com/blog/logging-in-python/

## script07
Aplica o teste de Mann Kendall em uma série temporal.
Essa série temporal é extraída de um arquivo NetcDf(NC)
para um ponto de grade específico. O arquivo NC encontra-se
no diretório Entrada e está nomeado como **precip.mon.mean.nc**.