'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

for i in range(0,5):
    for j in range(0,5):
        if (i>=j):
            print("* ", end=" ")
    print("\r")
for i in range(4,0,-1):
    for j in range(0,i):
        if (i>=j):
            print("* ", end=" ")
    print("\r")

'''Take input from user and return in reverse order'''

input_user = input(" write here ")
rev_input = ""
for i in range(0,len(input_user)):
    rev_input = rev_input + input_user[(len(input_user)-1)-i]

print(rev_input)







