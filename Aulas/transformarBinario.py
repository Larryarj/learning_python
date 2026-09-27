decimal = int(input('digite um numero para transformar em binario: '))
bin = []

while decimal > 0:

    if decimal >= 1:
        
        bit = decimal % 2
        bin.append(bit)
        decimal = decimal // 2

    else:
        bin.append(1)
        decimal = 0

bin.reverse()
print(bin)
