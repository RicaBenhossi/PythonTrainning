"""
Este arquivo é para lembrar alguns exemplos de comandos mais básicos de python.
Segue abaixo os comandos.
"""

"""
Strings
"""

vTexto = "Teste de string"



# Concatenação de string
print("Teste" + " de cotatenação " + "de " + "Strings")

# Concatenação/Formatação de String usado % (MELHOR JEITO)
string1 = "Camelot"
string2 = "besta"
print ("Não vamos à %s. É um lugar %s pra dedéu." % (string1, string2))

# Método também funciona com Input.
# **** O método INPUT sempre retorna STRING. É necessário converter para putro tipo se necessário.
nome = input("Qua o seu nome?  ")
idade = input("Qual a sua idade?  ")

print ("Olá %s. Bom saber que você tem %s anos de idade." % (nome, idade))

"""
Data e Hora.
"""

#Atribuindo a hora atual à uma variavél
datahora = datetime.now() 
print(datahora)

# Desmembrando a data.
print(datahora.year)
print(datahora.month)
print(datahora.day) 

# Formatando data
print("%s/%s/%s" % (datahora.day, datahora.month, datahora.year))

# Desmembrando e fomatando a hora
print("%s:%s:%s" % (datahora.hour, datahora.minute, datahora.second)) 

# Data e hora formatados.
print("%s/%s/%s %s:%s:%s" % (datahora.day, datahora.month, datahora.year, datahora.hour, datahora.minute, datahora.second))

