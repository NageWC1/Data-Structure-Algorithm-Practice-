# Allways the Big O notation will take for the worst case senario 
arr = [10,12,13,14,15,16,17]

# fining the elements by its index so, it will take: O(1) time - constant time
print(arr[0])

# senario 02: find out the day which have price 15 
# here the time will be: O(n) - becasue have to go through all the element by for loop 
for i in range(len(arr)):
    if arr[i] == 15:
        print("They day is:", i+1)

# print the element also will take same amount of time which means O(n)
# because have to go through all the index to printout all the detail in the array 

# same time will take for insert and remove as Bog O: O(n)
arr.insert(1,200)
arr.remove(15)


# also we can create 2 dimentional array
two_d_arr = [
    [1,2,3,4],
    [3,4,5,6],
    [7,8,9,10]
]
  
#   accessing the 2 dimentionaly array
print("print the element in oth row and 4th element is:",two_d_arr[0][3])


                                # excerise 
# 1. Lets us say your expenses for every month are listed below 
#     i. january - 2200
#     ii. Februaury - 2350
#     iii. March - 2600
#     iv. April - 2130
#     v. May - 2190

# create a list to stroe these monthly expense and using it find out 
# below is dictionary 
month_exp = {
    'jan': 2200,
    'feb':2350,
    'mar':2600,
    'apr':2130,
    'may':2190
}

# 1) In feb, how many dollar you spent extra compare to january 
print('the amout that extra spent on feb compare to jan is', month_exp['feb'] - month_exp['jan'])

# 2) Find out your total expense in first quater of the year (1st three moth)
print("the total amount of the first quater is:", month_exp['jan'] + month_exp['feb'] + month_exp['mar'])

# 3) Find out if you spent exactly 2000 dollars in any month 

for element in month_exp.keys():
    val = month_exp[element]
    if val == 2000:
        print("the month",element)    
    

# 4) June month just finised and your expenses 1980. Add this to our monthly expence list 
month_exp['jun'] = 1980

# you returned an item that you bought in a monthof april and got a refund of 200$. make a correction to your expense 
month_exp['apr'] = month_exp['apr']  + 200
print("the updated dictionary will be", month_exp)


#                       EXCERCISE 02
heros = ['spider man','thor','hulk','iron man','captain america']

# questions 
# 10 lenth of the list 
print(len(heros))

# 2) add 'black panther' at the end of the list 
heros.append('balck panther')
print('updated after added the black panther', heros)

# 3) you realize tht you need to add hulk 'blacl panther' after 'hulk', so remove it from the list and then add 
# it after 'hulk'
# this code will remove it from the end of the list - 'black panther'
heros.pop()

heros.insert(3,'black panther')
# priniting the list after updating it
print(heros)

#                       EXCERCISE 03 
# create a list of all odd number between 1 and max number. Max number is something need to take from a user input()
# function

# taking input from the user - to take the integer number we have to specify the type before it 
max_number = int(input("Enter the number:\n"))
# declare empty list 
list_num = []
for i in range(max_number + 1):
    if i%2 != 0:
        list_num.append(i)


print(list_num)