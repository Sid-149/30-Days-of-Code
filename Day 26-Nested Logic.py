# Enter your code here. Read input from STDIN. Print output to STDOUT
Actual_Date = str(input()).split(' ')
Da = int(Actual_Date[0])
Ma = int(Actual_Date[1])
Ya = int(Actual_Date[2])

Expected_Date = str(input()).split(' ')
De = int(Expected_Date[0])
Me = int(Expected_Date[1])
Ye = int(Expected_Date[2])

fine = 0

if Ya > Ye:
    fine = 10000
elif Ya == Ye:
    if Ma > Me:
        fine = (Ma - Me) * 500
    elif Ma == Me and Da > De:
        fine = (Da - De) * 15

print(fine)
