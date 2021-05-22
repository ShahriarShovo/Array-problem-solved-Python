#1.Write a  program to read and print elements of array. 

""" array=[1,8,6,4,5]
print(array)
for i in range(len(array)):
    print(array[i],end=' ')
 """
#1.Write a  program to read and print elements of array. 

""" array=[]
n=int(input("Enter How many elements you want store in Array : "))

for i in range(n):
   
    a=int(input("Enter the Elements : "))
    
    array.append(a)

for i in range(len(array)):
    print(array[i],end=' ') """

#2.Write a  program to print all negative elements in an array.
""" array= []
n=int(input("Enter How many elements you want store in Array : "))
for i in range(n):
    c=int(input("Enter the Elements : "))
    array.append(c)

for j in range(len(array)):
    if array[j]<0:
        print(array[j]) """


#3.Write a  program to find sum of all array elements.
""" array= []
sum=0
n=int(input("Enter How many elements you want store in Array : "))
for i in range(n):
    c=int(input("Enter the Elements : "))
    array.append(c)
for j in range(len(array)):
    sum=sum+array[j]
print(sum) """

#4.Write a  program to find maximum and minimum element in an array.
""" 
array= []
sum=0
n=int(input("Enter How many elements you want store in Array : "))
for i in range(n):
    c=int(input("Enter the Elements : "))
    array.append(c)

print("Elements in Array : ")

for j in range(len(array)):
    print(array[j],end=' ')

max=array[0]
min=array[0]
for k in range(len(array)):
    if k>array[0]:
        max=array[k]
print("\nMaximum element in Array : ",max)

for l in range(len(array)):
    if l<array[0]:
        min=array[l]
print("\nMinimum element in Array : ",min) """

#5.Write a  program to find second largest element in an array.

""" array=[]
n=int(input("Enter the Size of Array : "))
for i in range(n):
    c=int(input("Enter the Elements in Array : "))
    array.append(c)
print("Element in Array : ")
for j in range(len(array)):
    print(array[j],end=' ')

max=array[0]
second_max=[1]

for l in range(len(array)):
    if array[l]>=max:
        second_max=max
        max=array[l]

    elif array[l]<=max and array[l]>second_max:
        second_max=array[l]

print("\nLargest number is : ",max)
print("\nSecond Largest number is : ",second_max)
     """

#6.Write a program to count total number of even and odd elements in an array.

""" array=[]
n=int(input("Enter the Size of Array : "))
for i in range(n):
    c=int(input("Enter the Elements : "))
    array.append(c)

print("Elements in Array : ")
for j in range(len(array)):
    print(array[j],end=' ')

even=0
odd=0

for l in range(len(array)):
    if array[l]%2==0:
        even=even+1
    if array[l]%2!=0:
        odd=odd+1

print("\nTotal even number in Array : ",even)
print("\nTotal odd number in Array : ",odd)
 
 """

#7.Write a program to count total number of negative elements in an array.
""" array=[]
n=int(input("Enter the size of Array : "))

negative=0

for i in range(n):
    c=int(input("Enter the Elements of Array : "))
    array.append(c)

print("Elements in Array : ")
for j in range(len(array)):
    print(array[j])

for l in range(len(array)):
    if array[l]<0:
        negative=negative+1
print("Negative elements in Array : ",negative) """


#8.Write a program to copy all elements from an array to another array.

""" array=[]

n=int(input("Enter the size of Array : "))
for i in range(n):
    c=int(input("Enter the elements : "))
    array.append(c)

copy_array=[None]*n

for i in range(0,len(array),1):

    copy_array[i]=array[i]

print("Array ---- A ")
for i in range(len(array)):
    print(array[i],end=' ')

print("\nArray ----- B ")
for i in range(len(copy_array)):
    print(copy_array[i],end=' ')  """


#9.Write a  program to insert an element in an array.

