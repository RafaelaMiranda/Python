n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

formar = n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2
equilatero = n1 == n2 == n3
isosceles = n1 == n2 or n1 == n3 or n2 == n3
escaleno = n1 != n2 or n1 != n3 or n2 != n3

if formar and equilatero:
    print('Os segmentos acima PODEM FORMAR triângulo EQUILÁTERO')
elif formar and isosceles:
    print('Os segmentos acima PODEM FORMAR triângulo ISÓSCELES')
elif formar and escaleno:
    print('Os segmentos acima PODEM FORMAR triângulo ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')