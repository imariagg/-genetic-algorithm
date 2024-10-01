
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
        
        #poblacion_seleccionada=seleccionTorneo(copia_poblacion_inicial2, 30, 4, 1)
        #poblacion_seleccionada=seleccionOrdenLineal(copia_poblacion_inicial2, 30, 1)
        poblacion_seleccionada=seleccionEmparejamientoVariadoInversoNAM(copia_poblacion_inicial2, 30, 6,'REAL')#pob, seleccionados y N en torneo
        #poblacion_seleccionada=seleccionRuleta(copia_poblacion_inicial2, 30, 1)


        #poblacion_cruzada=cruceRealAritmetico(poblacion_seleccionada,7,0.7, redondeo) #poblacion, n_cruces, probabilidad, redondeo
        poblacion_cruzada=cruceRealBLX(poblacion_seleccionada,7,0.3,0.7, redondeo) #el alpha es entre 0 y 1 #poblacion, n_cruces, alpha, probabilidad, redondeo


        poblacion_mutada=mutacionReal(poblacion_cruzada,0.2,0.5,redondeo) #poblacion, pobrabilidad_individuo, probabliadad_gen,redondeo


        #poblacion_reemplazada=reemplazoPeorRW(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 1, 'REAL') #p_inicial, p_mutada, elitismo, maximiza_miniza, tipo
        #poblacion_reemplazada=reemplazoTorneoRestringuidoTRS(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 5, 1,  'REAL')
        #poblacion_reemplazada=reemplazoPeorEntreSemejantes(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 5, 1,  'REAL')
        poblacion_reemplazada=reemplazoCrowdingDeterministicoDC(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 1,  'REAL')


        '''MINIMIZANDO'''

        #poblacion_seleccionada=seleccionTorneo(copia_poblacion_inicial2, 30, 4, -1)
        #poblacion_seleccionada=seleccionOrdenLineal(copia_poblacion_inicial2, 30,-1)
        #poblacion_seleccionada=seleccionEmparejamientoVariadoInversoNAM(copia_poblacion_inicial2, 30, 6, 'REAL') #pob, seleccionados y N en torneo
        #poblacion_seleccionada=seleccionRuleta(copia_poblacion_inicial2, 30, -1)


        #poblacion_cruzada=cruceRealAritmetico(poblacion_seleccionada, 7, 0.7, redondeo) #poblacion, n_cruces, probabilidad, redondeo
        #poblacion_cruzada=cruceRealBLX(poblacion_seleccionada,7,0.3,0.7, redondeo) #el alpha es entre 0 y 1 #poblacion, n_cruces, alpha, probabilidad, redondeo


        #poblacion_mutada=mutacionReal(poblacion_cruzada,0.2,0.5,redondeo) #poblacion, pobrabilidad_individuo, probabliadad_gen,redondeo


        #poblacion_reemplazada=reemplazoPeorRW(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, -1, 'REAL') #p_inicial, p_mutada, elitismo, maximiza_miniza, tipo
        #poblacion_reemplazada=reemplazoTorneoRestringuidoTRS(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 5, -1,  'REAL')
        #poblacion_reemplazada=reemplazoPeorEntreSemejantes(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 5, -1,  'REAL')
        #poblacion_reemplazada=reemplazoCrowdingDeterministicoDC(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, -1,  'REAL')

       
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

def generaPoblacionReal(tamanoPoblacion, numeroVarReales , rangoMin, rangoMax, redondeo):

    poblacion=[]

    for i in range(0,tamanoPoblacion):
        individuo = Individuo()
        genes_aux=[]
        for j in range(0, numeroVarReales):
            aux = random.uniform(rangoMin, rangoMax)
            valor = round(aux, redondeo)
            genes_aux.append(valor)
        individuo.setGenes(genes_aux)
        poblacion.append(individuo)

    return poblacion


def funcionObjetivo(poblacion, tipo):
    
    if tipo=='REAL':
        return funcionObjetivoR(poblacion)
    
