salary=int(input('Enter your salary'))
hra=0
da=0
if (salary<10000):
    gross = ((67 / 100) * salary)+((73 / 100) * salary)+salary
elif (salary<20000):
    gross = ((69 / 100) * salary) + ((76 / 100) * salary) + salary
else :
    gross = ((73 / 100) * salary) + ((81/ 100) * salary) + salary
print(gross)