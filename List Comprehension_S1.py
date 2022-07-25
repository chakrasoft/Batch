'''
Comprehensions provide us with a short and concise way to construct new sequences 
(such as lists, set, dictionary etc.) 
4 types of comprehensions:
**************************
List Comprehensions
Dictionary Comprehensions
Set Comprehensions
Generator Comprehensions
'''
[expression for item in iterable]
[x for x in range(1,11)]
S = [x**2 for x in range(10)]
print(S)
#########################################
[expression for item in iterable if conditional]
[x for x in range(1,11) if x%2==0]
new_list = [n**2 for n in numbers if n%2==0] #expression followed by for loop followed by the conditional clause
print(new_list)
############################################
numbers = range(10)
# Initialize `new_list`
new_list = []
# Add values to `new_list`
for n in numbers:
    if n%2==0: #check if the element is even
        new_list.append(n**2) #raise that element to the power of 2 and append to the list
print(new_list)
################################################
[expression if conditional else stmt for item in iterable]
[x if x>2 else x+1 for x in range(1,11)]
##########################################
prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
Result = [i if i > 0 else 0 for i in prices]
Result

def get_price(price):
    return price if price > 0 else 0
Result = [get_price(i) for i in prices]
Result
#####################################################
'''
Dictionary Comprehensions:
output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}

creating an output dictionary which contains only the odd numbers 
that are present in the input list as keys and their cubes as values
'''
in_list = [1, 2, 3, 4, 5, 6, 7]
  
out_dict = {}
  
for i in in_list:
    if i % 2 != 0:
        out_dict[i] = i**3
  
print("Dictionary using for loop:",out_dict )
##########################################
in_list = [1,2,3,4,5,6,7]
  
dict_comp = {i:i ** 3 for i in in_list if i % 2 != 0}
  
print("Output Dictionary Using dictionary comprehensions:",dict_comp)
#############################################
'''
two lists containing the names of states and their corresponding capitals, 
construct a dictionary which maps the states with their respective capitals.
'''
state = ['Andhra', 'Goa', 'Telangana']
capital = ['Amaravati', 'Panaji', 'Hyderabad']
  
out_dict = {}
  
for (key, value) in zip(state, capital):
    out_dict[key] = value
  
print("Dictionary using for loop:",out_dict)
##############################################
state = ['Andhra', 'Goa', 'Telangana']
capital = ['Amaravati', 'Panaji', 'Hyderabad']
  
dict_comp = {key:value for (key, value) in zip(state, capital)}
  
print("Using dictionary comprehensions:", dict_comp)
###########################################
'''
Set Comprehensions:
Set comprehensions are pretty similar to list comprehensions. 
The only difference between them is that set comprehensions use curly brackets { }    

create an output set which contains only the even numbers that are 
present in the input list. Note that set will discard all the duplicate values.
'''
in_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
  
out_set = set()
  
for i in in_list:
    if i % 2 == 0:
        out_set.add(i)
  
print("Output Set using for loop:", out_set)
############################################
in_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
  
set_comp = {i for i in in_list if i % 2 == 0}
  
print("Output Set using set comprehensions:",set_comp)
###############################################
'''
Generator Comprehensions:
*************************
Generator Comprehensions are very similar to list comprehensions. 
One difference between them is that generator comprehensions use circular 
brackets whereas list comprehensions use square brackets. 
The major difference between them is that generators don’t allocate 
memory for the whole list. Instead, they generate each value one by one 
which is why they are memory efficient. 
'''
in_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
  
out_gen = (i for i in in_list if i % 2 == 0)
  
print("Using generator comprehensions:", end = ' ')
  
for var in out_gen:
    print(var, end = ' ')
#############################################
'''
Nested List Comprehensions:
***************************
Nested List Comprehensions are nothing but a list comprehension within 
another list comprehension which is quite similar to nested for loops.
'''
matrix = []
for i in range(5): 
    # Append an empty sublist inside the list
    matrix.append([])
      
    for j in range(5):
        matrix[i].append(j)       
print(matrix)
#########################################
matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)
##############################################
'''
#To flatten a given 2-D list:
we can divide the list comprehension into
three parts:

flatten_matrix = [val
                  for sublist in matrix
                  for val in sublist]
'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flatten_matrix = []
  
for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)
          
print(flatten_matrix)
##############################################
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
  
flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)
################################################