def funcionObjetivoR(poblacion_inicial):

    cont=0
    poblacion_aux=[]
   
    if len(poblacion_inicial)==0:
        next
    else:
        
        #---------IMPORTANTE PARA SACAR EL REDONDEO---------
        individuo_aux=poblacion_inicial[0]

        numero=individuo_aux.getGenes()[0]
        cadena = str(numero)
        partes = cadena.split('.')
        
        if len(partes) > 1:
            num_decimales = len(partes[1])
        else:
            num_decimales = 0

        redondeo=num_decimales
        #redondeo=len(str(parte_decimal))

        #----------------------------------------------------
    '''
    for individuo in poblacion_inicial:
        genes=individuo.getGenes()
        for gen in genes:
            cont=cont+gen
            cont=round(cont,redondeo)
        individuo.setFitness(cont)
        poblacion_aux.append(individuo)
        cont=0

    '''
    for individuo in poblacion_inicial:
        cont=0
        for i in range(len(individuo.getGenes())):
            xi=individuo.getGenes()[i]

            if xi>-2 or xi<-5:
                cont=-100000
            else:
                primer_elemento=xi**4
                segundo_elemento=16*(xi**2)
                tercer_elemento=5*xi

                funcion=primer_elemento-segundo_elemento+tercer_elemento
                cont=cont+funcion

        cont=(1/2)*cont
        cont=round(cont,2)
        individuo.setFitness(cont)
       
        poblacion_aux.append(individuo)


    return poblacion_aux


def distanciaR(individuo1,individuo2):
    #Euclidea
    genes_indiv1=individuo1.getGenes()
    genes_indiv2=individuo2.getGenes()
    distancia=0

    for gen in range(len(genes_indiv1)):
        if genes_indiv1[gen]!=genes_indiv2[gen]:
            distancia=distancia + abs(genes_indiv1[gen]-genes_indiv2[gen])
            
    return distancia

def distancia(individuo1, individuo2, tipo):
    
    if tipo=='REAL':
        return distanciaR(individuo1, individuo2)
    
    

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
        poblacion_aux.remove(seleccionado1) 
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
        poblacion_aux.remove(seleccionado2)
       
    return seleccionados






def seleccionRuleta(poblacion, n_seleccionados_total, minimiza_o_maximiza):
    
    poblacion_aux=poblacion
    lista_fitnesses=[]
    #Sacar fitness maximo 
    for individuo in poblacion_aux:
        lista_fitnesses.append(individuo.getFitness())

        if minimiza_o_maximiza == 1:
            max_fitness=max(poblacion_aux, key=lambda parti: parti.getFitness()).getFitness()
            min_fitness=min(poblacion_aux, key=lambda parti: parti.getFitness()).getFitness()
            #max_fitness=0
            #f (individuo.getFitness()>max_fitness):
                #max_fitness=individuo.getFitness()
                #max_fitness=print(max(poblacion_aux, key=lambda parti: parti.getFitness()).getFitness())
        
        elif minimiza_o_maximiza == -1:
            max_fitness=max(poblacion_aux, key=lambda parti: parti.getFitness()).getFitness() #Sigue min_fitness
            min_fitness=min(poblacion_aux, key=lambda parti: parti.getFitness()).getFitness()
            
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

    if 0 in probabilidades:
        for p in range(len(probabilidades)):
            if probabilidades[p]<2.348539710359483e-309:
                probabilidades[p]=2.348539710359483e-309


  

    seleccionados=[]
    for i in range(n_seleccionados_total):

        ind_seleccionado = random.choices(range(len(poblacion_aux)), weights=probabilidades, k=1)[0]
        
        seleccionado=poblacion_aux[ind_seleccionado]
        seleccionados.append(seleccionado)
        del poblacion_aux[ind_seleccionado]
        del probabilidades[ind_seleccionado]
        
    return seleccionados

#---------------------------------------------CRUCES---------------------------------------------------------------------------------

