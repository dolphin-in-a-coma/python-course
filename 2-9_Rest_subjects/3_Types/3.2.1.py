a=int(input('первое число='))
b=int(input('второе число='))
print("a+b:  {}\na-b:  {}\na*b:  {}\na/b:  {:.2f}\n\
a//b: {}\na%b:  {}\na^b:  {}"
.format(a+b,a-b,a*b,a/b,a//b,a%b,a**b))
print('a<b: ',a<b,'\na<=b:',a<=b,'\na>b: ',a>b,'\na>=b:',a>=b,'\na!=b:'
,a!=b,'\na==b:',a==b)
