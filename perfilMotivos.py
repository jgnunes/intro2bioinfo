from contagemMotivos import contagem

def perfil(matriz):
    num_sequencias = len(matriz)
    matriz_contagem = contagem(matriz)
        
    for i in matriz_contagem:
        for j in i:
            j = float(j)/num_sequencias
            
    return(matriz_contagem)

print(perfil(["TTGGGGACTT","TTGCATAGGT","TTGGGGTATT","TTAAGGAAAT"]))
