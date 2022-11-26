def ispalindrome(num):
    x=num
    reverse=0
    while (x!=0):
        rem=x%10
        reverse=reverse*10+rem
        x=x//10
    if num==reverse:
        return True
    else :
        return False

def isprime(n):
    x=True
    for i in range(2,n):
        if n%i==0:
            x=False
            break
    return x

n=int(input("Give Nth value:"))
primeAndPalindrome=[]
p=10**n
for i in range (2,p):
    if ispalindrome(i) and isprime(i):
        primeAndPalindrome.append(i)
    if len(primeAndPalindrome)==n+1:
        break
print(f'{n}th prime palindrome number is {primeAndPalindrome[n-1]}')


