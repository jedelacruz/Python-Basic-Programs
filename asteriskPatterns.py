#asterisk patterns in python

print("============= ASTERISK PATTERNS =============")
print()
"""""
*
**
***
****
*****
"""""

for i in range(1,6):
    print("*" * i)

print()

"""""
*****
****
***
**
*
"""""

for i in range(5,0,-1):
    print("*" * i)

print()

"""""
    *
   ***
  *****
 *******
"""""

for i in range(1,5):
    print(" " * (4 - i) + "*" * (2 * i - 1))


print()

"""""
    *
   ***
  *****
 *******
  *****
   ***
    *
"""""

for i in range(1,5):
    print(" " * (4 - i) + "*" * (2 * i - 1))

for i in range(3,0,-1):
    print(" " * (4 - i) + "*" * (2 * i - 1))
