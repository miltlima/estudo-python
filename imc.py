# Milton Lima
# IMC com IF , Elif 
peso = int(input('Informe o seu peso:' ))
altura = float(input('Informe o sua altura:' ))
imc = round(peso / (altura * altura),2)
print ('Seu IMC:', imc)
if (imc < (18.5)):
    print('você está abaixo do peso')
elif (imc >= 18.5) and (imc <= 24.9):
    print('Você esta com o peso normal')
elif (imc >= 25) and (imc <=  29.9):
    print('Você está acima do peso')
elif (imc >= 30) and (imc <= 34.9):
    print('Você está com obesidade 2')
elif (imc >= 35) and (imc <= 39.9):
    print('Você está com obesidade 3')    
elif (imc >= 40):
    print('Você está com Obesidade Morbida')            


