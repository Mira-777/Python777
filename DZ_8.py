a = ('ab', 'abcd', 'cde', 'abc', 'def')
s = str(input("s = "))
i = 0
for a_ in a:
    if a_ == s:
        print("Yes")
        i =+ 1
        break
if s not in a:
    print("No")