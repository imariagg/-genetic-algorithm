
import random
import copy
import math
import statistics
from Individuo import Individuo

#---------------------------------------FUNCIONES AUXILIARES---------------------------------------------------------------------------

def mostrar_poblacion(poblacion):
    for i in range(len(poblacion)):
        print('Individuo ' + str(i) + ', Genes: ' + str(poblacion[i].getGenes()) + ', Fitness: ' + str(poblacion[i].getFitness()))

def iteraciones(poblacion_reemplazada, si_hay_referencia, valor_fitness_referencia, max_iteraciones_sin_mejorar, si_hay_max_iteraciones, max_iteraciones, maximiza_minimiza): #Si no hay max iteraciones se pone a -1
    
    mostrar_poblacion(poblacion_reemplazada)
    #Elegimos el mejor de la poblacion seleccionada primero

    if maximiza_minimiza==1:
        num = max(poblacion_reemplazada, key=lambda ind: ind.getFitness()).getFitness()
        ind_mejor_fitness=Individuo([],num)
        
    elif maximiza_minimiza==-1:
        num = min(poblacion_reemplazada, key=lambda ind: ind.getFitness()).getFitness()
        ind_mejor_fitness=Individuo([],num)

    
    acabar=False

    for ind in poblacion_reemplazada:
        
        if ind.getFitness() == ind_mejor_fitness.getFitness():
            ind_mejor_fitness=ind
            print('Mejor desde un principio')
            ind.mostrar()

      
    if (si_hay_referencia=='si'):
            acabar=True
            
        
              
    #Ya tenemos el mejor de la poblacion seleccionada
    cont_iteraciones_sin_mejorar=0
    cont=0 
    it=0

    while(cont_iteraciones_sin_mejorar != max_iteraciones_sin_mejorar or it==max_iteraciones ):

        if acabar==True:
            print('Hemos encontrado el individuo que buscamos:')
            ind_mejor_fitness.mostrar()
            break


        copia_poblacion_inicial_para_reemplazo = copy.deepcopy(poblacion_reemplazada)
        copia_poblacion_inicial2 = copy.deepcopy(poblacion_reemplazada)
        

        '''MAXIMIZANDO'''
        poblacion_seleccionada=seleccionTorneo(copia_poblacion_inicial2, 50,3,1) #(poblacion, n_seleccionados_total, n_participantes_en_pelea, minimiza_o_maximiza)
        #poblacion_seleccionada=seleccionOrdenLineal(copia_poblacion_inicial2, 50, 1)
        #poblacion_seleccionada=seleccionEmparejamientoVariadoInversoNAM(copia_poblacion_inicial2, 50, 6, 'BINARIO') #pob, seleccionados y N en torneo
        #poblacion_seleccionada=seleccionRuleta(copia_poblacion_inicial2, 50, 1)

        poblacion_cruzada=cruceBinario(poblacion_seleccionada, 30, 2, 0.7) #poblacion, n_cruces, probabilidad

        poblacion_mutada=mutacionBinaria(poblacion_cruzada,0.2,0.2) #poblacion, probabilidad_individuo, probabilidad_gen

        poblacion_reemplazada=reemplazoPeorRW(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 1, 'BINARIO') #p_inicial, p_mutada, elitismo, maximiza_miniza, tipo
        #poblacion_reemplazada=reemplazoTorneoRestringuidoTRS(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 3, 1, 'BINARIO')
        #poblacion_reemplazada=reemplazoPeorEntreSemejantes(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 3, 1, 'BINARIO')
        #poblacion_reemplazada=reemplazoCrowdingDeterministicoDC(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 1, 'BINARIO')


        '''MINIMIZANDO'''
        #poblacion_seleccionada=seleccionTorneo(copia_poblacion_inicial2, 50,3,1) #(poblacion, n_seleccionados_total, n_participantes_en_pelea, minimiza_o_maximiza)
        #poblacion_seleccionada=seleccionOrdenLineal(copia_poblacion_inicial2, 50, 1)
        #poblacion_seleccionada=seleccionEmparejamientoVariadoInversoNAM(copia_poblacion_inicial2, 50, 6, 'BINARIO') #pob, seleccionados y N en torneo
        #poblacion_seleccionada=seleccionRuleta(copia_poblacion_inicial2, 50, 1)

        #poblacion_cruzada=cruceBinario(poblacion_seleccionada, 30, 2, 0.7) #poblacion, n_cruces, probabilidad

        #poblacion_mutada=mutacionBinaria(poblacion_cruzada,0.2,0.2) #poblacion, probabilidad_individuo, probabilidad_gen

        #poblacion_reemplazada=reemplazoPeorRW(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 1, 'BINARIO') #p_inicial, p_mutada, elitismo, maximiza_miniza, tipo
        #poblacion_reemplazada=reemplazoTorneoRestringuidoTRS(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 3, 1, 'BINARIO')
        #poblacion_reemplazada=reemplazoPeorEntreSemejantes(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 3, 1, 'BINARIO')
        #poblacion_reemplazada=reemplazoCrowdingDeterministicoDC(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 1, 'BINARIO')


        mostrar_poblacion(poblacion_reemplazada)
        for ind in poblacion_reemplazada:
            
            if maximiza_minimiza==1:
                if ind.getFitness() > ind_mejor_fitness.getFitness():
                    ind_mejor_fitness=ind
                    print('Mejor x ahora')
                    ind.mostrar()
                    cont_iteraciones_sin_mejorar=0
                    cont+=1

            elif maximiza_minimiza==-1:

                if ind.getFitness() < ind_mejor_fitness.getFitness():
                    ind_mejor_fitness=ind
                    print('Mejor x ahora')
                    ind.mostrar()
                    cont_iteraciones_sin_mejorar=0
                    cont+=1


            if (si_hay_referencia=='si'):
                if ind.getFitness()==valor_fitness_referencia:
                    ind_mejor_fitness=ind
                    acabar=True
                   
        if cont==0:
            cont_iteraciones_sin_mejorar+=1
            print('Cont_iteraciones_sin_mejorar')
            print(cont_iteraciones_sin_mejorar)
        else:
            cont=0

        if si_hay_max_iteraciones=='si':
            it+=1
            print('it')
            print(it)
            if it==max_iteraciones:
                break

        elif si_hay_max_iteraciones=='no':
            it-=1

    print('El mejor individuo encontrado es:')
    ind_mejor_fitness.mostrar()


