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