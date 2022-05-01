l = [2,4,7,3,14,19]
for i in l:
    # your code here
    odd = lambda x : x % 2
    if odd(i) != 0:
        print("True")
    else:
        print("False")
    