from random import seed
from random import randint
from datetime import datetime
import random
import time
population_size=random.randrange(4,8,1)
bit_size=random.randrange(8,16,1)
i=0
population=[]
fitness=pow(2,bit_size)-1
i=0
number=''
while(i<bit_size):
    number=number+'1'
    i=i+1
number=int(number,2)
number=number+1
i=0
while(i<population_size):
    seed(datetime.now().time())
    num=randint(0,number)
    time.sleep(0.2)
    seed(datetime.now().time())
    population.append(num)
    i=i+1
    seed(datetime.now().time())
count=0
print("Initial Population: ",population)
while True:
    count=count+1
    number1=0
    number2=0
    string=''
    str1=''
    crossover1=''
    crossover2=''
    loop=0
    if(max(population)==fitness):
        break
    # print("Popuation",population)
    # print("Maximum: ",max(population))
    # print("Fitness: ",fitness)
    population.pop(population.index(min(population)))
    size=len(population)-1
    seed(datetime.now().time())
    number=randint(0,size)
    population.append(population[number])
    # count=0
    size=len(population)-1
    seed(datetime.now().time())
    number1=randint(0,size)
    seed(datetime.now().time())
    number2=randint(0,size)
    seed(datetime.now().time())
    # print("For CrossOver: ",number1)
    # print("For CrossOver: ",number2)
    crossover1=bin(population[number1]).replace("0b","")
    crossover2=bin(population[number2]).replace("0b","")
    crossover1=str(crossover1)
    crossover2=str(crossover2)
    string=''
    loop=bit_size-len(crossover1)
    i=0
    while(i<loop):
        string=string+'0'
        i=i+1
    # print("String: ",string)    
    string=string+crossover1
    crossover1=string
    string=''
    loop=bit_size-len(crossover2) 
    i=0
    while(i<loop):
        string=string+'0'
        i=i+1
    # print("String: ",string)    
    string=string+crossover2
    crossover2=string
    swap1=''
    swap2=''
    a=2
    while(a<5):
        swap1=swap1+crossover1[a]
        a=a+1
    a=5
    while(a<8):
        swap2=swap2+crossover2[a]
        a=a+1
    swap1=list(swap1)
    swap2=list(swap2)
    crossover1=list(crossover1)
    crossover2=list(crossover2)
    while(a<5):
        var=swap2[b]
        crossover1[a]=var
        a=a+1
        b=b+1
    b=0    
    while(a<8):
        crossover2[a]=swap1[b]
        a=a+1
        b=b+1

    str1 = ""  
    for ele in crossover1:  
        str1 += ele
    crossover1=str1
    str1 = ""  
    for ele in crossover2:  
        str1 += ele
    crossover2=str1
    # crossover1=int(crossover1)
    # crossover2=int(crossover2)
    # print("CrossOver: ",crossover1)
    # print("CrossOver: ",crossover2)   
    population[number1]=int(crossover1,2)
    population[number2]=int(crossover2,2)
    size=len(population)-1
    seed(datetime.now().time())
    # print("Size",size)
    number1=randint(0,size)
    # print("Number1: ",number1)
    seed(datetime.now().time())
    range1=bit_size-1
    number2=randint(0,range1)
    seed(datetime.now().time())
    # print("Mutation to be: ",number2)
    # print("BitSize: ",bit_size)
    # print("Population[number1]: ",int(population[number1]))
    var=bin(population[number1]).replace("0b","")
    # print(var)
    string=''
    # print("Length: ",len(var))
    # print("Bit_size: ",bit_size)
    loop=bit_size-len(var)
    # print("Loop: ",loop)
    i=0
    while(i<loop):
        string=string+'0'
        i=i+1
    # print("String: ",string)    
    string=string+var
    var=string
    # print("Var: ",var)
    var=list(var)
    if(var[number2]=='0'):
        var[number2]='1'
    else:
        var[number2]='0'
    str1 = ""  
    for ele in var:  
        str1 += ele
    var=str1
    # print(var)        
    # print(type(var))
    var=int(var,2)
    # print(var)
    population[number1]=var
    # print("Count: ",count)
print("Loop Count: ",count)
print("Population: ",population)
print("Digits in each Population: ",bit_size)
print("Population Size: ", len(population)+1)
print("Fitness Function: ",fitness)    