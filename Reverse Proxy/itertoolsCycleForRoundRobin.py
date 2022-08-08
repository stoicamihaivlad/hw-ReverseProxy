import itertools
  
  
# List for sequence generation
Inputlist = ['10.0.0.1', '10.0.0.2', '10.0.0.3']
  
# Calling the function Cycle from
# itertools and passing list as 
# an argument and the function 
# returns the iterator object
ipBuffer = itertools.cycle(Inputlist)

def roundRobin(listBuffer):
    return next(listBuffer)


print(roundRobin(ipBuffer))
print(roundRobin(ipBuffer))
print(roundRobin(ipBuffer))
print(roundRobin(ipBuffer))