#---------------------------------------FUNCIONES INICIALES---------------------------------------------------------------------------

def generaPoblacionBinaria(tamanoPoblacion, numeroBitsIndividuo):

    for i in range(0,tamanoPoblacion):
        individuo = Individuo([],0)
        genes_aux=[]
        for j in range(0,numeroBitsIndividuo):
            bit = random.randint(0, 1)
            genes_aux.append(bit)
        individuo.setGenes(genes_aux)    
        poblacion_inicial.append(individuo)

    return poblacion_inicial


def funcionObjetivo(poblacion, tipo):
    if tipo=='BINARIO':
        return funcionObjetivoB(poblacion)
    
def funcionObjetivoB(poblacion_inicial):

    cont=0
    poblacion_aux=[]

    for individuo in poblacion_inicial:
        genes=individuo.getGenes()
        for gen in genes:
            if gen==1:
                cont+=1
        individuo.setFitness(cont)
        poblacion_aux.append(individuo)
        cont=0

    return poblacion_aux

def mochila(poblacion_inicial):

    ind=Individuo([0,1,0,1,0])
    poblacion_inicial=[ind]
    poblacion_aux=[]
    mochila=[[2,650],[4,12],[1,1],[0.1,150],[0.2,200]]
    tam_total_mochila=5
    

    for p in poblacion_inicial:
        it=0
        tam_aux_mochila=0
        peso_aux=0
        precio_aux=0

        for gen in p.getGenes():
            
            if gen==1:
                item=mochila[it]
                peso=item[0]
                precio=item[1]

                peso_aux=peso_aux+peso
                precio_aux=precio_aux+precio
            it=it+1   
        if peso_aux<tam_total_mochila:
            p.setFitness(precio_aux)

        else:
            p.setFitness(0)
    poblacion_aux.append(p)

    return poblacion_aux



def distancia(individuo1, individuo2, tipo):
    if tipo=='BINARIO':
        return distanciaB(individuo1, individuo2)

