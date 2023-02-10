# for basic examples
for i in range (99):
    print(i, end = ' ') 

print("\n++++++++++++++++++++++++++++++++++++++++")

for i in range (3 ,8):
    print(i , end= " ")
    
print("\n++++++++++++++++++++++++++++++++++++++++")

for i in range (3, 15, 3):
    print(i, end=" ")
    
print("\n++++++++++++++++++++++++++++++++++++++++")

for i in ("mahdi"):
    print(i)

print("\n++++++++++++++++++++++++++++++++++++++++")
for _ in range(9):
    print("Mahdi", end = " ")
    
print("\n++++++++++++++++++++++++++++++++++++++++")
for i in range (9, 1, -3):
    print(i, end= " ")
print("\n++++++++++++++++++++++++++++++++++++++++")

a = "Mahdi Mohammadiyazani"
b = 0
for i in a:
    b += 1
print(b)

print("\n++++++++++++++++++++++++++++++++++++++++")

a = "Mahdi Mohammadiyazani"
b = 0
for i in a:
 if i == "i":
  b += 1
print(b)

print("\n++++++++++++++++++++++++++++++++++++++++")

name = "Mahdi Mohammadiyazani"
vowel = "aiuoe"
c = 0
for i in name:
    if i in  vowel:
        print(i, end= " ") 
        c+= 1
print()
print(c)

print("\n++++++++++++++++++++++++++++++++++++++++")

x = [i for i in name if i in vowel]
print(x)

print("\n++++++++++++++++++++++++++++++++++++++++")

#Nested fors basic examples

for i in range (1, 4):
    for j in range (2, 4):
        print(j, end=" ")
    print('\n')
    
print("\n++++++++++++++++++++++++++++++++++++++++")

for i in range (1, 4):
    for j in range (2, 4):
        print(i, end=" ")
    print()
    
print("\n++++++++++++++++++++++++++++++++++++++++")

for i in range (2, 5):
    for j in range (i):
        print(j, end=" ")
    print()
    
print("\n++++++++++++++++++++++++++++++++++++++++")

for i in range (2, 9):
    for j in range (1, i):
        print(j, end=" ")
    print()
    
print("\n++++++++++++++++++++++++++++++++++++++++")


print("\n #Break")

for i in range(5):
    if i == 3:
        break
    else:
        print(i, end= " ")
        
print("\n #continue")

for i in range(5):
    if i == 3:
        continue
    else:
        print(i, end= " ")

print("\n++++++++++++++++++++++++++++++++++++++++")

for i in range (10, 15):
    for j in range (2, i):
        if i % j == 0:
         print(i)
        break
    
print("\n++++++++++++++++++++++++++++++++++++++++")

for i in range (3, 8):
    for j in range (2, i):
        if i % j == 0:
         break
    else:
        print(i, end(" "))
        

        


