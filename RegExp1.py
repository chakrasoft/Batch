
'''
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
Built-in package re for Regular Expressions.'''


'''####The re module offers a set of functions that allows us to search a string for a match:
re.match(pattern, string, flags=0)
	
pattern-This is the regular expression to be matched.
string - This is the string, which would be searched to match 
the pattern at the beginning of string.
flags - You can specify different flags using bitwise OR (|). 
These are modifiers, which are listed in the table below.
'''
#Search the string to see if it starts with "The" and ends with "Spain":

import re
re.
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
'''
findall -	Returns a list containing all matches
search	- Returns a Match object if there is a match anywhere in the string
split	- Returns a list where the string has been split at each match
sub	- Replaces one or many matches with a string
'''

'''Metacharacters are characters with a special meaning##############
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"world$"	
*	Zero or more occurrences	"aix*"	
+	One or more occurrences	"aix+"	
{}	Exactly the specified number of occurrences	"al{2}"	
|	Either or	"falls|stays"	
()	Capture and group

'''
'''#####A special sequence is a \ followed by one of the characters in the list below, 
and has a special meaning:
    
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain"
r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bain"
r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

'''

'''###A set is a set of characters inside a pair of square brackets [] with a special 
meaning:'''
'''
[arn]	Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
'''
'''############################################'''
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)
###################################
str = "The rain in Spain"
x = re.findall("Portugal", str)
print(x)
######################################
str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())
########################################
str = "The rain in Spain"
x = re.search("Portugal", str)
print(x)
#################################
str = "The rain in Spain"
x = re.split("\s", str)
print(x)
################################
str = "The rain in Spain"
x = re.split("\s", str, 2)
print(x)
####################################
str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)
################################
str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)
###############################

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())

####################################### 
'''The re.match function returns a match object on success, 
None on failure. We usegroup(num) or groups() function of match object to 
get matched expression.

group(num=0)-This method returns entire match (or specific subgroup num)
groups()-This method returns all matching subgroups in a tuple (empty if there weren't any)
'''

import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : "), matchObj.group()
   print ("matchObj.group(1) : "), matchObj.group(1)
   print ("matchObj.group(2) : "), matchObj.group(2)
else:
   print ("No match!!")
   
############################################
line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print ("searchObj.group() : "), searchObj.group()
   print ("searchObj.group(1) : "), searchObj.group(1)
   print ("searchObj.group(2) : "), searchObj.group(2)
else:
   print ("Nothing found!!")

#####################Matching Versus Searching###########################
'''Python offers two different primitive operations based on regular expressions: 
    match checks for a match only at the beginning of the string, 
    while search checks for a match anywhere in the string 
    (this is what Perl does by default).'''
    
line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : "), matchObj.group()
else:
   print ("No match!!")

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print ("search --> searchObj.group() : "), searchObj.group()
else:
   print ("Nothing found!!")
####################################################





