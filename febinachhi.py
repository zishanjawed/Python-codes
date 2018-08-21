def febi(n,d):
    if n in d:
        return d[n]
    else:
        ans = febi(n-1,d)+febi(n-2,d)
        d[n] = ans
        return ans
d = {1:1,2:2}
n = input("Enter the number : ")
print(febi(n,d))
