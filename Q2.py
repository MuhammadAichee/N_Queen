# def checkRow(i,j,visited,rowcol):
#     a=0
#     b=j
#     flag=0
#     while(a<rowcol):
#         if(visited[a][b]==1):
#             flag=1
#             break
#         a=a+1
#     print("value of a: ",a)        
#     return flag
def checkDiagonal(i,j,visited,rowcol):
    a=i
    b=j
    flag=0
    while(b<rowcol and a<rowcol):
        # print("Value of a and b: ",a,b,"Visited: ",visited[a][b])
        if(visited[a][b]==1):
            flag=1
            break
        b=b+1
        a=a+1
    a=i
    b=j
    while(a>=0 and b>=0):
        # print("Value of a and b: ",a,b,"Visited: ",visited[a][b])
        if(visited[a][b]==1):
            flag=1
            break
        b=b-1
        a=a-1        
    a=i
    b=j
    while(b<rowcol and a>=0):
        # print("Value of a and b: ",a,b,"Visited: ",visited[a][b])
        if(visited[a][b]==1):
            flag=1
            break
        b=b+1
        a=a-1
    a=i
    b=j
    while(a<rowcol and b>=0):
        # print("Value of a and b: ",a,b,"Visited: ",visited[a][b])
        if(visited[a][b]==1):
            flag=1
            break
        b=b-1
        a=a+1
    return flag


def checkCol(i,j,visited,rowcol):
    a=i
    b=0
    flag=0
    while(b<rowcol):
        if(visited[a][b]==1):
            flag=1
            break
        b=b+1    
    return flag

# def markCol(i,j,visited,rowcol):
#     b=j
#     a=0
#     while(a<rowcol):
#         visited[a][b]=1
        # a=a+1

def markRow(i,j,visited,rowcol):
    b=0
    a=i
    while(b<rowcol):
        visited[a][b]=1
        b=b+1               
         
def markDiagonal(i,j,visited,rowcol):
    b=i
    a=j
    while(b<rowcol or a<rowcol):
        visited[a][b]=1
        b=b+1               
        a=a+1
    a=i
    b=i
    while(a>=0 or b>=0):
        visited[a][b]=1
        a=a-1
        b=b-1
            
rowcol=input("Enter size of Matrix: ")
rowcol=int(rowcol)
stack=[]
array=[]
false_position=[]
visited = [[0 for x in range(rowcol)] for y in range(rowcol)] 
Matrix = [[0 for x in range(rowcol)] for y in range(rowcol)]
# for j in range (rowcol):
#     print("For Jth column: ",j)
#     for i in range (rowcol):
i=0
j=0
while(j<rowcol):
    # print("For Jth column: ",j)
    while(i<rowcol):
        if(j not in array):
            # print("---------------------\nChecking for ",i,j,"\n")
            checkdiagonal=checkDiagonal(i,j,visited,rowcol)
            checkcol=checkCol(i,j,visited,rowcol)
            if(checkcol==0 and checkdiagonal==0):
                Matrix[i][j]=1
                visited[i][j]=1
                stack.append((i,j))
                # print("Marking value: ",i,j)
                array.append(j)
                break
        i=i+1        
    # print("Array: ",array)
    # print("False Position: ",false_position)
    a=len(array)
    # print("Value of j in line 124: ",j)
    if(array[a-1]!=j):
        # print("a-1: ", array[a-1]," j: ",j)
        false_i, false_j= stack.pop()
        # print("if ke ander: ",false_i,false_j)
        Matrix[false_i][false_j]=0
        visited[false_i][false_j]=0
        array.pop()
        i=false_i+1
        j=false_j                
    else:
        j=j+1
        i=0    
# for i in range (rowcol):
#     for j in range (rowcol):
#         print(Matrix[i][j],end=" ")
#     print("\n")               

# print("----------------")

for i in range (rowcol):
    for j in range (rowcol):
        if(visited[i][j]==1):
            visited[i][j]='Q'
        else:
            visited[i][j]="#"    
        print(visited[i][j],end="  ")
    print("\n")     