frase = 'Curso em Vídeo Python'

## FATIAMENTO

print(frase[9])
print(frase[9:21])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase)) # Quantidade de caracteres na frase
print(frase.count('o')) # Quantidade de letras O na frase
print(frase.count('o', 0, 13)) # Contagem com fatiamento do 0 ao 12
print(frase.find('deo')) # Na posição que iniciou o DEO
print('Curso' in frase) # Se existe Curso na variavel frase

## TRANSFORMAÇÃO

print(frase.replace('Python', 'Android')) # Muda python para android
print(frase.upper()) # Tudo maiusculo
print(frase.lower()) # Tudo minisculo
print(frase.capitalize()) # Apenas primeira letra maisculo
print(frase.title()) # Primeira letra maisculo por palavra
print(frase.strip()) # Remove os espaços do começo e fim da frase
print(frase.rstrip()) # Remove os espaços do fim da frase
print(frase.lstrip()) # Remove os espaços do inicio da frase

## DIVISÃO

print(frase.split()) # Criando divisão por espaço

## JUNÇÃO

print('-'.join(frase))