

# You are given with a number ‘n’. You have to count the pair of two numbers a and b such that sum of two numbers are equal to n.
# Note:Both numbers lie in range 1<=a,b<n

# Input Description:
# You are given a number ‘n’

# Output Description:
# Print the number of pairs satisfying above condition

# Sample Input :
# 5

# Sample Output :
# 4

n = int(input())
count = 0
for i in range(0,n):
    for j in range(0,n):
        if (i+j == n):
            count+=1
        else:
            count = count
print(count)
    



# A person saves his monthly saving according to given schema. He saves same amount of money which is equal to the money saved in immediate previous two months. 
# Assume, initially he saved 1000 rupees and in first month he saved another 1000. Your task is to tell how much he had totally saved at the end of ‘n’ months

# Input Description:
# You will be given a number ‘n’->No. of months

# Output Description:

# Print the total savings at the end of ‘n’ months

# Sample Input :
# 1

# Sample Output :
# 2000

n = int(input())
a = 1000
b = 1000
count = 2000
for i in range(0,n-1):
    c = a+b
    a = b
    b = c
    count+=c
print(count)
        



# Simi is learning about palindromic numbers. Her teacher gave him the task to count all palindromic numbers present in that range.
# Simi has told you about this and want your help.
# You design an algorithm in order to help simi.

# Input Description:
# You will be given a number ‘n’

# Output Description:
# Print the count of all palindromic numbers till ‘n’(inclusive)

# Sample Input :
# 5

# Sample Output :
# 5

n = int(input())
numbers = []
for j in range(1,n+1):
    numbers.append(j)
count = 0
length = len(numbers)
for i in range(0,n):
    temp = numbers[i]
    reverse = 0
    while(temp>0):
        reminder = temp%10
        reverse = (reverse*10)+reminder
        temp = temp//10

    if(numbers[i] == reverse):
        count+=1
#print(i)
print(count)



# You are provided with a number ’n’. Your task is to tell whether that number is saturated. A saturated number is a number which is made by exactly two digits.

# Input Description:
# You are given with a number n.

# Output Description:
# Print Saturated if it is saturated else it is Unsaturated

# Sample Input :
# 121

# Sample Output :
# Saturated

text = input()
sett = list(set(text))
#print(sett)

if(len(sett) == 2):
    print("Saturated")



# boy rolls an unbiased die until he gets ‘1’. You are given a number n find the total sum of probability that he will get ‘1’ on or before nth trial.
# (Probability of getting 1 at 1 time + probability of getting 1 at 2 trial….+probability of getting 1 at nth trial)

# Constraints

# 1<=n<=1000

# Input Description:
# You are given a number ‘n’.

# Output Description:
# Print two numbers denoting numerator and denominator

# Sample Input :
# 1

# Sample Output :
# 1 6


n = int(input())
if (n == 1):
    numerator = 1
    denominator = 6
    print(numerator, end = ' ')
    print(denominator)

else:
    numerator = (n*6)-1
    denominator = (6*6)
    print(numerator, end = ' ')
    print(denominator)



# You are given a number ‘n’. You have to tell whether a number is great or not. 
# A great number is a number whose sum of digits let (m) and product of digits let(j) when summed together gives the number back

# m+j=n

#  

# Input Description:
# You are given a number n;

# Output Description:
# Print Great if a number is great else print the no

# Sample Input :
# 59

# Sample Output :
# Great


string = input()
digit = []

for i in string:
    digit.append(int(i))
    
product = 1
for i in digit:
    product = product*i

add = sum(digit)

final = product+add
actual = int(string)


if(final == actual):
    print('Great')
else:
    print("no")
    


# In XYZ country there is rule that car’s engine no. depends upon car’ number plate. 
# Engine no is sum of all the integers present on car’s Number plate.The issuing authority has hired you in order to provide engine no. to the cars.
# Your task is to develop an algorithm which takes input as in form of string(Number plate) and gives back

# Engine number.

# Input Description:
# You are given a string ’s’

# Output Description:
# Print the engine number

# Sample Input :
# HR05-AA-2669

# Sample Output :
# 28


string = input()

digit = []
for i in string:
    if(i.isdigit() == True):
        digit.append(int(i))
print(sum(digit))



# Find the minimum among 10 numbers.
# Sample Testcase :
# INPUT
# 5 4 3 2 1 7 6 10 8 9
# OUTPUT
# 1

n = input()
#for i in n :
#    if(i.isdigit()== True):
#        print(i)
 
n_new = n.split(' ')

n_final = []
for ele in n_new:
    n_final.append(int(ele))
    
print(min(n_final))



# Given 2 arrays print 'yes' if they are mirror images of each other,otherwise 'no'.
# Input Size : N <= 1000000
# Sample Testcase :
# INPUT
# 4
# 1 2 3 4
# 4 3 2 1
# OUTPUT
# yes


n = int(input())

string1 = input()
string2 = input()

list1 = string1.split(' ')
list2 = string2.split(' ')

int_list1 = []
int_list2 = []

for i in list1:
    int_list1.append(int(i))
