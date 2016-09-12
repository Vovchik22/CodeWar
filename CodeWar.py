#CodeWar python solution


##Format a string of names like 'Bart, Lisa & Maggie'.

'''
Example:
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
'''

def namelist(names):
	if len(names) > 1:
		return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
								names[-1]['name'])
	elif names:
		return names[0]['name']
	else:
		return ''



def namelist(names):
	if len(names)==0: return ''
	if len(names)==1: return names[0]['name']
	return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']


def namelist(names):
	return " ".join([names[i]["name"] + (" &" if i == len(names)-2 else "" if i==len(names)-1 else ",") for i in range(len(names))])


##Beginner Series #3 Sum of Numbers

'''
Example: 
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
'''


def get_sum(a,b):
	return sum(xrange(min(a,b), max(a,b)+1))

def get_sum(a, b):
	return (a + b) * (abs(a - b) + 1) // 2




##Money, Money, Money

'''
Example:

  Let P be the Principal = 1000.00      
  Let I be the Interest Rate = 0.05      
  Let T be the Tax Rate = 0.18      
  Let D be the Desired Sum = 1100.00


After 1st Year -->
  P = 1041.00
After 2nd Year -->
  P = 1083.86
After 3rd Year -->
  P = 1128.30

'''


from math import ceil, log
def calculate_years(principal, interest, tax, desired):
	if principal >= desired: return 0
	
	return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))

def calculate_years(p, i, t, d, n=0):
	if p >= d:
		return n
	p = p + p * i * (1 - t)
	return calculate_years(p, i, t, d, n+1)


##Consecutive strings

'''
Description:

You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Example:

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
'''


def longest_consec(strarr, num):
	if not strarr or num < 1 or num > len(strarr):
		return ''
	longest = 0
	longest_i = None

	for i in range(len(strarr)):
		length = sum(len(item) for item in strarr[i:i + num])
		if length > longest:
			longest = length
			longest_i = i

	return ''.join(strarr[longest_i:longest_i + num])

def longest_consec(strarr, k):
	result = ""
	
	if k > 0 and len(strarr) >= k:
		for index in range(len(strarr) - k + 1):
			s = ''.join(strarr[index:index+k])
			if len(s) > len(result):
				result = s
			
	return result


def longest_consec(strarr, k):
	if (len(strarr) == 0 or k <= 0) or len(strarr) < k:
		return ""
	lst = [''.join(strarr[i:i+k]) for i in xrange(len(strarr))]
	return max(lst, key= lambda x: len(x))

def longest_consec(s, k):
	return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""


##Is this a triangle?

'''
Description:

Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).
'''

def is_triangle(a, b, c):
	a, b, c = sorted([a, b, c])
	return a + b > c

def is_triangle(a, b, c):
	return (a<b+c) and (b<a+c) and (c<a+b)

def is_triangle(a, b, c):
	return abs(a-b) < c < a+b

#Equal Sides Of An Array

'''
Description:

You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

For example:

Let's say you are given the array {1,2,3,4,3,2,1}:
Your function will return the index 3, because at the 3rd position of the array, the sum of left side of the index ({1,2,3}) and the sum of the right side of the index ({3,2,1}) both equal 6.

Let's look at another one.
You are given the array {1,100,50,-51,1,1}:
Your function will return the index 1, because at the 1st position of the array, the sum of left side of the index ({1}) and the sum of the right side of the index ({50,-51,1,1}) both equal 1.

Note: Please remember that in most programming/scripting languages the index of an array starts at 0.

Input:

An integer array of length 0 < arr < 1000. The numbers in the array can be any integer positive or negative.

Output:

The lowest index N where the side to the left of N is equal to the side to the right of N. If you do not find an index that fits these rules, then you will return -1.

Note:

If you are given an array with multiple answers, return the lowest correct index.
'''


def find_even_index(arr):
	for i in range(len(arr)):
		if sum(arr[:i]) == sum(arr[i+1:]):
			return i
	return -1

