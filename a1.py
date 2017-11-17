strin=input("Enter the string you want to check")
i=0 
p=0
j=0
k=0
while(i<len(strin)):
    if(strin[i]=='{'):
        p=p+1
    elif(strin[i]=='}'):
        p=p-1
    elif(strin[i]=='('):
        j=j+1
    elif(strin[i]==')'):
        j=j-1
    elif(strin[i]=='['):
        k=k+1
    elif(strin[i]==']'):
        k=k-1
    i=i+1
if(p==0 and j==0 and k==0):
    print("the paranthesis are balanced")    
else:
    print("the paranthesis are  not balanced")
