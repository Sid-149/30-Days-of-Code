# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())

for i in range(t):
    str1=''
    str2=''
    s=input()
    for j in range(len(s)):
        if j%2==0:
            str1=str1+s[j]
        else:
            str2=str2+s[j]
    print(str1,str2)