""" array=[]
n=int(input("Enter the size of Array : "))

for i in range(n):
    c=int(input("Enter the elements : "))
    array.append(c)

for i in range(len(array)):
    print(array[i],end=' ')

position = int(input("\nEnter the Position you want insert element : "))
value=int(input("\nEnter the Value : "))
array.insert(position,value)

for i in range(len(array)):
    print(array[i],end=' ')

#Second version 
array=[]
n=int(input("Enter the size of Array : "))

for i in range(n):
    c=input("Enter the elements : ")
    array.append(c)

for i in range(len(array)):
    print(array[i],end=' ')

position = int(input("\nEnter the Position you want insert element : "))
value=input("\nEnter the Value : ")
array.insert(position,value)

for i in range(len(array)):
    print(array[i],end=' ')

 """

#10.Write a program to delete an element from an array at specified position.

""" array=[]
n=int(input("Enter the size of Array : "))

for i in range(n):
    c=input("Enter the elements : ")
    array.append(c)

for i in range(len(array)):
    print(array[i],end=' ')
delete=int(input("Enter the Position : "))

array.pop(delete)

for i in range(len(array)):
    print(array[i],end=' ') """

#11.program to count frequency of each element in an array

""" array=[]
n=int(input("Enter the size of Array : "))

for i in range(n):
    c=input("Enter the elements : ")
    array.append(c)

for i in range(len(array)):
    print(array[i],end=' ')

freq_array=[None]*len(array)
visited=-1

for i in range(len(array)):
    count=1
    for j in range(i+1,len(array)):
        if array[i]==array[j]:
            count=count+1
            freq_array[j]=visited

    if freq_array[i]!=visited:

        freq_array[i]=count

#Displays the frequency of each element present in array    
print("---------------------");    
print(" Element | Frequency");    
print("---------------------");    
for i in range(0, len(freq_array)):    
    if(freq_array[i] != visited):    
        print("    " + str(array[i]) + "    |    " + str(freq_array[i]));    
print("---------------------"); 

 """

 #12.Write a  program to count total number of duplicate elements in an array.

""" array=[]
count=0
n=int(input("Enter the size of Array : "))

for i in range(n):
    c=input("Enter the elements : ")
    array.append(c)

for i in range(len(array)):
    print(array[i],end=' ')

for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]==array[j]:
           print("\nDuplicate Array is : ",array[j],end=' ')
           count=count+1
           break
print("\nTotal Duplicate Array is : ",count)

    
 """

 

#13. Separate Even and Odd numbe in Array 
'''
array=[]

n=int(input("Enter the Size of Array : "))

for i in range(n):
      c=int(input("Enter Elements : "))
      array.append(c)

even_number=[None]*len(array)
even_count=0


odd_number=[None]*len(array)
odd_count=0


for i in range(len(array)):
    if array[i] % 2==0:
        even_number[even_count]=array[i]
        even_count=even_count+1
    else:
        odd_number[odd_count]=array[i]
        odd_count=odd_count+1

print("Even :")
for e in range(even_count):
    print(even_number[e],end=' ')
print()
print("Odd : ")
for o in range(odd_count):
    print(odd_number[o],end=' ')

'''
#14.Write a  program to search an element in an array.
'''
array = []

n=int(input("Enter the size of An Array : "))

for i in range(n):
    c=int(input("Enter elements : "))
    array.append(c)
    
count=0

for i in range(len(array)):
    print(array[i],end=' ')
print()
item=int(input("Enter the Number for search : "))
print()
for j in range(len(array)):
                    if array[j]==item:
                        count=1
                        break
                        
if count==1:
    print(item,"is in array")
else:
    print(item,"is not in array")


'''
#15.Write a  program to sort array elements in ascending or descending order.
'''
array=[3,99,11,10,4,9,0]

#Ascending 
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]> array[j]:
            temp=array[i]
            array[i]=array[j]
            array[j]=temp

#Descending

for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]< array[j]:
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
           
            
            
for i in range(len(array)):
    print(array[i],end=' ')
    

'''
#16.Reverse An Array
'''
array=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(array)-1,-1,-1):
    print(array[i],end=' ')
'''
                        
 