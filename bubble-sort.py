import matplotlib.pyplot as plt
N = 20 #numero de variaveis
lista = [11,18,3,1,16,12,6,19,5,0,14,4,17,9,13,7,10,15,2,8] #lista de variaveis entre colchetes

#gráfico figura final (lista desorganizada)

plt.figure() 
plt.plot(range(0, N),lista,'ok')
plt.title("Estado Inicial")
plt.xlabel("Indice")
plt.ylabel("Valor")
plt.savefig("fig/bubble-inicio.png")
plt.close()

troca = 0
print("lista original", lista) #python executa a lista original
for i in range(0, N-1, 1): #para gerar a lista i usa-se o comando range, onde os dois primeiros valores representam o começo e o fim da lista, e o terceiro representa o intervalo entre eles
    for j in range(i+1, N, 1): #para gerar a lista j usa-se o comanado range, repitindo o processo anterior para determinar a ordem
        if lista [i] > lista [j]: #caso a i seja maior que j, aplica-se os proximos codigos, caso seja menor, pega-se o proximo numero
            temp = lista [i]  #temp funciona como uma terceira variavel, que é igual a variavel i
            lista [i] = lista [j] #i é igual a j, e temp continua sendo igual a i antes de ser igual a j
            lista [j] = temp #j troca de lugar com i
            troca = troca + 1
            plt.figure()
            plt.plot(range(0, N),lista,'ok')
            plt.title("Estado Transitorio")
            plt.xlabel("Indice")
            plt.ylabel("Valor")
            plt.savefig("fig/bubble-troca-{}.png".format(troca))
            plt.close()
            
            plt.figure()
            plt.plot(i,lista[i],'or')
            plt.plot(j,lista[j],'ob')
            plt.plot(range(0, N, 1),lista,'ok')
            plt.title("Iteracao")
            plt.xlabel("Indice")
            plt.ylabel("Valor")
            plt.savefig("fig/bubble-it-{}.png".format(troca))
            plt.close()

print("lista em ordem crescente", lista) #python executa a lista original em ordem crescente 
lista [0:5] 
lista [N:N-6:-1]
print("cinco maiores valores", lista [N:N-6:-1])
print("cinco menores valores", lista [0:5])


