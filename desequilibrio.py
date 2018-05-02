def desequilibrio(genoma):
	"""Toma um genoma e calcula o desequilibrio (diferenca de frequencia 
	entre G e C) a cada 100000 nucleotideos"""

	desequilibrio = 0
	desequilibrio_por_posicao = []
	c = 0
	for nucleotideo in genoma:
		if nucleotideo == "G":
			desequilibrio = desequilibrio + 1
		elif nucleotideo == "C":
			desequilibrio = desequilibrio - 1
		if c%100000 == 0:
			desequilibrio_por_posicao.append(desequilibrio)

	return desequilibrio_por_posicao