def distanciaB(individuo1, individuo2):
    #Manhattan
    genes_indiv1=individuo1.getGenes()
    genes_indiv2=individuo2.getGenes()
    distancia=0

    for gen in range(len(genes_indiv1)):
        if genes_indiv1[gen]!=genes_indiv2[gen]:
            distancia=distancia+1
    
    return distancia


#-------------------------------------------SELECCIONES----------------------------------------------------------------------------

def seleccionTorneo(poblacion, n_seleccionados_total, n_participantes_en_pelea, minimiza_o_maximiza):  
#Si tienes una N mayor es explotacion porque encuentras al mayor fitness del tiron
#Si tienes una N menor busca en un rango menor por tanto explora mas
    poblacion_aux=poblacion
    seleccionados = []
    
    while len(seleccionados) < n_seleccionados_total:
        participantes = random.sample(poblacion_aux, n_participantes_en_pelea)

        if minimiza_o_maximiza == 1: #Maximiza
            mejor_individuo = max(participantes, key=lambda parti: parti.getFitness())
        elif minimiza_o_maximiza == -1: #Minimiza
            mejor_individuo = min(participantes, key=lambda parti: parti.getFitness())

        seleccionados.append(mejor_individuo)
        poblacion_aux.remove(mejor_individuo)
    
    return seleccionados

#Va acutalizando la probababilidad y es exponencial
def seleccionOrdenLineal(poblacion, n_seleccionados_total, minimiza_o_maximiza):
    #Si maximiza es 1 y si minimiza -1
    seleccionados = []
    pob_ordenada=[]
    pob_ordenada_con_prob=[]
    
    if (minimiza_o_maximiza==1): #maximiza
        #Ordena de menor a mayor segun el fitness
        pob_ordenada=sorted(poblacion, key=lambda ind: ind.getFitness())
       
       
    elif(minimiza_o_maximiza==-1): #minimiza
        #Ordena de mayor a menor segun el fitness
        pob_ordenada=sorted(poblacion, key=lambda ind: -ind.getFitness())

    print('ordena')    
    mostrar_poblacion(pob_ordenada)

    lista_aux=pob_ordenada 
    for i in range(n_seleccionados_total):
        
        probabilidad=(1/len(lista_aux))
        cont=probabilidad
        lista_aux2=[]
        probabilidades=[]
        #probabilidades = np.exp(np.linspace(np.log(probabilidad), 0, len(lista_aux)))
        
        for j in range(len(lista_aux)):
            p = math.exp(math.log(probabilidad) * (1 - j / (len(lista_aux)-1)))
            probabilidades.append(p)
        #print(probabilidades)

        j=0
        for individuo in lista_aux:
            individuo.setProb_seleccionOrdenLineal(probabilidades[j])
            lista_aux2.append(individuo)
            j=j+1

        
        ind_seleccionado = random.choices(range(len(lista_aux2)), weights=probabilidades, k=1)[0]
        
        seleccionado=lista_aux2[ind_seleccionado]
        seleccionados.append(seleccionado)
        del lista_aux2[ind_seleccionado]
        del probabilidades[ind_seleccionado]
        lista_aux=lista_aux2


    print('a')
    return seleccionados


def seleccionEmparejamientoVariadoInversoNAM(poblacion, n_seleccionados_total, N, tipo):

    poblacion_aux=poblacion
    seleccionados=[]

    while (len(seleccionados)!=n_seleccionados_total):
        
       
        seleccionado1=random.choice(poblacion_aux)
        distancia_max=0
        distancia_aux=0
        pos_mayor_distancia=0
        i=0
        poblacion_aux.remove(seleccionado1) #si no hago esto se hace la distancia consigo mismo a lo mejor
        poblacion_n_torneo=random.sample(poblacion_aux, N)

        for individuo in poblacion_n_torneo:
            distancia_aux=distancia(seleccionado1,individuo,tipo)
            if(distancia_aux>distancia_max):
                distancia_max=distancia_aux
                pos_mayor_distancia=i
            i=i+1

        
        seleccionado2=poblacion_aux[pos_mayor_distancia]
        seleccionados.append(seleccionado1)
        seleccionados.append(seleccionado2)
        #poblacion_aux.remove(seleccionado1) #Ya lo hago arriba
        poblacion_aux.remove(seleccionado2)
       
    return seleccionados




