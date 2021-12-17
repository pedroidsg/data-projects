# data-projects
#  O Govbot 

O Govbot é um projeto (original) de análise de dados cujo objetivo é apresentar a adoção de agentes de inteligência artificial (IA) pelo setor público e terceiro setor de diferentes instâncias governamentais e países, em particular chatbots destinados ao atendimento público (e-services) e participação política (e-participation) de pessoas cidadãs. 

Neste documento, apresento a fonte de dados que propiciou o projeto, o diretório desenvolvido pela [Chatbots Organization](https://chatbots.org/directory), a descrição do que é a organização e por qual razão é uma fonte de dados de qualidade. Além disso, detalho os objetivos, métodos propostos e resultados iniciais das análises obtidas por meio do Govbot-Project.



#### **- Diretório de Chatbots**

A Chatbots Organization foi fundada em 2008, como um diretório de chatbots que abrangeria serviços de listagem de empresas do setor, notícias sobre IA e outros serviços. Hoje, a organização se descreve como um recurso de comparação confiável para compradores, análise verificada de usuários e pesquisa sobre plataformas e soluções de chatbot e aplicativos de comunicação empresarial.

Em seu site, há uma área do diretório denominada "Temas do Consumidor" onde é possível selecionar e filtrar dados. A partir dessa funcionalidade, definem-se os tipos de chatbots que interessam ao usuário do diretório. 

Neste sentido, o diretório da organização cuja alimentação se deu pelos(as) profissionais de sua comunidade com 25.439 membros e 749 empresas / desenvolvedores(as) de mercados distintos mostrou-se capaz de fornecer os dados qualitativos adequados acerca do cenário governamental (global) de desenvolvimento dessas tecnologias. 

 

#### **- Descrição do Projeto**

Para iniciar o projeto e antes de realizar ações de análise de dados, foi necessário observar que, na área "Temas do Consumidor" há diversas temáticas, entre as quais se observam o tópico "Governo" e seus subtópicos: serviços governamentais, eleições, serviço militar, impostos, pensões etc.

Através da lista [Chatbots de Governo](https://chatbots.org/industry/government/) implementada no site da organização, delimitou-se o que poderia ser utilizado como categorias e variáveis. A lista foi o principal facilitador da pesquisa, porque o design da interface de navegação permitiu a visualização objetiva de todos os tópicos que viriam a formar o banco de dados do projeto.



#### **- Objetivos e Métodos**

A definição dos objetivos e métodos de análise do Govbot-Project compreenderam explorar o campo governamental, sob a perspectiva descritiva da Análise Exploratória de Dados ou "Exploratory Data Analysis (EDA)", verificando o início das operações de cada um dos 72 chatbots listados, a distribuição e a concetração geográfica do mercado e outros atributos que serão mais bem detalhados a seguir.

Para executar tal análise, o código do Govbot foi desenvolvido em cinco etapas:

1. Definição, coleta e compilação dos dados disponíveis nas páginas e perfis de cada chatbot da lista [Chatbots de Governo](https://chatbots.org/industry/government/);
2. Tabulação dos dados obtidos em arquivo .csv;
3. Importação de bibliotecas [pandas](https://pandas.pydata.org/), [matplotlib](https://matplotlib.org/) e [seaborn](https://seaborn.pydata.org/);
4. Exploração descritiva dos dados;
5. Visualização gráfica dos dados.

Durante o processo de codificação do script e execução da análise, foi utilizada a linguagem Python por meio de sua IDE e [Jupyter Notebook](https://jupyter.org/). No repositório deste projeto, é possível verificar o desenvolvimento do código acessando os arquivos .py e .ipynb e a licensa MIT atribuída.



#### **- Categorias e Variáveis**

A descrição da análise foi composta pela lista de atributos a seguir:

1. NOME: nomenclatura genérica;
2. INÍCIO: ano inicial da operação;
3. PAÍS: origem;
4. NÍVEL: municipal, regional, nacional e internacional;
5. SETOR: privado, público ou sem fins lucrativos;
6. PÚBLICO: específico ou todos os públicos;
7. OBJETIVO: e-services, e-participation ou eleitoral;
8. LÍNGUA: idioma oficial do chatbot;
9. DESENVOLVEDOR: público ou privado;
10. ORGANIZAÇÃO: privada, pública ou sem fins lucrativos;
11. ATIVO: sim ou não.



#### **- Resultados das Análises**

De acordo com os dados obtidos, no ano de 2012 houve amplo desenvolvimento de chatbots governamentais e a maior distribuição e / ou concentração geográfica desse desenvolvimento é observável na Polônia.

A maior parte das organizações é proveniente do setor público e, em oposição, o desenvolvimento dessas tecnologias é resultado do trabalho de desenvolvedores(as) de empresas privadas contratadas.

Obs.: O Govbot-Project é um desmembramento de pesquisa individual realizada no Centro de Estudos em Comunicação, Tecnologia e Política - [CTPol](http://ctpol.unb.br), da Universidade de Brasília - [UnB](https://www.unb.br). Somente uma parte dos dados já compilados foram agregados nesta análise, logo, não devem ser generalizados para qualquer fim.