def descobrir_agregados(L,t,k,genoma):
	kmers = {}
	agregados = []
	for i in range(len(genoma)- L + 1):
		janela = genoma[i:i+L]
		for j in range(len(janela) - k + 1):
			kmer = janela[j:j+k]
			kmer_rev = compReverso(kmer)
			if kmer not in kmers:
				kmers[kmer] = 1
			else:
				kmers[kmer] += 1
			if kmer_rev not in kmers:
				kmers[kmer_rev] = 1
			else:
				kmers[kmer_rev] += 1
			#print(kmers)
		for l in kmers:
			#print(l, kmers[l])
			if kmers[l] >= t:
				agregados.append((l,kmers[l],i))
		kmers = {}
	return agregados