def seleccionRuleta(poblacion, n_seleccionados_total, minimiza_o_maximiza):
    
    poblacion_aux=poblacion
    lista_fitnesses=[]
    #Sacar fitness maximo 
    for individuo in poblacion_aux:
        #print('proxima vuelta')
        lista_fitnesses.append(individuo.getFitness())

        if minimiza_o_maximiza == 1:
            max_fitness=max(poblacion_aux, key=lambda parti: parti.getFitness()).getFitness()
            min_fitness=min(poblacion_aux, key=lambda parti: parti.getFitness()).getFitness()
            #print(max_fitness)
            #max_fitness=0
            #f (individuo.getFitness()>max_fitness):
                #max_fitness=individuo.getFitness()
                #max_fitness=print(max(poblacion_aux, key=lambda parti: parti.getFitness()).getFitness())
        
        elif minimiza_o_maximiza == -1:
            max_fitness=max(poblacion_aux, key=lambda parti: parti.getFitness()).getFitness() #Sigue min_fitness
            min_fitness=min(poblacion_aux, key=lambda parti: parti.getFitness()).getFitness()
            #print(max_fitness)
            
            #max_fitness=max(poblacion_aux, key=lambda parti: parti.getFitness())
            #if (individuo.getFitness()<max_fitness):
                #max_fitness=individuo.getFitness() #En realidad es la menor
                #print(min(poblacion_aux, key=lambda parti: parti.getFitness()))
            
        
    probabilidades=[]
    


    for individuo in poblacion_aux:
        
        if minimiza_o_maximiza == 1: #Maximiza
            #probabilidad=individuo.getFitness()/max_fitness

            # Crear un vector de pesos con más peso en los valores más cercanos a -200
            probabilidades = [math.exp(-(x - max_fitness) ** 2 / (2 * 10 ** 2)) for x in lista_fitnesses]

            # Crear un vector de pesos con más peso en los valores más cercanos a +100
            

        elif minimiza_o_maximiza == -1: #Minimiza
           #probabilidad=max_fitness/individuo.getFitness()
           
            probabilidades = [math.exp(-(x - min_fitness) ** 2 / (2 * 10 ** 2)) for x in lista_fitnesses]
        #probabilidades.append(probabilidad)



    seleccionados=[]
    for i in range(n_seleccionados_total):
    
        ind_seleccionado = random.choices(range(len(poblacion_aux)), weights=probabilidades, k=1)[0]
        
        seleccionado=poblacion_aux[ind_seleccionado]
        seleccionados.append(seleccionado)
        del poblacion_aux[ind_seleccionado]
        del probabilidades[ind_seleccionado]
        
    return seleccionados


#---------------------------------------------CRUCES---------------------------------------------------------------------------------

#1 cruce para binario, 1 para permutaciones y 2 para reales

