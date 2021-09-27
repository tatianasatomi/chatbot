def cumprimento(nome):
    print(f"Bom dia, {nome}!")

nome = input("Qual o seu nome? ")
cumprimento(nome)

como = input(f"Tudo bem, {nome}? ").lower()
respostas = {"bem": "Que bom!", "mais ou menos": "Quer conversar sobre isso?", "mal": "Pouxa, o que aconteceu?", "bem mal": "Nossa, o que aconteceu? Quer conversar sobre isso?"}

for resp in respostas:
    if resp in como:
        if como == "bem mal" and como != "bem" and como != "mal":
            print(respostas["bem mal"])
            break
            
        else:
            print(respostas[resp])
            break
