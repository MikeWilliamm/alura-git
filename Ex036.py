casa = float(input('\nTitulo? '))
salario = float(input('\nQual valor do salario? '))
anos = int(input('\ncurso? '))
teste = int(input('\teste? '))
teste2 = int(input('\teste2? '))
<<<<<<< HEAD
teste4 = 'aaaaa'  
=======

teste5 'dsda'

>>>>>>> b6c7ea162a5543fca8bac5a51d68592aca24f1c7

parcelas = casa / (anos * 12) 
porcentagem = (salario * 30) / 100

if parcelas > porcentagem:
    print('\nPara comprar uma casa de {} a prestação será de R${:.2f} em {}x vezes\nEmprestimo Negado!\nA prestação mensal não pode exceder 30''%'' do salário!'.format(casa, parcelas, anos * 12))
elif parcelas <= porcentagem:
    print('\nPara comprar uma casa de {} a prestação será de R${:.2f} em {}x vezes\nEmprestimo Aprovado!'.format(casa, parcelas, anos * 12))

#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.