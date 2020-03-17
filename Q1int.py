from random import seed
from random import randint
import random
# i=0
# while(i<10):
#     print(random.randint(0,100))
#     i=i+1
population_size=random.randrange(4,8,1)
print("Population: ",population_size)
bit_size=random.randrange(8,16,1)
print(bit_size)
i=0
population=[]
fitness=pow(2,bit_size)-1
print("Fitness Function: ",fitness)
i=0
number=''
while(i<bit_size):
    number=number+'1'
    i=i+1
print(number)
number=int(number,2)
print("Number: ",number)
number=number+1
i=0
while(i<population_size):
    num=randint(0,number)
    # seed(100)
    # print(number)
    population.append(num)
    i=i+1
print(population)
# population.pop(population.index(min(population)))
count=0
print(population)
size=len(population)-1
number1=randint(0,size)
seed(2)
number2=randint(0,size)
crossover1=bin(population[number1]).replace("0b","")
crossover2=bin(population[number2]).replace("0b","")
crossover1=str(crossover1)
crossover2=str(crossover2)
print("Cross: ",crossover1)
print("Cross: ",crossover2)
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
print("CrossOver: ",crossover1,crossover2)
print("Swap: ",swap1,swap2)        
a=2
b=0
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
print("CrossOver: ",crossover1,crossover2)        
crossover1=int(crossover1,2)
crossover2=int(crossover2,2)   
population[number1]=crossover1
population[number2]=crossover2
print(population)
    
# while True:
#     count=count+1
#     if(max(population)==fitness):
#         break
#     print(population)
#     population.pop(population.index(min(population)))
#     size=len(population)
#     number=randint(0,size)
#     population.append(population[number])
#     count=0
#     print(population)
#     size=len(population)-1
#     number1=randint(0,size)
#     seed(2)
#     number2=randint(0,size)
#     crossover1=bin(population[number1]).replace("0b","")
#     crossover2=bin(population[number2]).replace("0b","")
#     crossover1=str(crossover1)
#     crossover2=str(crossover2)
#     print("Cross: ",crossover1)
#     print("Cross: ",crossover2)
#     string=''
#     loop=bit_size-len(crossover1)
#     i=0
#     while(i<loop):
#         string=string+'0'
#         i=i+1
#     print("String: ",string)    
#     string=string+crossover1
#     crossover1=string
#     string=''
#     loop=bit_size-len(crossover2) 
#     i=0
#     while(i<loop):
#         string=string+'0'
#         i=i+1
#     print("String: ",string)    
#     string=string+crossover2
#     crossover2=string
#     swap1=''
#     swap2=''
#     a=2
#     while(a<5):
#         swap1=swap1+crossover1[a]
#         a=a+1
#     a=5
#     while(a<8):
#         swap2=swap2+crossover2[a]
#         a=a+1
#     swap1=list(swap1)
#     swap2=list(swap2)
#     crossover1=list(crossover1)
#     crossover2=list(crossover2)
#     while(a<5):
#         var=swap2[b]
#         crossover1[a]=var
#         a=a+1
#         b=b+1
#     b=0    
#     while(a<8):
#         crossover2[a]=swap1[b]
#         a=a+1
#         b=b+1

#     str1 = ""  
#     for ele in crossover1:  
#         str1 += ele
#     crossover1=str1
#     str1 = ""  
#     for ele in crossover2:  
#         str1 += ele
#     crossover2=str1
#     crossover1=int(crossover1)
#     crossover2=int(crossover2)   
#     population[number1]=crossover1
#     population[number2]=crossover2
     