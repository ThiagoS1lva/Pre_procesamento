import unidecode
import string

base = [['EXCESS@!O'], ['Hoje eu comi !rango assado'],['subsídio'], ['paralisaao'], ['licensa']]
print("Printando remoção")
            
#Removendo letras repetidas juntas na palavra
for lista in base:
    for palavra in lista:
        palavra = list(palavra)
        x = 0
        while x < len(palavra) - 1:
            if palavra[x] == palavra[x+1]:
                del palavra[x]
                x -= 1
            x += 1
                    #junta as letras e a deixa em minusculo
        lista[0] = ''.join(palavra).lower()
                    #removendo acentos
        lista[0] = unidecode.unidecode(lista[0])
                    #removendo pontuação
        lista[0] = ''.join(c for c in lista[0] if c not in string.punctuation)
print(base)  