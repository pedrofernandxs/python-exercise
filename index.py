salary = float(input("Informe o salário: "))
salary_init = salary
reaj = 0
real_salary = 0

if salary <= 280:
    reaj = salary * 0.20
    salary += reaj
    real_salary = salary - (salary * 0.038)
    
    print("Salário Inicial:", salary_init)
    print("Aumento de 20%")
    print("Valor do aumento:", reaj)
    print("Salário Novo:", salary)
    print("Salário Real Pós Inflação:", real_salary)
    
elif 280 < salary < 700:
    reaj = salary * 0.15
    salary += reaj
    real_salary = salary - (salary * 0.038)
     
    print("Salário Inicial:", salary_init)
    print("Aumento de 15%")
    print("Valor do aumento:", reaj)
    print("Salário Novo:", salary)
    print("Salário Real Pós Inflação:", real_salary)
    
elif 700 < salary < 1500:
    reaj = salary * 0.10
    salary += reaj
    real_salary = salary - (salary * 0.038)
    
    print("Salário Inicial:", salary_init)
    print("Aumento de 10%")
    print("Valor do aumento:", reaj)
    print("Salário Novo:", salary)
    print("Salário Real Pós Inflação:", real_salary)
    
elif salary > 1500:
    reaj = salary * 0.05
    salary += reaj
    real_salary = salary - (salary * 0.038)
    
    print("Salário Inicial:", salary_init)
    print("Aumento de 5%")
    print("Valor do aumento:", reaj)
    print("Salário Novo:", salary)
    print("Salário Real Pós Inflação:", real_salary)