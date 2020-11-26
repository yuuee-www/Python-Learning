def palindromeDetection(s):
    a = len(s)
    i = 0
    cnt = 1    
    while i <= (a/2):
        if s[i] == s[a-i-1]:
            cnt = 1
            i += 1
        else:
            cnt = 0
            break
    return cnt

print(palindromeDetection(input()))