def cruceBinario(poblacion, n_puntos_cruce, n_cruces, probabilidad):

    seleccionados=[]
    for k in range(0, n_cruces):

        padre1=random.choices(poblacion)[0]
        padre2=random.choices(poblacion)[0]
   
        while(padre1==padre2):
            padre2=random.choices(poblacion)[0]

        probabilidad_aux = random.random()
        if probabilidad>probabilidad_aux:
            
            if n_puntos_cruce==1 :
                punto_cruce = random.randint(1, len(padre1.getGenes()) - 1)
                print(punto_cruce)
                descendiente_c1 = padre1.getGenes()[:punto_cruce] + padre2.getGenes()[punto_cruce:]
                descendiente_c2 = padre2.getGenes()[:punto_cruce] + padre1.getGenes()[punto_cruce:]

                hijo1 = Individuo(descendiente_c1)
                hijo2 = Individuo(descendiente_c2)
                seleccionados.append(hijo1)
                seleccionados.append(hijo2)

            elif n_puntos_cruce==2:
                lista_puntos_cruce=[]
                i=0
                for i in range(n_puntos_cruce):
                    lista_puntos_cruce.append(random.randint(1, len(padre1.getGenes()) - 1)) #cuidado que se repiten
                
                while(lista_puntos_cruce[0]==lista_puntos_cruce[1]):
                    lista_puntos_cruce[1]=random.randint(1, len(padre1.getGenes()) - 1)

                lista_puntos_cruce.sort()
                descendiente_c1 = padre1.getGenes()[:lista_puntos_cruce[0]] + padre2.getGenes()[lista_puntos_cruce[0]:lista_puntos_cruce[1]] + padre1.getGenes()[lista_puntos_cruce[1]:]
                descendiente_c2 = padre2.getGenes()[:lista_puntos_cruce[0]] + padre1.getGenes()[lista_puntos_cruce[0]:lista_puntos_cruce[1]] + padre2.getGenes()[lista_puntos_cruce[1]:]
               
                hijo1 = Individuo(descendiente_c1)
                hijo2 = Individuo(descendiente_c2)
                seleccionados.append(hijo1)
                seleccionados.append(hijo2)
                
            elif n_puntos_cruce==3:
                lista_puntos_cruce=[]
                i=0
                for i in range(n_puntos_cruce):
                    cruce_aux=(random.randint(1, len(padre1.getGenes()) - 1)) 
                   
                    while(cruce_aux in lista_puntos_cruce):
                        cruce_aux=(random.randint(1, len(padre1.getGenes()) - 1))
                           
                    lista_puntos_cruce.append(cruce_aux)
                    

                lista_puntos_cruce.sort()
                descendiente_c1 = padre1.getGenes()[:lista_puntos_cruce[0]] + padre2.getGenes()[lista_puntos_cruce[0]:lista_puntos_cruce[1]] + padre1.getGenes()[lista_puntos_cruce[1]:lista_puntos_cruce[2]] + padre2.getGenes()[lista_puntos_cruce[2]:]
                descendiente_c2 = padre2.getGenes()[:lista_puntos_cruce[0]] + padre1.getGenes()[lista_puntos_cruce[0]:lista_puntos_cruce[1]] + padre2.getGenes()[lista_puntos_cruce[1]:lista_puntos_cruce[2]] + padre1.getGenes()[lista_puntos_cruce[2]:]
                
                hijo1 = Individuo(descendiente_c1,0, padre1.getGenes(), padre2.getGenes())
                hijo2 = Individuo(descendiente_c2,0, padre1.getGenes(), padre2.getGenes())
                seleccionados.append(hijo1)
                seleccionados.append(hijo2)

      

    funcionObjetivoB(seleccionados) 
    return seleccionados
   
#--------------------------------------------MUTACIÓN---------------------------------------------------------------------------------

def mutacionBinaria(poblacion, probabilidad_individuo, probabilidad_gen):
    poblacion_aux=[]
    poblacion_aux=poblacion
    
    for individuo in poblacion_aux:
        probabilidad_individuo_aux=random.random()
        if probabilidad_individuo_aux < probabilidad_individuo:
            #Se hace la mutacion
            for it in range(len(individuo.getGenes())):
                probabilidad_gen_aux=random.random()
                if probabilidad_gen_aux < probabilidad_gen:
                    if individuo.getGenes()[it] == 1:
                        individuo.genes[it]=0
                   
                    elif individuo.getGenes()[it] == 0:
                        individuo.genes[it]=1   

    funcionObjetivoB(poblacion_aux)
    return poblacion_aux        
     
#----------------------------------------REEMPLAZAMIENTO---------------------------------------------------------------------------------

def reemplazoPeorRW(p_inicial, p_mutada, elitismo, maximiza_miniza, tipo):
    
    n_individuos_elitistas=0
    if elitismo>0:
        n_individuos_elitistas=int(round((elitismo*len(p_inicial))/100, 0))

    p_elitista=[]
    p_reemplazada=[]


    if maximiza_miniza==1:  #Maximiza
        p_inicial = sorted(p_inicial, key=lambda ind: ind.getFitness(), reverse=True)
        p_elitista=p_inicial[0:n_individuos_elitistas]


        for i in range(0,n_individuos_elitistas):
            p_inicial.remove(p_elitista[i])

        p_inicial = sorted(p_inicial, key=lambda ind: ind.getFitness(), reverse=False) #De menor a mayor
        
    
    elif maximiza_miniza==-1: #Minimiza
        p_inicial = sorted(p_inicial, key=lambda ind: ind.getFitness(), reverse=False) 
        p_elitista=p_inicial[0:n_individuos_elitistas]

        for i in range(0,n_individuos_elitistas):
            p_inicial.remove(p_elitista[i])

        p_inicial = sorted(p_inicial, key=lambda ind: ind.getFitness(), reverse=True) #De mayor a menor
        


    n_hijos_mutados=len(p_mutada)
    p_inicial[0:n_hijos_mutados]=[]

    p_reemplazada = p_inicial + p_mutada + p_elitista
    funcionObjetivo(p_reemplazada, tipo)
   

    if maximiza_miniza==1:  #Maximiza
        p_reemplazada = sorted(p_reemplazada, key=lambda ind: ind.getFitness(), reverse=True) #Estan a la izq los mejores
       
    
    elif maximiza_miniza==-1: #Minimiza
        p_reemplazada = sorted(p_reemplazada, key=lambda ind: ind.getFitness(), reverse=False) #Estan a la izq los mejores
      

    return p_reemplazada


