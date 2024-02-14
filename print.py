#Python is an interpreted language
#man language -> compiler(execute at last)/interpreter(execute at a time) -> machine language

#To get rid of repetative code usage, we create function.

#function(string arg)
print('Life is lovely...!!!') 

#seperate line
print('''Mohammed 
      Faisal ''')

#Escape char won't print char, will print functionality(space here)
print('\a')

#new line
print('\n')

#tab space 
print('\t')

#Arguments - seperation arg, end arg

#Seperation arg (default space)
print('hello', 'world', sep='_')

#end arg (using the \n)
print("Mohammed Faisal")
print('hello', 'world', sep='_', end= '\t')
print("Mohammed Faisal")

#String replication
print("Keep the faith alive..!! " * 3)

#String concat 
print("Mohammed " + 'Faisal')


# example
str1 = 'code'
str2 = 'io'
print(str1, '.', sep=' ', end='')
print(str2)