#Stop gninnipS My sdroW!

'''
Description:

Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
'''

def spin_words(sentence):
	# Your code goes here
	return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

def spin_words(sentence):
	return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split())


#Array.diff

'''
Description:

Your goal in this kata is to implement an difference function, which subtracts one list from another.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

'''

def array_diff(a, b):
	return [x for x in a if x not in b]

def array_diff(a, b):
	return filter(lambda i: i not in b, a)

def array_diff(a, b):
	for i in b:
		while a.count(i):
			a.remove(i)
	return a

#Title Case

'''
Description:

A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

Arguments (Haskell)

First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.
Second argument: the original string to be converted.
Arguments (Other languages)

First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words that must always be lowercase except for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.
Example

title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'
'''

def title_case(title, minor_words = ''):
	if len(title) == 0:
		return ''
	res = [title.title().split()[0]]
	for word in title.title().split()[1:]:
		if word.lower() in [w.lower() for w in minor_words.split()]:
			res.append(word.lower())
		else:
			res.append(word)
	return ' '.join(res)

def title_case(title, minor_words=''):
	title = title.capitalize().split()
	minor_words = minor_words.lower().split()
	return ' '.join([word if word in minor_words else word.capitalize() for word in title])


#IQ Test

'''
Description:

Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
'''

def iq_test(numbers):
	e = [int(i) % 2 == 0 for i in numbers.split()]
	return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

def iq_test(numbers):
	numbers = numbers.split(" ")
	odd = []
	even = []
	for i,v in enumerate(numbers):
		if int(v) % 2:
			odd.append([i,v])
		else:
			even.append([i,v])
	if len(even) == 1:
		return (even[0][0])+1
	if len(odd) == 1:
		return (odd[0][0])+1

def iq_test(n):
	n = [int(i)%2 for i in n.split()]
	if n.count(0)>1:
		return n.index(1)+1
	else:
		return n.index(0)+1

#Triple trouble

'''
Description:

Write a function

triple_double(num1, num2)
which takes in numbers num1 and num2 and returns 1 if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.
For example:
triple_double(451999277, 41177722899) == 1 // num1 has straight triple 999s and 
										  // num2 has straight double 99s

triple_double(1222345, 12345) == 0 // num1 has straight triple 2s but num2 has only a single 2

triple_double(12345, 12345) == 0

triple_double(666789, 12345667) == 1
If this isn't the case, return 0

'''

def triple_double(num1, num2):
	for x in str(num1):
		while str(num1).find(x*3)>-1 and str(num2).find(x*2)>-1:
			return 1
	return 0
	return [1 if str(num1).find(x*3)>0 and str(num2).find(x*2)>0 else 0 for x in str(num1)]

def triple_double(num1, num2):
	return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])


#WeIrD StRiNg CaSe

'''
Description:

Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:

to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
'''
#1
def to_weird_case(string):
	recase = lambda s: "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
	return " ".join([recase(word) for word in string.split(" ")])

#2
def to_weird_case_word(string):
	return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))
	
def to_weird_case(string):
	return " ".join(to_weird_case_word(str) for str in string.split())

#3
def to_weird_case(a):
	c = a.split(" ")
	for i in range(len(a.split(" "))):
		b = []
		for j in range(len(a.split(" ")[i])):
			if j % 2 ==0:
				b += a.split(" ")[i][j].upper()
			else:
				b += a.split(" ")[i][j].lower()
		c[i]= ''.join(b)
	return ' '.join(c)

#Pete, the baker

'''
Description:

Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
'''

#注意dict.get(key, default=None)的妙用
def cakes(recipe, available):
	return min(available.get(k, 0)/recipe[k] for k in recipe)

def cakes(recipe, available):
	return min(available.get(k, 0) / v for k, v in recipe.iteritems())

def cakes(recipe, available):
	return min([available[k]/v][0] if k in available else 0 for k,v in recipe.items())

#Human Readable Time

