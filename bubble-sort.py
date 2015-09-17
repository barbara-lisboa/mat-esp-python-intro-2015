N = 20
lista = [11,18,3,1,16,12,6,19,5,0,14,4,17,9,13,7,10,15,2,8]
for i in range(0, N-1, 1):
    for j in range(i+1, N, 1):
	    if lista [i] > lista [j]:
		    temp = lista [i]
			lista [i] = lista [j]
			lista [j] = temp
print(lista)			
