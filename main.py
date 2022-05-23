#Desenvolva uma aplicação que repita a inserção de dados 
#de alunos (nome, nota1, nota2 e nota3) até que o 
#usuário peça para parar a aplicação.
#As notas para serem consideradas válidas devem estar entre 0 e 10
#Apresente ao final:
#Qtd de alunos aprovados (média>=7)
#Qtd de alunos reprovados (média<4)
#Qtd de alunos de exame final (média >= 4 e media <7)

aprovados=0
exame=0
reprovados=0
genero=''

cadastrar = input('Deseja iniciar lançamentos (S/N)? ' )

while cadastrar.upper() !='S' and cadastrar.upper()!='N':

    cadastrar= input('Opção Inválida, informe (S/N): ')

while cadastrar.upper() == 'S':
    
    # nome = input('Informe nome do aluno: ')
    
    # genero = input('Informe o Genero do aluno(M/F): ')

    # while genero.upper() !='M' and genero.upper()!='F':

    #     genero= input('Opção Inválida, informe (M/F): ')
    
    #while genero.upper() == 'M' or genero.upper() == 'F':

    for cont in range (1,4):
       if cont==1:
           nota1 = int(input('Informe N1:'))
           while nota1<0 or nota1>10:
               nota1 =int(input('N1 inválido, valor deve ser entre 0 e 10: '))
       elif cont==2:
           nota2 = int(input('Informe N2:'))
       while nota2 < 0 or nota2 > 10:
           nota2 = int(input('N2 inválido, valor deve ser entre 0 e 10: '))
    else:
       nota3 = int(input('Informe N3:'))
       while nota3 < 0 or nota3 > 10:
           nota3 = int(input('N3 inválido, valor deve ser entre 0 e 10: '))

    #calcular média e verificar status do alunos
    
    media = (nota1+nota2+nota3)/3

    print(str(media))

    if media>=7:
         aprovados+=1
       
    elif media>=4:
         exame+=1
    else:
         reprovados+=1
    
    #calcula media aluno feminino
    cadastrar = input('Deseja efetuar outro lançamento (S/N)? ')
    while cadastrar.upper() != 'S' and cadastrar.upper() != 'N':
        cadastrar = input('Opção Inválida, informe (S/N): ')

else:
    print('Lancamentos Finalizados')

print('Total de alunos APROVADOS: ' +str(aprovados))
print('Total de alunos de EXAME: ' +str(exame))
print('Total de alunos REPROVADOS: ' +str(reprovados))

if genero=='M' and aprovados:

    print('Total de pessoas do sexo masculino aprovadas'+ str(aprovados))

if genero=='F' and aprovados:

    print('Total de pessoas do sexo feminino aprovadas'+ str(aprovados))

if genero=='M' and exame:

    print('Total de pessoas do sexo masculino de exame'+ str(exame))

if genero=='F' and exame:

    print('Total de pessoas do sexo feminino de exame'+ str(exame))

if genero=='M' and reprovados:

    print('Total de pessoas do sexo masculino reprovadas'+ str(reprovados))

if genero=='F' and reprovados:

    print('Total de pessoas do sexo feminino reprovadas'+ str(reprovados))