def cruceRealAritmetico(poblacion, n_cruces, probabilidad, redondeo):

    poblacion_aux=poblacion
    cruzados=[]
 
    
    for k in range(0, n_cruces):
        probabilidad_aux = random.random()
        if probabilidad>probabilidad_aux:
            padre1=random.choices(poblacion)[0]
            padre2=random.choices(poblacion)[0]

            hijo=Individuo([],0)
            genHijo=0
            genesHijo=[]
            
            #Generar hijo:
            for i in range(len(padre1.getGenes())):
                xi=padre1.getGenes()[i]
                yi=padre2.getGenes()[i]
                genHijo=(xi+yi)/2
                genHijo=round(genHijo,redondeo)
                genesHijo.append(genHijo)

            hijo.setGenes(genesHijo)
            hijo.setGenesPadre1(padre1.getGenes())
            hijo.setGenesPadre2(padre2.getGenes())
            cruzados.append(hijo)


    funcionObjetivo(cruzados, 'REAL')
    return cruzados


def cruceRealBLX(poblacion, n_cruces, alpha, probabilidad, redondeo):
#Alpha es el mismo para todos los genes y tiene que ser entre 0 y 1

    poblacion_aux=poblacion
    cruzados=[]

    
    for k in range(0, n_cruces):
        probabilidad_aux = random.random()
        if probabilidad>probabilidad_aux:
            padre1=random.choices(poblacion)[0]
            padre2=random.choices(poblacion)[0]

            hijo=Individuo([],0)
            genHijo=0
            genesHijo=[]
            
            #Generar hijo:
            for i in range(len(padre1.getGenes())):
                xi=padre1.getGenes()[i]
                yi=padre2.getGenes()[i]
                a=xi-(alpha*(yi-xi))
                b=yi+(alpha*(yi-xi))
                
                if a>b:
                    a, b = b, a

                genHijo=random.uniform(a,b)
                genHijo=round(genHijo,redondeo)
                genesHijo.append(genHijo)

            hijo.setGenes(genesHijo)
            hijo.setGenesPadre1(padre1.getGenes())
            hijo.setGenesPadre2(padre2.getGenes())
            cruzados.append(hijo)


    funcionObjetivoR(cruzados)
    return cruzados

    

#--------------------------------------------MUTACIÓN---------------------------------------------------------------------------------
          
def mutacionReal(poblacion, pobrabilidad_individuo, probabliadad_gen,redondeo):
    poblacion_aux=[]
    poblacion_aux=poblacion
    
    for individuo in poblacion_aux:
        probabilidad_individuo_aux=random.random()
        if probabilidad_individuo_aux < pobrabilidad_individuo:
            #Se hace la mutacion
            desviacion_tipica=statistics.stdev(individuo.getGenes())
            
            for it in range(len(individuo.getGenes())): 
                probabilidad_gen_aux=random.random()
                
                if probabilidad_gen_aux < probabliadad_gen:
                    valor_mutacion = random.gauss(0, desviacion_tipica)
                    valor_mutacion=round(valor_mutacion,redondeo)
                    individuo.getGenes()[it]= round(individuo.getGenes()[it]+valor_mutacion,redondeo)

    funcionObjetivoR(poblacion_aux)
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
    #Se reemplaza al mas parecido de entre w (w=3, ...). Mantiene una cierta diversidad.
    # W numero de participantes

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

#WAMS
def reemplazoPeorEntreSemejantes(p_inicial, p_mutada, elitismo, n_parecidos, maximiza_miniza, tipo):
    #Se reemplaza el peor cromosoma del conjunto de N padres más parecidos al descendiente generado (seleccionados de toda la población)
 
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

        poblacion_ordenada_por_distancia = sorted(p_inicial, key=lambda ind: distancia(ind_m, ind, tipo), reverse=False) #a la izq estan los mas parecidos, los que tienen menos distancia
        
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
    # El hijo reemplaza a su padre más parecido. Mantiene diversidad.
   
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


    #Creo una lista solo de los genes de la poblacion inicial de modo auxiliar
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
        p_reemplazada = sorted(p_reemplazada, key=lambda ind: ind.getFitness(), reverse=False) 
      
    
    return p_reemplazada



#------------------------------------INICIALIZACION VARIABLES------------------------------------------------------------------------

poblacion_inicial=[]   
poblacion_seleccionada=[]
poblacion_cruzada=[]

#--------------------------------------------MAIN------------------------------------------------------------------------------------

print('--------------------------REAL----------------------------')

