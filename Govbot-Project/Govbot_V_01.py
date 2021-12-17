# PROJETO Govbot

# PARTE 1
# Operações Básicas

import pandas as pd
govbot = pd.read_csv ('govbot_v_01.csv', sep=',', encoding='utf-8')

print(govbot)

govbot.info()

govbot.head()

govbot.sort_values(by='INÍCIO', ascending=True)

govbot['PAÍS'].value_counts()

govbot['PAÍS'].value_counts(normalize=True)

# PARTE 2
# Operações com Gráficos

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

govbot['PAÍS'].value_counts().plot.bar(title='Percentual de chatbots por governo / país')

govbot['PAÍS'].value_counts().plot.bar()
plt.title('Percentual de chatbots por governo / país',fontsize=14,color='black')
plt.xlabel('Países avaliados',fontsize=10,color='green')
plt.ylabel('Níveis de adesão à tecnologia chatbot',fontsize=10,color='green')
plt.rcParams ['xtick.labelsize'] = 14
plt.rcParams ['ytick.labelsize'] = 14

govbot.boxplot(column='INÍCIO', color='blue')
plt.rcParams ['xtick.labelsize'] = 10
plt.rcParams ['ytick.labelsize'] = 10
plt.show()

sns.catplot(x="INÍCIO",kind='box',data=govbot,color='blue')
plt.title("Concentração de chatbots por ano de início de atividade")
plt.xlabel('INÍCIO')
plt.ylabel('ATIVIDADE')
plt.show()

sns.catplot(x="NÍVEL",data=govbot)
plt.title('Concentração de chatbots por nível de governo',fontsize=14,color='black')
plt.show()

sns.displot(govbot['PÚBLICO'],bins= 30,color='blue')
plt.title('Atendimento por tipo de público',fontsize=14,color='black')
plt.show()

sns.stripplot(data=govbot, x='SETOR',y='PAÍS')
plt.title('Países e concentração de chatbots governamentais por setor',fontsize=14,color='black')
plt.show()

# Conclusão