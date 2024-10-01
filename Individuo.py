class Individuo:
    def __init__(self, genes_=None, fitness_=None, genesPadre1_ = None, genesPadre2_ = None, prob_seleccionOrdenLineal_=None):
        self.genes = genes_
        self.fitness = fitness_
        self.genesPadre1 = genesPadre1_
        self.genesPadre2 = genesPadre2_
        self.prob_seleccionOrdenLineal = prob_seleccionOrdenLineal_

    def getGenes(self):
        return self.genes

    def setGenes(self, new_genes):
        self.genes = new_genes

    def getFitness(self):
        return self.fitness
    
    def setFitness(self, new_fitness):
        self.fitness = new_fitness

    def getGenesPadre1(self):
        return self.genesPadre1

    def setGenesPadre1(self, new_genesPadre1):
        self.genesPadre1 = new_genesPadre1

    def getGenesPadre2(self):
        return self.genesPadre2

    def setGenesPadre2(self, new_genesPadre2):
        self.genesPadre2 = new_genesPadre2


    def getProb_seleccionOrdenLineal(self):
        return self.prob_seleccionOrdenLineal

    def setProb_seleccionOrdenLineal(self, new_prob_seleccionOrdenLineal):
        self.prob_seleccionOrdenLineal = new_prob_seleccionOrdenLineal

    def mostrar(self):
        print('Genes: {}, Fitness: {}'.format(self.genes, self.fitness))


