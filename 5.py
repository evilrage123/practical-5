# given year is leap year or not
fh = open('pactical5.txt','w')
a=int(input('Enter a number:'))
b=a%4
if(b==0):
    fh.write('leap year')
else:
    fh.write('not leap year')
