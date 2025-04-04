import pandas as pd

def aluno_aprovado(nome, media, legenda):
    caminho = "/Users/leonardo/Documents/eng_computacao/programacao2/atividade_3/aprovados.xlsx"
    novo = pd.DataFrame([{"Nome": nome, "Média": media, "Legenda": legenda}])
    
    try:
        df = pd.read_excel(caminho)
        df = pd.concat([df, novo], ignore_index=True)
    except FileNotFoundError:
        df = novo

    df.to_excel(caminho, index=False)

def aluno_reprovado(nome, media, legenda):
    caminho = "/Users/leonardo/Documents/eng_computacao/programacao2/atividade_3/reprovados.xlsx"
    novo = pd.DataFrame([{"Nome": nome, "Média": media, "Legenda": legenda}])

    try:
        df = pd.read_excel(caminho)
        df = pd.concat([df, novo], ignore_index=True)
    except FileNotFoundError:
        df = novo

    df.to_excel(caminho, index=False)

def aluno_exame(nome, media):
    caminho = "/Users/leonardo/Documents/eng_computacao/programacao2/atividade_3/exame.xlsx"
    novo = pd.DataFrame([{"Nome": nome, "Média": media}])

    try:
        df = pd.read_excel(caminho)
        df = pd.concat([df, novo], ignore_index=True)
    except FileNotFoundError:
        df = novo

    df.to_excel(caminho, index=False)

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

            caminho_geral = "/Users/leonardo/Documents/eng_computacao/programacao2/atividade_3/notas.xlsx"
            nova_nota = pd.DataFrame([{"Nome": nome, "Nota 1": nota1, "Nota 2": nota2, "Nota 3": nota3, "Média": media}])

            try:
                df = pd.read_excel(caminho_geral)
                df = pd.concat([df, nova_nota], ignore_index=True)
            except FileNotFoundError:
                df = nova_nota

            df.to_excel(caminho_geral, index=False)

            # Classifica o aluno
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