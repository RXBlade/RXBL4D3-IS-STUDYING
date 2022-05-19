############### THE OLD FASHIONED WAY ##############

def sum(a,b):
    return a + b

a = 1
b = 2
c = sum(a,b)
print(c)

############## THE LAMBDA WAY ##################

a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)