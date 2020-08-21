ask = int(input("How many rows of asterisks would you like? "))
for i in range(1,ask +2):  
  for j in range(1,i):
    print("*", end =" ")
  print()

for i in range(1,7):
    for j in range(1,i):
        print(j, end=" ")
    print()

print()
word = (input("Enter a word: "))
l=len(word)

print()
for i in range(0,l+1):
    for j in range(0,i):
        print(word[j], end=" ")
    print()