'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''
## %02d = two digits at least

def make_readable(seconds):
	return "%02d:%02d:%02d"%(seconds/(60*60),(seconds/60)%60,seconds%60)

def make_readable(s):
	return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

#Bit Counting

'''
Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in the binary representation of that number.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''
def countBits(n):
	return bin(n).count("1")

def countBits(n):
	total = 0
	while n > 0:
		total += n % 2
		n >>= 1
	return total

#Moving Zeros To The End
'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

Test.assert_equals(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
Test.assert_equals(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]),[9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
Test.assert_equals(move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]),["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
Test.assert_equals(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]),["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
Test.assert_equals(move_zeros([0,1,None,2,False,1,0]),[1,None,2,False,1,0,0])
Test.assert_equals(move_zeros(["a","b"]),["a","b"])
Test.assert_equals(move_zeros(["a"]),["a"])
Test.assert_equals(move_zeros([0,0]),[0,0])
Test.assert_equals(move_zeros([0]),[0])
Test.assert_equals(move_zeros([]),[])

'''

def move_zeros(array):
	a = list(filter(lambda x: x!=0 or type(x) is bool, array))
	return a + [0]*(len(array)-len(a))

def move_zeros(array):
	a = list(filter(lambda x: x!=0 or type(x) is bool, array))
	return a + [0]*(len(array)-len(a))

###
def move_zeross(array):
	for i in range(len(array)):
		if array[i] is not False and array[i] == 0:
			array.pop(i)
			array.append(0)
	return array

def move_zeros(array):
	for i in range(len(array)):
		if array[i] is not False and array[i] == 0:
			move_zeross(array)
	return array

###recursive
def move_zeros(array, n=None):
	if n is None:
		n = len(array) - 1
	if n < 0:
		# no more to process
		return array
	if array[n] is not False and array[n] == 0:
		# move this zero to the end
		array.append(array.pop(n))
	return move_zeros(array, n-1)



#Your order, please
'''
Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"
'''

import re
def order(sentence):
	if sentence:
		a = [map(int, re.findall(r'\d+', x)) for x in sentence.split(" ")]
		b = []
		for i in range(1,len(a)+1):
			b.append(sentence.split(" ")[a.index([i])])
		return " ".join(b)
	else:
		return 0

#The value of the key parameter should be a function that takes a single argument and returns a key to use for sorting purposes. 
#This technique is fast because the key function is called exactly once for each input record.
def order(sentence):
	return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))


def order(words):
	return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

#Permutations

'''
Description:

In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
'''

'''
The sets module provides classes for constructing and manipulating unordered collections of unique elements. Common uses include membership testing, removing duplicates from a sequence, and computing standard math operations on sets such as intersection, union, difference, and symmetric difference.
'''

def permutations(string):
	result = set([string])
	if len(string) == 2:
		result.add(string[1] + string[0])
	elif len(string) > 2:
		for i, c in enumerate(string):
			for s in permutations(string[:i] + string[i + 1:]):
				result.add(c + s)
	return list(result)


def permutations(string):
  if len(string) == 1: return set(string)
  first = string[0]
  rest = permutations(string[1:])
  result = set()
  for i in range(0, len(string)):
    for p in rest:
      result.add(p[0:i] + first + p[i:])
  return result

# p[, r]	r-length tuples, all possible orderings, no repeated elements
import itertools
def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))

import itertools
def permutations(string):
    return set(''.join(x) for x in itertools.permutations(string, r=len(string)))

#coding by next function. just add set(),and remove duplicate item.
def perms(s):        
    if(len(s)==1): return [s]
    result=[]
    for i,v in enumerate(s):
        result += [v+p for p in perms(s[:i]+s[i+1:])]
    return list(set(result))


#permutation without duplicate characters
def perms(s):        
    if(len(s)==1): return [s]
    result=[]
    for i,v in enumerate(s):
        result += [v+p for p in perms(s[:i]+s[i+1:])]
    return result