def reemplazoTorneoRestringuidoTRS(p_inicial, p_mutada, elitismo, w, maximiza_miniza, tipo):

    n_individuos_elitistas=0
    if elitismo>0:
        n_individuos_elitistas=int(round((elitismo*len(p_inicial))/100, 0))

    p_elitista=[]
    p_reemplazada=[]

    if maximiza_miniza==1: 
        p_inicial = sorted(p_inicial, key=lambda ind: ind.getFitness(), reverse=True) #Estan a la izq los mejores
        p_elitista=p_inicial[0:n_individuos_elitistas]

        for i in range(0,n_individuos_elitistas):
            p_inicial.remove(p_elitista[i])

    elif maximiza_miniza==-1:
        p_inicial = sorted(p_inicial, key=lambda ind: ind.getFitness(), reverse=False) #Estan a la izq los mejores
        p_elitista=p_inicial[0:n_individuos_elitistas]

        for i in range(0,n_individuos_elitistas):
            p_inicial.remove(p_elitista[i])

    for ind_m in p_mutada:
        poblacion_w_aux=[]

        poblacion_w_aux=random.sample(p_inicial, w)
        distancias_lista_aux=[]

        for ind_w_aux in poblacion_w_aux:
            
            distancias_lista_aux.append(distancia(ind_w_aux, ind_m,tipo))


        posicion_menor_distancia = distancias_lista_aux.index(min(distancias_lista_aux))
       
        individuo_menor_distancia = poblacion_w_aux[posicion_menor_distancia]
    
        p_inicial.remove(individuo_menor_distancia)



    p_reemplazada = p_inicial + p_elitista + p_mutada
    funcionObjetivo(p_reemplazada, tipo)
   

    if maximiza_miniza==1:  #Maximiza
        p_reemplazada = sorted(p_reemplazada, key=lambda ind: ind.getFitness(), reverse=True) 
       
    
    elif maximiza_miniza==-1: #Minimiza
        p_reemplazada = sorted(p_reemplazada, key=lambda ind: ind.getFitness(), reverse=False) 
      

    return p_reemplazada


def reemplazoPeorEntreSemejantes(p_inicial, p_mutada, elitismo, n_parecidos, maximiza_miniza, tipo):

    n_individuos_elitistas=0
    if elitismo>0:
        n_individuos_elitistas=int(round((elitismo*len(p_inicial))/100, 0))

    p_elitista=[]
    p_reemplazada=[]

    if maximiza_miniza==1: 
        p_inicial = sorted(p_inicial, key=lambda ind: ind.getFitness(), reverse=True) 
        p_elitista=p_inicial[0:n_individuos_elitistas]

        for i in range(0,n_individuos_elitistas):
            p_inicial.remove(p_elitista[i])

    elif maximiza_miniza==-1:
        p_inicial = sorted(p_inicial, key=lambda ind: ind.getFitness(), reverse=False) 
        p_elitista=p_inicial[0:n_individuos_elitistas]

        for i in range(0,n_individuos_elitistas):
            p_inicial.remove(p_elitista[i])


    
    for ind_m in p_mutada:

       
        poblacion_ordenada_por_distancia = sorted(p_inicial, key=lambda ind: distancia(ind_m, ind, tipo), reverse=False) 

        lista_mas_parecidos=poblacion_ordenada_por_distancia[0:n_parecidos]
        

        if maximiza_miniza==1: 
            peor=min(lista_mas_parecidos, key=lambda ind: ind.getFitness())
            p_inicial.remove(peor)
        

        elif maximiza_miniza==-1:
            peor=max(lista_mas_parecidos, key=lambda ind: ind.getFitness())
            p_inicial.remove(peor)
        
    

    p_reemplazada = p_inicial + p_elitista + p_mutada
    funcionObjetivo(p_reemplazada, tipo)


    if maximiza_miniza==1:  #Maximiza
        p_reemplazada = sorted(p_reemplazada, key=lambda ind: ind.getFitness(), reverse=True) 
       
    
    elif maximiza_miniza==-1: #Minimiza
        p_reemplazada = sorted(p_reemplazada, key=lambda ind: ind.getFitness(), reverse=False) 
      
    
    return p_reemplazada


