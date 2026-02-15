#Crie um programa que traduza termos usados nodesenvolvimento web e mobile (ex.: Framework, Commit, etc.).

dicionario = {
    "frontend" : "Tudo que o utilizador vê e interage. Botões, cores, animações, layout. A camada visual e sensorial.",
    "backend" : "O que acontece por trás. Lógica, base de dados, autenticação, regras do sistema.",
    "token" : "Uma chave de acesso temporária usada na autenticação.",
    "deploy" : "O ato de colocar a app no ar.",
    "microserviços" : "Várias pequenas aplicações independentes que formam um sistema maior."
}

while True:
    palavra = input("Insira um termo tech para saber o significado: ").strip().lower()

    if palavra in dicionario:
        print(f"{palavra}: {dicionario[palavra]}")
    else:
        print("Termo não encontrado!!!")
        add = input("Queres adicionar este termo ao dicionário? [s/n] ").lower()
        if add == "s":
            significado = input("Insira o significado: ").strip().lower()
            dicionario[palavra] = significado
            print(f"Siginificado do termo {palavra} inserido com sucesso!")

    sair = input("Queres sair ou continuar a pesquisar? [s/c]").lower()

    if sair == "s":
        break
