#instalação da biblioteca
!pip install pdfplumber

#importação das bibliotecas utilizadas
import re
import pdfplumber
import pandas as pd
from collections import namedtuple

#determinação do cabeçalho da tabela que será lida
line = namedtuple('line', '___')#'títulos das colunas que o scrip irá reconhecer no pdf com mesma formatação e separados por espaço, ex.: 'Nome Idade Cidade'
#determinação do formato de dado a ser lido
line_re = re.compile(r'(___)')#utilizando regular expression configura a linha que o scrip irá ler, ex.: Se é numérico: [0-9]

#importação do arquivo a ser lido
file = '___' #nome do arquivo com formato, se o arquivo estiver fora da pasta do projeto deverá se colocar o nome com caminho do arquivo ex.: 'C:\Usuario\Desktop\arquivo.pdf'

#leitura do arquivo pdf
lines_df = [] #lista que irá receber os dados lidos
c = 0 #contador

with pdfplumber.open(file) as pdf: #comando para biblioteca ler o arquivo na variável 'file'
    pages = pdf.pages
    for page in pdf.pages: #comando para a biblioteca ler cada uma das páginas do arquivo
        text = page.extract_text() #comando para extrair o conteúdo da página
        c += 1 #incremento do contador para cada página lida
        for line in text.split('\n'): #separação do conteúdo lido por linhas
            if line_re.search(line): #comando para identificação da linha configurada
                itens = line.split() #separação do conteúdo por espaço
                lines_df.append(*itens) #comando que adiciona os itens a lista de dados

#criação do dataframe
df = pd.DataFrame(lines_df)

#visualização dos dados lidos do arquivo pdf
df.head()

#aqui pode ser feito vários exercícios de tratamento e correção de dados lidos

#Salvar no formato csv os dados lidos para ser acessado posteriormente de forma acessível ao pandas
df.to_csv('___', sep=';', index=False, line_terminator='\r\n',encoding='utf-8') #inserir o nome do arquivo a ser criado
