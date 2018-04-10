from distanciaDeHamming import hamming
from itertools import product


def encontrarDVizinhanca(padrao,d):

    dVizinhanca = set()
    nucleotideos = ['A','T','C','G']
    
    #cria um conjunto kmers com todos os kmers possiveis
    # a funcao product retorna combinacao de nucleotideos k a k
    for i in product(nucleotideos, repeat=len(padrao)):
        kmer = "".join(i)
        if hamming(kmer, padrao) <= d:
            dVizinhanca.add(kmer)
    return dVizinhanca

if __name__ == "__main__":
    print(encontrarDVizinhanca("ATG",1))  
