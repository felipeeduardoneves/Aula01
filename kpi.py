CONSTANTE_BONUS = 1000

# Solicite ao usuário que digite seu nome

nome = input("Qual seu nome")

# Solicita ao usuario qye digite seu salario

sal = float(input("Qual seu salário"))

#Solicita ao usuario que digite o valor de bonus recebido

bonus = float(input("Qua seu percentual de bonus"))

#Calcule o vlaor do bonus do usuario

valor_bonus = CONSTANTE_BONUS + sal * bonus

# Imprime calculo do KPI para o usuario

print(f"O Usuario {nome} possui o valor a receber de bonus de {valor_bonus}")