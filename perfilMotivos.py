from contagemMotivos import contagem

def perfil(matriz):
    num_sequencias = len(matriz)
    matriz_contagem = contagem(matriz)

    print(matriz_contagem)
        
    for i in range(len(matriz_contagem)):
        for j in range(len(matriz_contagem[0])):
            matriz_contagem[i][j] = matriz_contagem[i][j]/float(num_sequencias)

            
    return(matriz_contagem)

if __name__ == '__main__':
    matriz_contagem = perfil(["TTGGGGACTT","TTGCATAGGT","TTGGGGTATT","TTAAGGAAAT"])
    
    c = 0
    for nucleotideo in matriz_contagem:
        if c ==0:
            print('A:', nucleotideo)
        if c ==1:
            print('T:', nucleotideo)
        if c ==2:
            print('C:', nucleotideo)
        if c ==3:
            print('G:', nucleotideo)
            
        c +=1
