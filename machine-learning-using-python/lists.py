Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=10
>>> float(a)
10.0
>>> #LISTS
>>> names = []
>>> tyep(names)

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tyep(names)
NameError: name 'tyep' is not defined
>>> type(names)
<type 'list'>
>>> names.append('ram')
>>> names
['ram']
>>> names.append('suresh')
>>> names
['ram', 'suresh']
>>> names = ['varun']
>>> names
['varun']
>>> names.append('varun1','surehs')

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    names.append('varun1','surehs')
TypeError: append() takes exactly one argument (2 given)
>>> names
['varun']
>>> names.append('ram','suresh')

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    names.append('ram','suresh')
TypeError: append() takes exactly one argument (2 given)
>>> names.append('ram')
>>> names.append('suresh')
>>> names
['varun', 'ram', 'suresh']
>>> names.count
<built-in method count of list object at 0x02FAC170>
>>> names.count
<built-in method count of list object at 0x02FAC170>
>>> names.count
<built-in method count of list object at 0x02FAC170>
>>> names.append('virat')
>>> names.append('virat')
>>> names.append('virat')
>>> names.append('virat')
>>> names
['varun', 'ram', 'suresh', 'virat', 'virat', 'virat', 'virat']
>>> names.count
<built-in method count of list object at 0x02FAC170>
>>> names.count()

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    names.count()
TypeError: count() takes exactly one argument (0 given)
>>> names.count('virat')
4
>>> names.count('varun')
1
>>> names.count(names)
0
>>> names.count
<built-in method count of list object at 0x02FAC170>
>>> names.count names
SyntaxError: invalid syntax
>>> names.insert('dhoni')

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    names.insert('dhoni')
TypeError: insert() takes exactly 2 arguments (1 given)
>>> names.insert('dhoni',3)

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    names.insert('dhoni',3)
TypeError: an integer is required
>>> names.insert(3,'Dhoni')
>>> names
['varun', 'ram', 'suresh', 'Dhoni', 'virat', 'virat', 'virat', 'virat']
>>> names[0]
'varun'
>>> names
['varun', 'ram', 'suresh', 'Dhoni', 'virat', 'virat', 'virat', 'virat']
>>> names[0]
'varun'
>>> names[2]
'suresh'
>>> type(names[3])
<type 'str'>
\
>>> type(names)
<type 'list'>
>>> names.append(2)
>>> names
['varun', 'ram', 'suresh', 'Dhoni', 'virat', 'virat', 'virat', 'virat', 2]
>>> names[8]
2
>>> names[9]

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    names[9]
IndexError: list index out of range
>>> names
['varun', 'ram', 'suresh', 'Dhoni', 'virat', 'virat', 'virat', 'virat', 2]
>>> names.index('Dhoni')
3
>>> names[3]
'Dhoni'
>>> names.pop(7)
'virat'
>>> names.pop(7)
2
>>> names.pop(7)

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    names.pop(7)
IndexError: pop index out of range
>>> names
['varun', 'ram', 'suresh', 'Dhoni', 'virat', 'virat', 'virat']
>>> names.pop(5)
'virat'
>>> names.pop(5)
'virat'
>>> names.pop(5)

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    names.pop(5)
IndexError: pop index out of range
>>> names.remove('suresh')
>>> names
['varun', 'ram', 'Dhoni', 'virat']
>>> names.pop(0)
'varun'
>>> names
['ram', 'Dhoni', 'virat']
>>> names.remove('suresh')

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    names.remove('suresh')
ValueError: list.remove(x): x not in list
>>> names
['ram', 'Dhoni', 'virat']
>>> names.append('virat')
>>> names.remove('virat')
>>> names.remove('virat')
>>> names
['ram', 'Dhoni']
>>> names.append()

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    names.append()
TypeError: append() takes exactly one argument (0 given)
>>> names.append('Dhoni')
>>> names
['ram', 'Dhoni', 'Dhoni']
>>> names.remove('Dhoni')
>>> names
['ram', 'Dhoni']
>>> names
['ram', 'Dhoni']
>>> names.append('suresh raina')
>>> names.append('W sundar')
>>> names
['ram', 'Dhoni', 'suresh raina', 'W sundar']
>>> names[3]
'W sundar'
>>> names[4]

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    names[4]
IndexError: list index out of range
>>> names[5]

Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    names[5]
IndexError: list index out of range
>>> names[4]

Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    names[4]
IndexError: list index out of range
>>> names[3]
'W sundar'
>>> names[-1]
'W sundar'
>>> names[-2]
'suresh raina'
>>> names[-3]
'Dhoni'
>>> names[-4]
'ram'
>>> names[-4]
'ram'
>>> names
['ram', 'Dhoni', 'suresh raina', 'W sundar']
>>> names
['ram', 'Dhoni', 'suresh raina', 'W sundar']
>>> names[-1]
'W sundar'
>>> names.index(names[-1])
3
>>> 1+int(names.index(names[-1]))
4
>>> names.append('Dhoni')
>>> names
['ram', 'Dhoni', 'suresh raina', 'W sundar', 'Dhoni']
>>> 1+int(names.index(names[-1]))
2
>>> names[-1]
'Dhoni'
>>> names
['ram', 'Dhoni', 'suresh raina', 'W sundar', 'Dhoni']
>>> names
['ram', 'Dhoni', 'suresh raina', 'W sundar', 'Dhoni']
>>> names.sort()
>>> names
['Dhoni', 'Dhoni', 'W sundar', 'ram', 'suresh raina']
>>> names.reverse()
>>> names
['suresh raina', 'ram', 'W sundar', 'Dhoni', 'Dhoni']
>>> names.append('arun')
>>> names
['suresh raina', 'ram', 'W sundar', 'Dhoni', 'Dhoni', 'arun']
>>> 
