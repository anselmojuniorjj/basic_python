def minha_funcao(x):
    print(x)

minha_funcao('hello man')

def elevar(x):
    y = x**2
    return y

x = 4
result = elevar(x)
print(result)

#map, 1º parametro uma função, 2º um lista. chama a função e percorre tds elementos da lista
seq = [1,2,3,4,5]
r = list(map(elevar, seq))  
print(r)

#função lambda, é usada apenas uma vez
r2 = list(map(lambda x: x**2, seq))
print(r2)

#filter, filtra elementos, de acordo com funçã
r3 = list(filter(lambda x : x % 2 == 0, seq))
minha_funcao(r3)

r4 = str.upper('hello python')
minha_funcao(r4)