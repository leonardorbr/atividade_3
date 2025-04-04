O código original utilizava a função open() para criar e escrever arquivos .txt com os dados dos alunos e a situação do aluno. 

Na nova versão, os arquivos .txt foram substituídos por planilhas .xlsx, utilizando a biblioteca pandas.

Principais alterações:
- Uso da biblioteca pandas: Substituímos o open() por pandas.read_excel() e pandas.to_excel() para ler e salvar os dados em planilhas Excel.
- Criação de DataFrame para cada aluno: Ao invés de escrever texto direto no arquivo, os dados do aluno são inseridos em um DataFrame, que é uma tabela.
- Concatenação com dados existentes: Quando o arquivo .xlsx já existe, ele é lido com pandas.read_excel() e o novo aluno é adicionado com pd.concat().
- Tratamento com try/except: Como o arquivo .xlsx pode ainda não existir, utilizamos um bloco try/except com FileNotFoundError para criar o arquivo do zero na primeira execução, evitando erros.
