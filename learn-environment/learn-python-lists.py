a = " Hello, World!"
print(a)
 #Hello, World!
print(a.upper()[2:5])
#ELL
print(a.strip())
#Hello, World!

print(a.replace("H", ""))
 #ello, World!

print(a.split("o"))
#[' Hell', ', W', 'rld!']

a = "Hello"
b = "World"
c = a +" "+ b
print(c)
#Hello World


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#I want to pay 49.95 dollars for 3 pieces of item 567.

txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
#We are the so-called "Vikings" from the north.

print(bool("Hello"))
#True
print(bool(15))
#True



#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
#False

#You can create functions that returns a Boolean Value:
def myFunction() :
  return True

print(myFunction())
#True



Python also has many built-in functions that return a boolean value
like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))
#True
x = 200
print(isinstance(x, float))
#False


----------------LISTAS------------
"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
- Dictionary is a collection which is ordered** and changeable. No duplicate members.

"""

Access Items

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#banana

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#cherry
"""
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # ele sempre vem um antes do ultimo. se quer a poisicao 4, tem que colocar a posicao 5.
#['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#['cherry', 'orange', 'kiwi', 'melon', 'mango']

'''Check if Item Exists
To determine if a specified item is present in a list use the in keyword
'''
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  #Yes, 'apple' is in the fruits list

  Change Item Value

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" # coloca o index do item e o que vc quer colocar no lugar
print(thislist)
#['apple', 'blackcurrant', 'cherry']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

If you insert more items than you replace, the new items will be inserted where you specified,
and the remaining items will move accordingly:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#['apple', 'blackcurrant', 'watermelon', 'cherry']

If you insert less items than you replace, the new items will be inserted where you specified,
and the remaining items will move accordingly:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#['apple', 'watermelon']

Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # inserir no index 2 e o que quer inserir
print(thislist)
# ['apple', 'banana', 'watermelon', 'cherry']

Append Items
To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#['apple', 'banana', 'cherry', 'orange']

Extend List
To append elements from typing import ForwardRef
from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#['apple', 'banana', 'cherry', 'kiwi', 'orange']

Remove Specified Item
The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#["apple", "cherry"]

Remove Specified Index
The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#["apple", "cherry"]

If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#["banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
del thislist
#a lista será deletada por completo


Clear the List
The clear() method empties the list.

The list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#[]

-------------LOOP INTO LISTS-----------------
Loop Through a List
You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
print(x)
#apple
#banana
#cherry

Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#apple
#banana
#cherry


Using a While Loop
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.

Remember to increase the index by 1 after each iteration.

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#apple
#banana
#cherry


Looping Using List Comprehension
List Comprehension offers the shortest syntax for looping through lists:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#apple
#banana
#cherry


List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#['apple', 'banana', 'mango']

-----

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#['apple', 'banana', 'mango']

The Syntax
newlist = [expression for item in iterable if condition == True]

newlist = [x for x in fruits if x != "apple"]



The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

The condition is optional and can be omitted:

newlist = [x for x in fruits]


Iterable
The iterable can be any iterable object, like a list, tuple, set etc.

You can use the range() function to create an iterable:

newlist = [x for x in range(10)]


Example
Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]


Expression
The expression is the current item in the iteration, but it is also the outcome, 
which you can manipulate before it ends up like a list item in the new list:

Example
Set the values in the new list to upper case:

newlist = [x.upper() for x in fruits]


You can set the outcome to whatever you like:

Example
Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]



The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

Example
Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]


Sort List Alphanumerically  -- coloca ordem alfabetica decrescente
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#[23, 50, 65, 82, 100]

Sort Descending - ordem crescente
To sort descending, use the keyword argument reverse = True:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#['pineapple', 'orange', 'mango', 'kiwi', 'banana']

Customize Sort Function
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):

Example
Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#[50, 65, 23, 82, 100]


ORDER BY LOWERCASE OR UPPERCASE
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#['banana', 'cherry', 'Kiwi', 'Orange']


Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements.

Example
Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#['cherry', 'Kiwi', 'Orange', 'banana']


Copy a List
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, 
and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().

Example
Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#['apple', 'banana', 'cherry']

Example
Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#["apple", "banana", "cherry"]


Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.

Example
Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#['a', 'b', 'c', 1, 2, 3]

Another way to join two lists is by appending all the items from list2 into list1, one by one:

Example
Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#['a', 'b', 'c', 1, 2, 3]

Or you can use the extend() method, which purpose is to add elements from one list to another list:

Example
Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
#['a', 'b', 'c', 1, 2, 3]



------------------EXEMPLOS DE PROJETOS-----------------------------------------

#Laço de repetição For

'''Estou simulando um carrinho de compras em um supermercado. A pessoa insere o nome do produto e valor, e no final quando ja nao irá mais cadastrar produto,
trazemos todos os produtos, preços e o valor da fatura atual '''


repetir = 's'
fatura = []
total = 0

while repetir == 's':
  produto = input('Digite o nome do produto: ')
  preco = input('Digite o preço do produto: '))

  fatura.append([produto, preco])
  total += preco 

  repetir = input('Há mais produtos a serem cadastrados? (S ou N)').lower()

for i in fatura:
  print(i[0], ':', i[1])

print('O total da fatura é: ', total)