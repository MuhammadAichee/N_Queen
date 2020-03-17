import random
population_size=random.randrange(4,8,1)
print("Population: ",population_size)
bit_size=random.randrange(8,16,1)
print(bit_size)
i=0
population=[]
fitness=pow(2,bit_size)-1
print("Fitnes Function: ",fitness)
while(i<population_size):
    # print("Bit size: ",bit_size)
    j=0
    original_number=''
    while(j<bit_size):
        number=random.randrange(0,2,1)
        original_number=original_number+str(number)
        # print(original_number)
        j=j+1
    population.append(original_number)
    i=i+1
print(str(population))
size=len(population)
i=1
minimum=int(population[0])
index=0
while(i<size):
    number=int(population[i])
    if(number<minimum):
        minimum=number
        index=i
    i=i+1    
print("minimum: ",str(minimum))
print("Index: ",index)
i=1
maximum=int(population[0])
index=0
while(i<size):
    number=int(population[i])
    if(number>maximum):
        maximum=number
        index=i
    i=i+1    
print("maximum: ",str(maximum))
print("Index: ",index)

# while True:
#     duplicate_list=population
#     print("Duplicate List")    
#     print(duplicate_list)
#     size=len(duplicate_list)
#     minimum=min(population_size)
#     print(minimum)
    