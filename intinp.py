#To show how to take input of integers using input(), string.split(), for loop and a random variable for storing the list

lista = []
inp = input("Enter the required numbers (Provide some spaces too) : ")
inp2 = inp.split()
lng = len(inp2)
for i in range(0,lng):
    inp2[i] = int(inp2[i])
    #print(inp2[i])
    lista.append(inp2[i])
print(lista)

