# Записати в стрічку філософію Пайтона 

philosophy = """Beautiful is better than ugly.
Explicit is better than implicit."
Simple is better than complex.  
Complex is better than complicated. 
Flat is better than nested. 
Sparse is better than dense. 
Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. 
Errors should never pass silently. 
Unless explicitly silenced. 
In the face of ambiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than right now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea. 
NameSpaces are one honking great idea -- let's do more of those!"""

# Знайти в заданій стрічці кількість входжень слів (better, never, is)
word = 'better never is'.split()
i = len(word)-1

while i >= 0:
    print('Слово {0} зустрічається {1} раз'.format(word[i], philosophy.count(word[i])))
    i -= 1
print(philosophy.upper()) # Вивести весь текст у верхньому регістрі (всі великі літери)
print(philosophy.replace('i', '&')) # Замінити всі входження символу “і” на “&”