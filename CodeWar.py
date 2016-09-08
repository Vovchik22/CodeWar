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