perms('abc')
['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

#Length of missing array

'''
Description:

You get an array of arrays.
If you sort the arrays by their length, you will see, that their length-values are consecutive.
But one array is missing!


You have to write a method, that return the length of the missing array.

Example:
[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3


If the array of arrays is null/nil or empty, return 0.

When an array in the array is null or empty, return 0 too!
There will always be a missing element and its length will be always between the given arrays. 

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.
'''
#best
def get_length_of_missing_array(a):
    lns = a and all(a) and list(map(len, a))
    return bool(lns) and sum(range(min(lns), max(lns) + 1)) - sum(lns)


#mine
def get_length_of_missing_array(array_of_arrays):
	print array_of_arrays
	if not array_of_arrays:
		return 0
	lensList = []
	for x in range(len(array_of_arrays)):
		if not array_of_arrays[x]:
			return 0
		else:
			lensList.append(len(array_of_arrays[x]))
	print lensList
	for i in range(sorted(lensList)[0],sorted(lensList)[-1]+1):
		if i not in lensList:
			return i


#Banker's Plan

'''
Description:

John has some amount of money of which he wants to deposit a part f0 to the bank at the beginning of year 1. He wants to withdraw each year for his living an amount c0.

Here is his banker plan:

deposit f0 at beginning of year 1
his bank account has an interest rate of p percent per year, constant over the years
John can withdraw each year c0, taking it whenever he wants in the year; he must take account of an inflation of i percent per year in order to keep his quality of living. i is supposed to stay constant over the years.
all amounts f0..fn-1, c0..cn-1 are truncated by the bank to their integral part
Given f0, p, c0, i the banker guarantees that John will be able to go on that way until the nth year.
Example:

f0 = 100000, p = 1 percent, c0 = 2000, n = 15, i = 1 percent

beginning of year 2 -> f1 = 100000 + 0.01*100000 - 2000 = 99000; c1 = c0 + c0*0.01 = 2020 (with inflation of previous year)

beginning of year 3 -> f2 = 99000 + 0.01*99000 - 2020 = 97970; c2 = c1 + c1*0.01 = 2040.20 (with inflation of previous year, truncated to 2040)

beginning of year 4 -> f3 = 97970 + 0.01*97970 - 2040 = 96909.7 (truncated to 96909); c3 = c2 + c2*0.01 = 2060.4 (with inflation of previous year, truncated to 2060) and so on...

John wants to know if the bankers'plan is right or wrong. Given parameters f0, p, c0, n, i build a function fortune which returns true if John can make a living for n years and false if it is not possible.
'''

#

def fortune(f,p,c,n,i):
	for x in range(n-1):
		f = round(f,2) * (1 + round(p,2)/100) - c * (1 + round(i,2)/100)**x
	return f > 0



#Text align justify

'''
Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the expected justification width. The longest word will never be greater than this width.

Here are the rules:

Use spaces to fill in the gaps between words.
Each line should contain as many words as possible.
Use '\n' to separate lines.
Gap between words can't differ by more than one space.
Lines should end with a word not a space.
'\n' is not included in the length of a line.
Large gaps go first, then smaller ones: 'Lorem---ipsum---dolor--sit--amet' (3, 3, 2, 2 spaces).
Last line should not be justified, use only one space between words.
Last line should not contain '\n'
Strings with one word do not need gaps ('somelongword\n').
Example with width=30:

Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.
Also you can always take a look at how justification works in your text editor or directly in HTML (css: text-align: justify).
'''



def justify(text, width):
    length = text.rfind(' ', 0, width+1)
    if length == -1 or len(text) <= width: return text
    line = text[:length]
    spaces = line.count(' ')
    if spaces != 0:
        expand = (width - length) / spaces + 1
        extra = (width - length) % spaces
        line = line.replace(' ', ' '*expand)
        line = line.replace(' '*expand, ' '*(expand+1), extra)
    return line + '\n' + justify(text[length+1:], width)