def reemplazoCrowdingDeterministicoDC(p_inicial, p_mutada, elitismo, maximiza_miniza, tipo):
   
    n_individuos_elitistas=0
    if elitismo>0:
        n_individuos_elitistas=int(round((elitismo*len(p_inicial))/100, 0))

    p_elitista=[]
    p_reemplazada=[]

    if maximiza_miniza==1: 
        p_inicial = sorted(p_inicial, key=lambda ind: ind.getFitness(), reverse=True) 
        p_elitista=p_inicial[0:n_individuos_elitistas]

        for i in range(0,n_individuos_elitistas):
            p_inicial.remove(p_elitista[i])

    elif maximiza_miniza==-1:
        p_inicial = sorted(p_inicial, key=lambda ind: ind.getFitness(), reverse=False) 
        p_elitista=p_inicial[0:n_individuos_elitistas]

        for i in range(0,n_individuos_elitistas):
            p_inicial.remove(p_elitista[i])

    p_inicial_aux=[]
    for ind_i in p_inicial:
        p_inicial_aux.append(ind_i.getGenes())
    
    cont=0
    for ind_m in p_mutada:
        
        print(cont)
        cont=cont+1
        genesPadre1=ind_m.getGenesPadre1()
        genesPadre2=ind_m.getGenesPadre2()

        padre1 = Individuo(genesPadre1,0)
        padre2 = Individuo(genesPadre2,0)

        padres = [padre1, padre2]

        funcionObjetivo(padres, tipo)

        distancia_p1 = distancia(ind_m, padres[0],tipo)
        distancia_p2 = distancia(ind_m, padres[1],tipo)

        if distancia_p1<=distancia_p2:
           
           if padres[0].getGenes() in p_inicial_aux:
              
                for i in range(len(p_inicial_aux)):
                    if p_inicial_aux[i]==padres[0].getGenes():
                        
                        p_inicial_aux.pop(i)
                        p_inicial.pop(i)
                        break       

           elif padres[0].getGenes() not in p_inicial_aux and  padres[1].getGenes() in p_inicial_aux:
                
                for i in range(len(p_inicial_aux)):
                    if p_inicial_aux[i]==padres[1].getGenes():
                       
                        p_inicial_aux.pop(i)
                        p_inicial.pop(i)
                        break   

           elif padres[0].getGenes() not in p_inicial_aux and padres[1].getGenes() not in p_inicial_aux:
                
                num_random=random.randint(0, len(p_inicial_aux)-1)

                p_inicial_aux.pop(num_random)
                p_inicial.pop(num_random)
               
               

        else:

            if padres[1].getGenes() in p_inicial_aux:

                for i in range(len(p_inicial_aux)):
                    if p_inicial_aux[i]==padres[1].getGenes():
                      
                        p_inicial_aux.pop(i)
                        p_inicial.pop(i)
                        break      

            elif padres[1].getGenes() not in p_inicial_aux and  padres[0].getGenes() in p_inicial_aux:
                
                for i in range(len(p_inicial_aux)):
                    if p_inicial_aux[i]==padres[0].getGenes():
                        
                        p_inicial_aux.pop(i)
                        p_inicial.pop(i)
                        break   

            elif padres[1].getGenes() not in p_inicial_aux and padres[0].getGenes() not in p_inicial_aux:
              
                num_random=random.randint(0, len(p_inicial_aux)-1)

            
                p_inicial_aux.pop(num_random)
                p_inicial.pop(num_random)
        
 
    p_reemplazada = p_inicial + p_elitista + p_mutada
    funcionObjetivo(p_reemplazada, tipo)


    if maximiza_miniza==1:  #Maximiza
        p_reemplazada = sorted(p_reemplazada, key=lambda ind: ind.getFitness(), reverse=True) 
       
    
    elif maximiza_miniza==-1: #Minimiza
        p_reemplazada = sorted(p_reemplazada, key=lambda ind: ind.getFitness(), reverse=False) #
      
    
    return p_reemplazada




