aluno = {}

aluno["nome"] = input("Informe seu nome: ")
aluno["nota1"] = int(input("Informe sua nota: "))
aluno["nota2"] = int(input("Informe a sua segunda nota: "))
aluno["media"] = (aluno["nota1"] + aluno["nota2"])/2

print(aluno)

print("Teste para verificar se o nome Cassiano está no dicionario: ")
print("Cassiano" in aluno)
