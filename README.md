# Activity Suggestions

A partir do nome de uma cidade, sugere uma lista de atividades que podem ser feitas na condição meteorológica do momento. A condição meteorológica é obtida através da API disponibilizada no https://openweathermap.org/

## Como utilizar:

Use uma das formas abaixo para testar a aplicação.

### Live Demo:

Em breve

### Imagem no Docker Hub:

Em breve

### Executar em modo de desenvolvimento

####Pré requisitos

A aplicação utiliza um backend python/flask com frontend react

Para executá-la em modo de desenvolvimento, é necessário um ambiente linux com as seguintes aplicações instaladas:

```
python3.9
python3.9-venv
pip3
nodejs
npm
make
git
```

Também é necessário ter uma chave da API do OpenWeather. Você pode criar uma no endereço: https://home.openweathermap.org/

####Instalação de dependências

A instalação das demais dependências e do ambiente virtual é feita por um arquivo Makefile. Para obter o código fonte e fazer a configuração inicial execute:

```
git clone https://github.com/Marcelo-Ferraz-de-Oliveira/controle_aplicacoes_financeiras.git
cd controle-aplicacoes-financeiras
make install API_KEY=youropenweatherkey
```

####Uso

Para iniciar os servidores de desenvolvimento (portas 3000 e 5000) execute `make start`

Para interromper a execução dos servidores de desenvolvimento execute `make stop`

Para iniciar o ambiente virtual de desenvolvimento python execute `. venv/bin/activate`

Para rodar os testes automatizados (no ambiente virtual) execute `pytest --cov`
