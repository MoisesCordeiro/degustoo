class Cnpj:

	lista_validacao_um = [5,4,3,2,9,8,7,6,5,4,3,2]
	lista_validacao_dois = [6,5,4,3,2,9,8,7,6,5,4,3,2]

	def __init__(self):
		pass

	def validate(self, cnpj):
		# limpando cnpj
		cnpj = cnpj.replace("-","")
		cnpj = cnpj.replace(".","")
		cnpj = cnpj.replace("/","")

		# digitos verificadores
		verificadores = cnpj[-2:]

		# verificando comprimento
		if len(cnpj) != 14:
			return False

		# calculando o primeiro digito
		soma = 0
		id = 0
		for numero in cnpj:
			# evita erros de indice
			try:
				self.lista_validacao_um[id]
			except:
				break

			soma += int(numero) * int(self.lista_validacao_um[id])
			id += 1

		soma = soma % 11
		if soma < 2:
			digito_um = 0
		else:
			digito_um = 11 - soma

		# conventendo digito para string
		digito_um = str(digito_um)

		# calculando o segundo digito
		soma = 0
		id = 0
		for numero in cnpj:
			# evitando erros de indice
			try:
				self.lista_validacao_dois[id]
			except:
				break

			soma += int(numero) * int(self.lista_validacao_dois[id])

		soma = soma % 11
		if soma < 2:
			digito_dois = 0
		else:
			digito_dois = 11 - soma

		# convertendo digito para string
		digito_dois = str(digito_dois)

		# verificando se digitos verificadores
		return bool(verificadores == digito_um + digito_dois)

	def format(self, cnpj):
		return "%s.%s.%s/%s-%s" % (cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])