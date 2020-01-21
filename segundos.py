# Exercicio para praticar divisão inteira e resto da divisão.
# author:milton lima
entrada = int(input("Por favor, entre com o número de segundos que deseja converter:"))
dias = int(entrada//86400) 
segundos = entrada % 86400
horas = int(segundos//3600)
segundos = segundos % 3600
minutos = int(segundos//60)
segundos = segundos % 60
print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")