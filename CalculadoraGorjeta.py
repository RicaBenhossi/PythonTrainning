meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + (meal * tax)
total = meal + (meal * tip)
#Exibindo os dados na tela.
print("%.2f" % total)
print("Obrigado por usar o nosso sistema.")