for j in list2:
    int_list2.append(int(j))
    

reverse = int_list2[::-1]

if(int_list1 == reverse):
    print('yes')
else:
    print('no')



# Given base(B) and height(H) of a triangle find its area.
# Input Size : N <= 1000000
# Sample Testcase :
# INPUT
# 2 4
# OUTPUT
# 4


n = input()
list1 = n.split(' ')

b = int(list1[0])
h = int(list1[1])

area = (b*h) / 2

print(area)



# Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range (inclusive of L and R ).
# Input Size : L <= R <= 100000(complexity O(n) read about Sieve of Eratosthenes)
# Sample Testcase :
# INPUT
# 2 5
# OUTPUT
# 3


def __prime__(x):
    for i in range(2,int(x/2)+1):
        if(x%i) == 0:
            return 0
            break
    else:
        return 1

digits = input()
list1 = digits.split(' ')

list2=[]
for i in list1:
    list2.append(int(i))

l = list2[0] 
r = list2[1]
count = 0
for i in range(l, r+1):
    res = __prime__(i)
    count +=res
print(count)



# Kabali is a brave warrior who with his group of young ninjas moves from one place to another to fight against his opponents. 
# Before Fighting he just calculates one thing, the difference between his ninja number and the opponent's ninja number.
# From this difference he decides whether to fight or not. Kabali's ninja number is never greater than his opponent.
# Input
# The input contains two numbers in every line. These two numbers in each line denotes the number ninjas in Kabali's clan and his opponent's clan . 
# print the absolute difference of number of ninjas between Kabali's clan and his opponent's clan. Each output should be in seperate line.
# Sample Testcase :
# INPUT
# 100 200
# OUTPUT
# 100


n = input()
list1 = n.split(' ')

list2 = []
for i in list1:
    list2.append(int(i))
    
print(list2[1] - list2[0])



# Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.
# Sample Testcase :
# INPUT
# 5 5
# OUTPUT
# yes

def sqrt(x):
    sq = x**(1/2)
    sq_new = sq*10
    if(sq_new %10 == 0):
        return int(sq_new/10)
    else:
        return sq
        
n = input()
list1 = n.split(' ')

list2=[]
for i in list1:
    list2.append(int(i))
    
product = list2[0]*list2[1]
result = sqrt(product)

if(type(result) == int):
    print('yes')
else:
    print('no')



# Given 2 numbers N and M add both the numbers and check whether the sum is odd or even.
# Sample Testcase :
# INPUT
# 9 2
# OUTPUT
# odd

n = input()
list1 = n.split(' ')

list2 = []
for i in list1:
    list2.append(int(i))

N = list2[0]
M = list2[1]

if((N+M)%2 == 0):
    print('even')
else:
    print('odd')




# Find the minimum among 10 numbers.
# Sample Testcase :
# INPUT
# 5 4 3 2 1 7 6 10 8 9
# OUTPUT
# 1

n = input()
#for i in n :
#    if(i.isdigit()== True):
#        print(i)
 
n_new = n.split(' ')

n_final = []
for ele in n_new:
    n_final.append(int(ele))
    
print(min(n_final))



# Given 2 numbers N and K followed by elements of N .Print 'yes' if K exists else print 'no'.
# Sample Testcase :
# INPUT
# 4 2
# 1 2 3 3
# OUTPUT
# yes

n = input()
list1 = n.split(' ')
elements = input()
list3 = elements.split(' ')
count = 0

for i in list3:
    if (i == list1[1]):
        count+=1  
       
        
if(count >= 1):
    print('yes')
else:
    print('no')
    


# Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.
# Sample Testcase :
# INPUT
# 6 2
# 1 2 3 5 7 8
# OUTPUT
# 0


n = input()
list1 = n.split(' ')
elements = input()
list3 = elements.split(' ')
count = 0

for i in list3:
    if (i == list1[1]):
        count+=1  
       
        
if(count>1):
    print(count)
elif(count == 1):
    print(0)
else:
    print(-1)
    


# Write a program to print the sum of the first K natural numbers.
# Input Size : n <= 100000
# Sample Testcase :
# INPUT
# 3
# OUTPUT
# 6

n = int(input())

if(n == 0):
    print(0)
else:
    numerator = n*(n+1)
    result = numerator / 2
    print(int(result))





# Write a code to get an integer N and print the even values from 1 till N in a separate line.

# Input Description:
# A single line contains an integer N.

# Output Description:
# Print the even values from 1 to N in a separate line.

# Sample Input :
# 6

# Sample Output :
# 2
# 4
# 6


n = int(input())

for i in range(1, n+1):
    if(i%2 == 0):
        print(i)





# Write a code to get 2 integers A and N. Print the integer A, N times in separate line.

# Input Description:
# First line contains an integer A. Second line contains an Integer N.

# Output Description:
# Print the integer A, N times in a separate line.

# Sample Input :
# 2 3

# Sample Output :
# 2
# 2
# 2


n = input()

list1 = n.split(' ')

list2 = []
for i in list1:
    list2.append(int(i))
    
for i in range(0, list2[1]):
    print(list2[0])