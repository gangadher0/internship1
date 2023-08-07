#!/usr/bin/env python
# coding: utf-8

# In[103]:


# Question 1
#Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
#Sample Text- 'Python Exercises, PHP exercises.'
#Expected Output: Python:Exercises::PHP:exercises:

import re

text = 'Python Exercises, PHP exercises.'
new_text = re.sub('[ ,.]', ':', text)

print(new_text)


# In[96]:


# Question 2
#Write a Python program to find all words starting with 'a' or 'e' in a given string.

import re

given_text = "The starting point of many philosophical inquiries into a field is the examination and clarification of the fundamental concepts used in this field, often in the form of conceptual analysis. This approach is particularly prominent in the analytic tradition. It aims to make ambiguities explicit and to uncover various implicit and potentially false assumptions associated with these terms. "


list = re.findall(r'\b[ae]\w+', given_text)

print(list)


# In[97]:


# Question 3
#Create a function in python to find all words that are at least 4 characters long in a string. 
#The use of the re.compile() method is mandatory.

import re
text = 'The quick yellow fox jump over the lazy cat.'
pattern= re.compile(r'\b\w{2,3}\b')
x = re.sub(pattern, ' ', text)
print(x)


# In[98]:


# Question 4
#Create a function in python to find all three, four, and five character words in a string.
#The use of the re.compile() method is mandatory.

import re
text = 'how many amount spend for Car'
pattern = re.compile(r'\b\w{3,4,5}\b')
x = re.sub(pattern, ' ', text)
print(x)


# In[99]:


# Question 5
#Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
#Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

#Expected Output:
#example.com
#hr@fliprobo.com
#github.com
#Hello Data Science World
#Data Scientist


# In[100]:


import re

def remove_parentheses(lst):
    pattern = re.compile(r'\((.*?)\)')
    new_lst = []
    for string in lst:
        new_string = pattern.sub('', string)
        new_lst.append(new_string)
    return new_lst


# In[101]:


lst = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
new_lst = remove_parentheses(lst)
for string in new_lst:
    print(string)


# In[ ]:


#Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
#Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
#Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
#Note- Store given sample text in the text file and then to remove the parenthesis area from the text.


# In[102]:


import re

with open('sample.txt', 'r') as file:
    text = file.read()
    new_text = re.sub(r'\s*\([^)]*\)\s*', '', text)
    new_text = [string.strip() for string in new_text.split('\n')]
    print(new_text)


# In[ ]:


#Question 7- Write a regular expression in Python to split a string into uppercase letters.
#Sample text: “ImportanceOfRegularExpressionsInPython”
#Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]


# In[105]:


import re

sample_text = "ImportanceOfRegularExpressionsInPython"
words = re.findall(r'[A-Z][^A-Z]*', sample_text)
print(words)


# In[9]:


#Question 8-Create a function in python to insert spaces between words starting with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
#Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython

import re

def insert_spaces(sample_text: str) -> str:
    return re.sub(r'(?<=\d)(?=[a-zA-Z])', ' ', text)
sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"
new_text = insert_spaces(sample_text)
print(new_text)


# In[12]:


#Question 9-Create a function in python to insert spaces between words starting with capital letters or with numbers.
#Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
#Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython

import re

def insert_spaces(text: str)-> str:
    return re.sub(r'(?<=\d)(?=[a-zA-Z])|(?<=[a-zA-Z])(?=[A-Z])', ' ', text)

text = "RegularExpression1IsAn2ImportantTopic3InPython"
new_text = insert_spaces(text)
print(new_text)


# In[14]:


#Question 10- Write a python program to extract email address from the text stored in the text file using Regular Expression.
#Sample Text- Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com. 
#Please contact us at hr@fliprobo.com for further information. 
#Expected Output: 
#['xyz@domain.com', 'xyz.abc@sdomain.domain.com']
#['hr@fliprobo.com']
#Note- Store given sample text in the text file and then extract email addresses.

import re

def extract_emails(filename: str) -> list:
    with open(filename, 'r') as f:
        text = f.read()
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

filename = 'sample_1.txt'
emails = extract_emails(filename)
print(emails)


# In[15]:


#Question 11- Write a Python program to match a string that contains only
#upper and lowercase letters, numbers, and underscores.

import re

def text_match(text):
    pattern = r'^[a-zA-Z0-9_]*$'
    if re.search(pattern, text):
        return 'Found a match!'
    else:
        return 'Not matched!'

text = 'RegularExpression1IsAn2ImportantTopic3InPython'
result = text_match(text)
print(result)


# In[16]:


#Question 12- Write a Python program where a string will start with a specific number.

def specific_number(string: str, number: int) -> str:
    return f"{number}{string.lstrip(str(number))}"

text = "123abc"
number = 5
new_text = specific_number(text, number)
print(new_text)


# In[17]:


#Question 13- Write a Python program to remove leading zeros from an IP address

def remove_zeros_from_ip(ip_add):
    new_ip_add = ".".join([str(int(i)) for i in ip_add.split(".")])
    return new_ip_add

ip = "216.08.094.196"
print(remove_zeros_from_ip(ip))


# In[1]:


#Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
#Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
#Expected Output- August 15th 1947
#Note- Store given sample text in the text file and then extract the date string asked format.

import re

with open('sample_2.txt', 'r') as file:
    text = file.read()
    match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}(st|nd|rd|th)?\s\d{4}', text)
    if match:
        print(match.group())


# In[2]:


