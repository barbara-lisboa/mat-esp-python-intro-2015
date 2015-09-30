import matplotlib.pyplot as plt
N = 20 #numero de variaveis
lista = [11,18,3,1,16,12,6,19,5,0,14,4,17,9,13,7,10,15,2,8] #lista de variaveis entre colchetes

#gráfico figura final (lista desorganizada)

plt.figure() #cria figura
plt.plot(range(0, N),lista,'ok') #propriedades do grafico: alcance, variavel utilizada, grafico de bolas pretas
plt.title("Estado Inicial") #adiciona titulo 
plt.xlabel("Indice") #nomeia o eixo x
plt.ylabel("Valor") #nomeia o eixo y
plt.savefig("fig/bubble-inicio.png") #nomeia os arquivos criados e os coloca na pasta fig
plt.close() #termina a criacao dos graficos

troca = 0 #cria uma variavel troca
iteracao = 0 #cria uma variavel iteracao
print("lista original", lista) #python executa a lista original
for i in range(0, N-1, 1): #para gerar a lista i usa-se o comando range, onde os dois primeiros valores representam o começo e o fim da lista, e o terceiro representa o intervalo entre eles
    for j in range(i+1, N, 1): #para gerar a lista j usa-se o comanado range, repitindo o processo anterior para determinar a ordem
        iteracao = iteracao + 1 #faz com que iteracao seja contada corretamente
        plt.figure() #linhas 21 a 29 possuem as mesmas propriedades do grafico feito anteriormente
        plt.plot(range(0, N, 1),lista,'ok')
        plt.plot(i,lista [i],'or') #grafico de bolas vermelhas
        plt.plot(j,lista [j],'ob') #grafico de bolas azuis
        plt.title("Iteracao {}".format(iteracao))
        plt.xlabel("Indice")
        plt.ylabel("Valor")
        plt.savefig("fig/bubble-it-{}.png".format(iteracao)) #{} e .format servem para variar iteracao dentro do {}
        plt.close()
        if lista [i] > lista [j]: #caso a i seja maior que j, aplica-se os proximos codigos, caso seja menor, pega-se o proximo numero
            temp = lista [i]  #temp funciona como uma terceira variavel, que é igual a variavel i
            lista [i] = lista [j] #i é igual a j, e temp continua sendo igual a i antes de ser igual a j
            lista [j] = temp #j troca de lugar com i
            troca = troca + 1
            plt.figure() #linhas 35 a 41 possuem as mesmas propriedades dos graficos feitos anteriormente
            plt.plot(range(0, N),lista,'ok')
            plt.title("Estado Transitorio")
            plt.xlabel("Indice")
            plt.ylabel("Valor")
            plt.savefig("fig/bubble-troca-{}.png".format(troca))
            plt.close()
            
print("lista em ordem crescente", lista) #python executa a lista original em ordem crescente 
lista [0:5] #pega os 5 primeiros valores da lista
lista [N:N-6:-1] #pega os 5 ultimos valores da lista
print("cinco maiores valores", lista [N:N-6:-1]) #escreve os cinco maiores valores 
print("cinco menores valores", lista [0:5]) #escreve os cinco menores valores

#gráfico figura inicial (lista organizada)
plt.figure() #linhas 50 a 56 possuem as mesmas propriedades do grafico feito anteriormente
plt.plot(range(0, N),lista,'ok')
plt.title("Estado Final")
plt.xlabel("Indice")
plt.ylabel("Valor")
plt.savefig("fig/bubble-fim.png")
plt.close()



