import modulo
from classe import Teste

print(modulo.x, modulo.y, modulo.z)

modulo.funcao()

modulo.teste("15º C")

algo = input("Digite algo: ")
algo_mais = input("Digite mais alguma coisa: ")
modulo.teste1(algo, algo_mais)

modulo.teste1(29.9, 16.45)

modulo.teste2(1, 2, 3, 4)


classe_teste = Teste("Tchau")
print(classe_teste.var, classe_teste.var1)

classe_teste.funcao_classe()

nome = input("Qual o seu nome? ")
classe_teste.cafe(nome)

x, y = "Ale", 26
classe_teste.forms(y, x)