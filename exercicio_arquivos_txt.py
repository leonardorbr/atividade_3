def aluno_aprovado(nome, media, legenda):
    with open("/Users/leonardo/Documents/eng_computacao/programacao2/atividade_3/aprovados.txt", "a") as aprovados:
        aprovados.write(f"Nome do aluno: {nome}\nMedia: {media:.2f}\nLegenda: {legenda}\n\n")

def aluno_reprovado(nome, media, legenda):
    with open("/Users/leonardo/Documents/eng_computacao/programacao2/atividade_3/reprovados.txt", "a") as reprovados:
        reprovados.write(f"Nome do aluno: {nome}\nMedia: {media:.2f}\nLegenda: {legenda}\n\n")

def aluno_exame(nome, media):
    with open("/Users/leonardo/Documents/eng_computacao/programacao2/atividade_3/exame.txt", "a") as exame:
        exame.write(f"Nome do aluno: {nome}\nMedia: {media:.2f}\n\n")
    
    nota_exame = float(input("Digite a nota do exame: "))
    nota_final = (media + nota_exame) / 2

    if nota_final >= 5:
        legenda = "Aprovado após exame"
        aluno_aprovado(nome, nota_final, legenda)
    else:
        legenda = "Reprovado após exame"
        aluno_reprovado(nome, nota_final, legenda)

# Loop principal
while True:
    try:
        cadastrar = input("Deseja cadastrar mais um aluno? S/N \n")

        if cadastrar.lower() == "s":
            nome = input("Digite o nome do aluno: ")
            nota1 = float(input("Digite a nota 1: "))
            nota2 = float(input("Digite a nota 2: "))
            nota3 = float(input("Digite a nota 3: "))

            media = (nota1 + nota2 + nota3) / 3

            # Salva as notas no arquivo geral
            with open("/Users/leonardo/Documents/eng_computacao/programacao2/atividade_3/notas.txt", "a") as arquivo:
                arquivo.write(f"{nome},{nota1},{nota2},{nota3}\n")

            # Classifica o aluno e grava no arquivo correspondente
            if media >= 7:
                legenda = "Aprovado direto"
                aluno_aprovado(nome, media, legenda)
            elif media >= 5:
                aluno_exame(nome, media)
            else:
                legenda = "Reprovado direto"
                aluno_reprovado(nome, media, legenda)

        elif cadastrar.lower() == "n":
            print("Muito obrigado. Volte sempre!")
            break
        else: 
            print("Digite 's' para cadastrar ou 'n' para encerrar o programa.")

    except Exception as e:
        print(f"Ops, deu o seguinte erro: {e}")