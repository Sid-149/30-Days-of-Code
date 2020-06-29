# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
phoneBook=dict()
for i in range(n):
    name,phoneNumber=input().split()
    phoneBook[name]=phoneNumber
while True:
    try:
        query=input()
        if query in phoneBook.keys():
            print(query+'='+phoneBook[query])
        else:
            print('Not found')
    except EOFError:
        break
