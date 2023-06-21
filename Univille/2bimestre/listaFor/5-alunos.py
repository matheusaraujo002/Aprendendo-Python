turma = int(input("Digite o número de turmas: "))

somaMedia = 0
for contaTurma in range(turma):
    alunos = int(input(f"Digite o número de alunos que tem na turma {contaTurma+1}: "))
    soma = 0
    for contaAluno in range(alunos):
        nota = float(input(f"Digite a nota do aluno {contaAluno+1}: "))
        soma = soma + nota
    media = soma / alunos
    print(f"A média é {media}")
    somaMedia = somaMedia + media
mediaEscola = somaMedia / turma
print(f"A média da escola é {mediaEscola}")