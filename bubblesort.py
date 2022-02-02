lista = []
inp = input("Enter the required numbers (Provide some spaces too) : ")
inp2 = inp.split()
lng = len(inp2)
for i in range(0,lng):
    inp2[i] = int(inp2[i])
    #print(inp2[i])
    lista.append(inp2[i])
print(lista)

print("The sorted version of the list :- ")
for s in range(0,len(lista)):
    if (lista[s] > lista[s+1]):
        #using an empty var z for purpose
        z = lista[s+1]
        lista[s+1] = lista[s]
        lista[s] = z
    # else:
    #     pass
print(lista)