#------------------------------------INICIALIZACION VARIABLES------------------------------------------------------------------------

poblacion_inicial=[]   
poblacion_seleccionada=[]
poblacion_cruzada=[]

#--------------------------------------------MAIN------------------------------------------------------------------------------------

print('-----------------------BINARIA---------------------------')


poblacion_inicial=funcionObjetivo(generaPoblacionBinaria(100,10), 'BINARIO') 
copia_poblacion_inicial_para_reemplazo = copy.deepcopy(poblacion_inicial)
copia_poblacion_inicial2 = copy.deepcopy(poblacion_inicial)

'''MAXIMIZANDO'''

#poblacion_seleccionada=seleccionTorneo(poblacion_inicial, 50,3,1) #(poblacion, n_seleccionados_total, n_participantes_en_pelea, minimiza_o_maximiza)
#poblacion_seleccionada=seleccionOrdenLineal(poblacion_inicial, 50, 1)

#poblacion_seleccionada=seleccionEmparejamientoVariadoInversoNAM(poblacion_inicial, 50, 6, 'BINARIO') #pob, seleccionados y N en torneo
#poblacion_seleccionada=seleccionRuleta(poblacion_inicial, 50, 1)

#poblacion_cruzada=cruceBinario(poblacion_seleccionada, 30, 2,0.7) #poblacion, n_cruces, probabilidad

#poblacion_mutada=mutacionBinaria(poblacion_cruzada,0.2,0.2) #poblacion, probabilidad_individuo, probabilidad_gen

#poblacion_reemplazada=reemplazoPeorRW(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 1, 'BINARIO') #p_inicial, p_mutada, elitismo, maximiza_miniza, tipo
#poblacion_reemplazada=reemplazoTorneoRestringuidoTRS(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 3, 1, 'BINARI0')
#poblacion_reemplazada=reemplazoPeorEntreSemejantes(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 3, 1, 'BINARI0')
#poblacion_reemplazada=reemplazoCrowdingDeterministicoDC(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 1, 'BINARI0')

#iteraciones(poblacion_reemplazada, 'no', 0, 50, 'si', 500, 1) #poblacion_reemplazada, si_hay_referencia, valor_fitness_referencia, max_iteraciones_sin_mejorar, si_hay_max_iteraciones, max_iteraciones, maximiza_minimiza





'''MINIMIZANDO'''

#poblacion_seleccionada=seleccionTorneo(poblacion_inicial, 50,3,-1) #(poblacion, n_seleccionados_total, n_participantes_en_pelea, minimiza_o_maximiza)
#poblacion_seleccionada=seleccionOrdenLineal(poblacion_inicial, 50, -1)

#poblacion_seleccionada=seleccionEmparejamientoVariadoInversoNAM(poblacion_inicial, 50, 6, 'BINARIO') #pob, seleccionados y N en torneo
#poblacion_seleccionada=seleccionRuleta(poblacion_inicial, 50, -1)

#poblacion_cruzada=cruceBinario(poblacion_seleccionada, 30, 2,0.7) #poblacion, n_cruces, probabilidad

#poblacion_mutada=mutacionBinaria(poblacion_cruzada,0.2,0.2) #poblacion, probabilidad_individuo, probabilidad_gen

#poblacion_reemplazada=reemplazoPeorRW(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, -1, 'BINARIO') #p_inicial, p_mutada, elitismo, maximiza_miniza, tipo
#poblacion_reemplazada=reemplazoTorneoRestringuidoTRS(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 3, -1, 'BINARI0')
#poblacion_reemplazada=reemplazoPeorEntreSemejantes(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 3, -1, 'BINARI0')
#poblacion_reemplazada=reemplazoCrowdingDeterministicoDC(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, -1, 'BINARI0')

#iteraciones(poblacion_reemplazada, 'no', 0, 50, 'si', 500, -1) #poblacion_reemplazada, si_hay_referencia, valor_fitness_referencia, max_iteraciones_sin_mejorar, si_hay_max_iteraciones, max_iteraciones, maximiza_minimiza


pob=[]
mostrar_poblacion(mochila(pob))