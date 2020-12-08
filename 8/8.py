#Open acc file
with open('8/acc') as file:
    acclist = list(file.read().splitlines())

i=0
accumulator=0
besucht=[]

while True:
    if(i in besucht):
        print(i)
        print(accumulator)
        break
    besucht.append(i)
    operations = acclist[i].split(' ')
    if(operations[0]=='acc'):
        accumulator+=int(operations[1])
        i+=1
    if(operations[0]=='jmp'):
        i+=(int(operations[1]))
    if(operations[0]=='nop'):
        i+=1

