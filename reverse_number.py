def reverse(n):
    rev=0

    while n!=0:
        d = n%10
        rev = rev*10+d
        n//=10

    return rev

print(reverse(24567))


def reverse_positiveAnd_NegativeNo(input, rinput=0):
    if input<0:
        input=input-(input*2)
        print(-reverse(input))
    else:
        print(reverse(input))

reverse_positiveAnd_NegativeNo(-123)