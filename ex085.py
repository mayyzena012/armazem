#
nums = [[],[]]
num = 0

for n in range(7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)
    
nums[0].sort()
nums[1].sort()

print(f'os valores pares digitados foram {nums[0]}')
print(f'os valors impares digitados foram {nums[1]}')
