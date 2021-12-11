# data-projects
#  O CDBot 

O CDBot é um projeto (original) de robô para web que foi desenvolvido para facilitar a compreensão e o acompanhamento de proposições, leis e políticas brasileiras, suas apresentações, alterações e tramitações no Congresso Nacional.



#### **- Descrição do Projeto**

Da forma como foi codificado, o robô atuará como web scraper ou crawler e foi pensado especificamente para realizar ações de engenharia de dados a partir da [API RESTful](https://dadosabertos.camara.leg.br/swagger/api.html) integrada ao site [Dados Abertos](https://dadosabertos.camara.leg.br/) da Câmara dos Deputados.

O CDBot é resultado dos estudos realizados proposto através da plataforma de ensino à distância [Alura](https://www.alura.com.br/), cujo objetivo é avaliar habilidades técnicas de extração, transformação e carregamento de dados abertos que possam ser úteis a processos de análise e tomada de decisão por diferentes empresas, associações e setores.



#### **- Operações do Projeto**

A principal operação atribuída ao CDBot é a de atuar como agente auxiliar na conferência de downloads de arquivos das proposições publicadas no site [Dados Abertos](https://dadosabertos.camara.leg.br/), bem como automâto de ações repetitivas. Neste sentido, busca-se contribuir para o aperfeiçoamento e eficácia das atividades de engenharia de dados aprendidas na [Alura](https://www.alura.com.br/).

Para tornar possíveis tais operações, o código de conferência do CDBot foi desenvolvido em três etapas:

1. Automação do acesso e preenchimento de dados (parâmetros) na [API](https://dadosabertos.camara.leg.br/swagger/api.html) do site [Dados Abertos](https://dadosabertos.camara.leg.br/), com uso do framework [Selenium](https://www.selenium.dev/);
2. Extração e transformação de dados a partir das bibliotecas [urllib](https://docs.python.org/3/library/urllib.html), [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) e [pandas](https://pandas.pydata.org/);
3. Conferência do código MD5 dos arquivos armazenados a partir dos comandos e funções da biblioteca [Hashlib](https://docs.python.org/3/library/hashlib.html).

Em todo o processo de codificação e execução do script do CDBot, foi utilizada a linguagem Python por meio do [Jupyter Notebook](https://jupyter.org/). É possível verificar o desenvolvimento do código acessando os arquivos .ipynb, e a licensa atribuída ao robô, no repositório deste projeto.



#### **- Desenvolvimento do Bot**

No decorrer de uma semana, algumas dúvidas e dificuldades se somaram ao desenvolvimento do projeto, em particular, devido ao desconhecimento de técnicas de engenharia e bibliotecas úteis à prática do web scraping. A princípio, entendia-se que seria possível realizar toda a automação do acesso ao site [Dados Abertos](https://dadosabertos.camara.leg.br/) e às proposições tramitadas nos últimos três dias utilizando a biblioteca Requests e Beautiful Soup. Entretanto, aquelas bibliotecas se mostraram insuficientes frente à ideia de emular um usuário, simular cliques de um mouse, digitar e preencher campos de entrada de dados / texto.

Para solucionar o problema, foi utilizada a [Selenium](https://www.selenium.dev/), biblioteca destinada à automação de testes e que é útil para simular a digitação humana. Basicamente, foram utilizados os comandos .click() e .send_keys() para acessar páginas web e caixas de texto que foram preenchidas com valores estabelecidos previamente. Primeiro, os valores correspondentes às siglas que compreendem as proposições em tramitação dos últimos 3 dias, quais sejam, PEC, PLP e PL, e as datas de início e término da busca desejada. Nesta versão do projeto, CDBot_Version_01, foram definidas as datas de 2021-09-21 e 2021-09-24 em conformidade com o formato requerido no formulário da API, AAAA-MM-DD. Os resultados iniciais deste processamento correspondem a 15 proposições das quais obteve-se o retorno de 15 projetos de lei. Não foram retornados resultados para PEC ou PLP.