#Question 15- Write a Python program to search some literals strings in a string. 
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox', 'dog', 'horse'

import re

sample_text = 'The quick brown fox jumps over the lazy dog.'
patterns = ['fox', 'dog', 'horse']

for pattern in patterns:
    if re.search(pattern, text):
        print(f'{pattern} found in the text.')
    else:
        print(f'{pattern} not found in the text.')


# In[3]:


#Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
#Sample text : 'The quick brown fox jumps over the lazy dog.'
#Searched words : 'fox'

import re

sample_text = 'The quick brown fox jumps over the lazy dog.'
pattern = 'fox'
match = re.search(pattern, sample_text)
if match:
    start = match.start()
    end = match.end()
    print(f'Found "{pattern}" in "{sample_text}" from {start} to {end}.')
else:
    print(f'"{pattern}" not found in "{sample_text}".')


# In[4]:


#Question 17- Write a Python program to find the substrings within a string.
#Sample text : 'Python exercises, PHP exercises, C# exercises'
#Pattern : 'exercises'.

sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
start = 0
while True:
    start = sample_text.find(pattern, start)
    if start == -1:
        break
    end = start + len(pattern)
    print(f'Found "{pattern}" at index {start} to {end} in "{sample_text}".')
    start = end


# In[5]:


#Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
start = 0
count = 0
while True:
    start = text.find(pattern, start)
    if start == -1:
        break
    end = start + len(pattern)
    print(f'Found "{pattern}" at index {start} to {end} in "{text}".')
    start = end
    count += 1
print(f'Total occurrences of "{pattern}" in "{text}" is {count}.')


# In[ ]:


#Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

date_string = '2023-08-07'
date_obj =  datetime.strptime(date_string, '%Y-%m-%d')
new_date_string = date_obj.strftime('%d-%m-%Y')
print(new_date_string)


# In[8]:


#Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string.
#The use of the re.compile() method is mandatory.

import re

def find_decimal_numbers(text):
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')
    return pattern.findall(text)

text = 'The apple price is $09.23 and the quantity is 46.6.'
decimal_numbers = find_decimal_numbers(text)
print(decimal_numbers)


# In[9]:


#Question 21- Write a Python program to separate and print the numbers and their position of a given string.

import re

text = 'Given example creates a ArrayList with a capacity of 55 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly.'
pattern = r'\d+'
for match in re.finditer(pattern, text):
    print(f'Number: {match.group()}, Position: {match.start()}')


# In[14]:


#Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
#Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
#Expected Output: 950

import re

sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
pattern = r'\d+'
numbers = [int(match) for match in re.findall(pattern, sample_text)]
max_number = max(numbers)
print(f'The maximum numeric value in "{text}" is {max_number}.')


# In[17]:


#Question 23- Create a function in python to insert spaces between words starting with capital letters.
#Sample Text: “RegularExpressionIsAnImportantTopicInPython"
#Expected Output: Regular Expression Is An Important Topic In Python


import re

def insert_spaces(text):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    return pattern.sub(' ', text)

text = 'RegularExpressionIsAnImportantTopicInPython'
new_text = insert_spaces(text)
print(new_text)


# In[18]:


#Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

text = 'WeNeedToUnderstandATablesSchemaToEffectivelyPulloutTheDataWeWant'
pattern = r'[A-Z][a-z]+'
matches = re.findall(pattern, text)
if matches:
    print(f'Sequences of one upper case letter followed by lower case letters in "{text}" are:')
    for match in matches:
        print(match)
else:
    print(f'No sequences of one upper case letter followed by lower case letters found in "{text}".')


# In[19]:


#Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
#Sample Text: "Hello hello world world"
#Expected Output: Hello hello world


import re

text = 'Hello hello world world'
pattern = r'\b(\w+)(?:\W+\1\b)+'
new_text = re.sub(pattern, r'\1', text,)
print(new_text)


# In[20]:


#Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

import re

def check_string(string):
    regex = r'[a-zA-z0-9]$'
    if re.search(regex, string):
        print(f'The string "{string}" ends with an alphanumeric character.')
    else:
        print(f'The string "{string}" does not end with an alphanumeric character.')

check_string('shivi01072022')


# In[21]:


#Question 27-Write a python program using RegEx to extract the hashtags.
#Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
#Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']


import re

text = 'RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo'
pattern = r'#\w+'
text = re.findall(pattern, text)
print(text)


# In[22]:


#Question 28- Write a python program using RegEx to remove <U+..> like symbols
#Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
#Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
#Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders


import re

text = '@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders'
pattern = r'<U\+[0-9A-Fa-f]{1,4}>'
new_text = re.sub(pattern, '', text)
print(new_text)


# In[23]:


#Question 29- Write a python program to extract dates from the text stored in the text file.
#Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
#Note- Store this sample text in the file and then extract dates.


import re

with open('sample_3.txt', 'r') as file:
    text = file.read()
    pattern = r'\d{1,2}-\d{1,2}-\d{4}'
    dates = re.findall(pattern, text)
    if dates:
        print(f'Dates found in the text file are:')
        for date in dates:
            print(date)
    else:
        print(f'No dates found in the text file.')


# In[24]:


#Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
#The use of the re.compile() method is mandatory.
#Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
#Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.

import re

def remove_words(text):
    pattern = re.compile(r'\b\w{2,4}\b')
    return pattern.sub('', text)
text = 'The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly.'
new_text = remove_words(text)
print(new_text)


# In[ ]:




