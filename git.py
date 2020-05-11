print('My first git file')

print("my second change to this file")

# Just assigning variable name to equal myName
name = input("Input a name(Default, if you type in myName it will print correct statement): ")

# Because myName is true, it will print whatever is under the if block
if name == 'myName':
  print('Statement for name is true')
# if you change name to equal something other than myName, the else block will print
else:
  print(f'{name} not found')
  
i = 0
while(i <5):
  print('Current i is: ' + i)
  # Then we add 1 to i, so that it can reach 5 to end the loop
  # i += 1 is the same as doing i = i + 1
  i += 1