redondeo=2
poblacion_inicial=funcionObjetivo(generaPoblacionReal(100, 10, -5, -2, redondeo), 'REAL')
copia_poblacion_inicial_para_reemplazo = copy.deepcopy(poblacion_inicial)
copia_poblacion_inicial2 = copy.deepcopy(poblacion_inicial)



'''MAXIMIZANDO'''

#poblacion_seleccionada=seleccionTorneo(poblacion_inicial, 50, 4, 1)
#poblacion_seleccionada=seleccionOrdenLineal(poblacion_inicial, 50,1)
poblacion_seleccionada=seleccionEmparejamientoVariadoInversoNAM(poblacion_inicial, 30, 6, 'REAL') #pob, seleccionados y N en torneo
#poblacion_seleccionada=seleccionRuleta(poblacion_inicial, 50, 1)


#poblacion_cruzada=cruceRealAritmetico(poblacion_seleccionada,7,0.7, redondeo) #poblacion, n_cruces, probabilidad, redondeo
poblacion_cruzada=cruceRealBLX(poblacion_seleccionada,7,0.3,0.7, redondeo) #el alpha es entre 0 y 1 #poblacion, n_cruces, alpha, probabilidad, redondeo


poblacion_mutada=mutacionReal(poblacion_cruzada,0.2,0.5,redondeo) #poblacion, pobrabilidad_individuo, probabliadad_gen, redondeo


#poblacion_reemplazada=reemplazoPeorRW(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 1, 'REAL') #p_inicial, p_mutada, elitismo, maximiza_miniza, tipo
#poblacion_reemplazada=reemplazoTorneoRestringuidoTRS(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 5, 1,  'REAL')
#poblacion_reemplazada=reemplazoPeorEntreSemejantes(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 3, 1,  'REAL')
poblacion_reemplazada=reemplazoCrowdingDeterministicoDC(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 1,  'REAL')

iteraciones(poblacion_reemplazada, 'no', 0, 50, 'si', 500, 1) #poblacion_reemplazada, si_hay_referencia, valor_fitness_referencia, max_iteraciones_sin_mejorar, si_hay_max_iteraciones, max_iteraciones, maximiza_minimiza




'''MINIMIZANDO'''

#poblacion_seleccionada=seleccionTorneo(poblacion_inicial, 50, 4, -1)
#poblacion_seleccionada=seleccionOrdenLineal(poblacion_inicial, 50,-1)
#poblacion_seleccionada=seleccionEmparejamientoVariadoInversoNAM(poblacion_inicial, 30, 6, 'REAL') #pob, seleccionados y N en torneo
#poblacion_seleccionada=seleccionRuleta(poblacion_inicial, 50, -1)


#poblacion_cruzada=cruceRealAritmetico(poblacion_seleccionada,7,0.7, redondeo) #poblacion, n_cruces, probabilidad, redondeo
#poblacion_cruzada=cruceRealBLX(poblacion_seleccionada,7,0.3,0.7, redondeo) #el alpha es entre 0 y 1 #poblacion, n_cruces, alpha, probabilidad, redondeo


#poblacion_mutada=mutacionReal(poblacion_cruzada,0.2,0.5,redondeo) #poblacion, pobrabilidad_individuo, probabliadad_gen,redondeo


#poblacion_reemplazada=reemplazoPeorRW(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, -1, 'REAL') #p_inicial, p_mutada, elitismo, maximiza_miniza, tipo
#poblacion_reemplazada=reemplazoTorneoRestringuidoTRS(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 5, -1,  'REAL')
#poblacion_reemplazada=reemplazoPeorEntreSemejantes(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, 3, -1,  'REAL')
#poblacion_reemplazada=reemplazoCrowdingDeterministicoDC(copia_poblacion_inicial_para_reemplazo, poblacion_mutada, 10, -1,  'REAL')

#iteraciones(poblacion_reemplazada, 'no', 0, 50, 'si', 500, -1) #poblacion_reemplazada, si_hay_referencia, valor_fitness_referencia, max_iteraciones_sin_mejorar, si_hay_max_iteraciones, max_iteraciones, maximiza_minimiza

