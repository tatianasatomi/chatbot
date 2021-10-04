def cumprimento(nome): #parâmetro
    print(f"Bom dia, {nome}!")

nome = input("Qual o seu nome? ")
cumprimento(nome) #argumento

como = input(f"Tudo bem, {nome}? ").lower()
respostas = {"bem": "Que bom!", "mais ou menos": "Quer conversar sobre isso?", "mal": "Pouxa, o que aconteceu?", "bem mal": "Nossa, o que aconteceu? Quer conversar sobre isso?"}



if "bem mal" in como:
    print(respostas["bem mal"])
else:
    for resp in respostas: #itera dentro do valor, por isso ignora filtros anteriores
        if "bem mal" not in resp:

            if resp in como:
                print(respostas[resp])    

