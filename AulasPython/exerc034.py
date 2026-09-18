sal = float(input('digite o salário do funcionário: '))

if sal >= 1250:
    salnovo = sal * 1.1
else:
    salnovo = sal * 1.15

print(f"salário novo: {salnovo}")
