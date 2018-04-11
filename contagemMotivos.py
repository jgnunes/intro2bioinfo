

def contagem(matriz):
    num_sequencias = len(matriz)
    num_colunas = len(matriz[0])
    
    # essa lista de listas contera as frequencias, coluna a coluna, 
    # de cada um dos 4 nucleotideos. Em ordem: A, T, C, G
    frequencia_nucleotideos = [[],[],[],[]]
    for j in frequencia_nucleotideos:
        for i in range(num_colunas):
            j.append(0)
    
    for coluna in range(num_colunas):
        for sequencia in range(num_sequencias):
                if matriz[sequencia][coluna] == 'A':
                    frequencia_nucleotideos[0][coluna] += 1
                elif matriz[sequencia][coluna] == 'T':
                    frequencia_nucleotideos[1][coluna] += 1
                elif matriz[sequencia][coluna] == 'C':
                    frequencia_nucleotideos[2][coluna] += 1
                elif matriz[sequencia][coluna] == 'G':
                    frequencia_nucleotideos[3][coluna] += 1
    

    return frequencia_nucleotideos

if __name__ == "__main__":

    frequencia_nucleotideos = contagem(["TTGGGGACTT","TTGCATAGGT","TTGGGGTATT","TTAAGGAAAT"])

    c = 0
    for nucleotideo in frequencia_nucleotideos:
        if c ==0:
            print('A:', nucleotideo)
        if c ==1:
            print('T:', nucleotideo)
        if c ==2:
            print('C:', nucleotideo)
        if c ==3:
            print('G:', nucleotideo)
            
        c +=1
