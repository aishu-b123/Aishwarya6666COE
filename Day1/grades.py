p=int(input('project score'))
i=int(input('internal score'))
e=int(input('external score'))


if (p >=50 and i >=50 and e >=50):
    total = ((70 / p ) * 100) + ((10 / i ) * 100) +((20 / e ) * 100)
    print(total)
    if total>=90:
        print('A')
    elif total>80:
        print('B')
    else:
        print('C')
else:
    if p<50:
        print('failed in project and score is:' , p)
    if e<50:
        print('failed in external and score is' , e)
    if i<50:
        print('failed in internal and score is' , i)