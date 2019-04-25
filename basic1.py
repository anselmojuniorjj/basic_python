#tupla
tup = (1,2,3)

#dicionário
dic = {'valor1': '10', 'valor2': '20'}
print(dic['valor2'])

#lista
lista1 = [1,2,3]
lista2 = [1,2, [11,22,33], 'hello']

print(lista2[2][2])
print(lista2[3])

lista3 = [2,4]
lista3.append(6)
print(lista3)

a = lista3.pop()
print(lista3)
print(a)

b = lista3.pop(1)
print(lista3)
print(b)

lista4 = [1,2,3,4,5]
lista4.reverse()
print(lista4)

# loop

seq = [1,2,3]

for i in seq:
    print(i)

for i in range(1, 4):
    print(i)

i = 1

while i < 4:
    print('i = {a}'.format(a=i))
    i += 1
#print('i = {}'.format(i))

out = []
x = [1,2,3]

for item in x:
    out.append(item ** 2)

print(out)

elevado = [item**2 for item in x]
print(elevado)

# operador in

print(2 in [1,2,3,4])
print('hello' in [1,2,'hello',4])