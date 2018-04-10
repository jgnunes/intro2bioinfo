from itertools import product
from distanciaDeHamming import hamming
from dVizinhanca import encontrarDVizinhanca


def enumerarMotivos(colecao, k,d):
    """Dada uma colecao de strings de DNA, identificar os kmers
    que aparecem com no maximo d mismatches em todas strings da
    colecao"""

    tamanho_colecao = len(colecao)
    kmers = {}
    nucleotideos = ['A','T','C','G']
    
    #cria um conjunto kmers com todos os kmers possiveis
    #a funcao product retorna combinacao de nucleotideos k a k
    for i in product(nucleotideos, repeat=k):
        kmer = "".join(i)
        kmers[kmer] = 0

    for kmer in kmers:
        for string_dna in colecao:
            for i in range(len(string_dna)-k+1):
                padrao = string_dna[i:i+k]
                if kmer in encontrarDVizinhanca(padrao, d):
                    kmers[kmer] += 1
                    break

    for kmer in kmers:
        if kmers[kmer] == 4:
            print(kmer, kmers[kmer])
        
        
    
if __name__ == "__main__":
    enumerarMotivos(("ATTTGGC","TGCCTTA","CGGTATC", "GAAAATT"), 3, 1)
                 
    
