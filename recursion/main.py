# Sum of digits -------------------------------------------
def iterativeSum(n):
    total = 0
    n = str(n)
    for i in range(len(n)):
        total += int(n[i])

    return total 

def recursiveSum(n):
    n = str(n)
    if len(n) <= 1:
        return int(n)
    return int(n[0]) + recursiveSum(n[1:])

print(f"""
Sum of Digits:
    Iterative:
        TEST 1: Input: 3 , Output: {iterativeSum(3)}
        TEST 2: Input: 23 , Output: {iterativeSum(23)}
        TEST 3: Input: 5238 , Output: {iterativeSum(5238)}
        TEST 4: Input: 126 , Output: {iterativeSum(126)}
        TEST 5: Input: 293332 , Output: {iterativeSum(293332)}
    Recursive:
        TEST 1: Input: 3 , Output: {recursiveSum(3)}
        TEST 2: Input: 23 , Output: {recursiveSum(23)}
        TEST 3: Input: 5238 , Output: {recursiveSum(5238)}
        TEST 4: Input: 126 , Output: {recursiveSum(126)}
        TEST 5: Input: 293332 , Output: {recursiveSum(293332)}
""")
# Sum of digits -------------------------------------------

# Palindromes ---------------------------------------------
def isPalindrome(text):
    if text.lower() == text[::-1].lower():
        return True

def iterativePalindrome(text):
    total = 0
    for i in range(len(text)):
        for j in range(len(text)+1):
            currText = text[i:j]
            if len(currText) <= 1:
                continue
            if isPalindrome(currText):
                total+=1
    return total

def recursivePalindrome(text):
    total = 0
    if len(text) <= 1:
        return 0
    if isPalindrome(text):
        total += 1
    total += recursivePalindrome(text[1:]) + recursivePalindrome(text[:-1]) - recursivePalindrome(text[1:-1])
    return total

print(f"""
Palindromes:
    Iterative:
        TEST 1: Input: kayak , Output: {iterativePalindrome('kayak')}
        TEST 2: Input: dob , Output: {iterativePalindrome('dob')}
        TEST 3: Input: totally , Output: {iterativePalindrome('totally')}
        TEST 4: Input: ooshishooos , Output: {iterativePalindrome('ooshishooos')}
        TEST 5: Input: aaaazssszaak , Output: {iterativePalindrome('aaaazssszaak')}
    Recursive:
        TEST 1: Input: kayak , Output: {recursivePalindrome('kayak')}
        TEST 2: Input: dob , Output: {recursivePalindrome('dob')}
        TEST 3: Input: totally , Output: {recursivePalindrome('totally')}
        TEST 4: Input: ooshishooos , Output: {recursivePalindrome('ooshishooos')}
        TEST 5: Input: aaaazssszaak , Output: {recursivePalindrome('aaaazssszaak')}
""")
# Palindromes ---------------------------------------------

# Mirrordromes --------------------------------------------
def isMirrordrome(text):
    single = ['i', 'l', 'm', 'n', 'o', 't', 'u', 'v', 'w', 'x']
    double = {'b':'d', 'p':'q', 's':'z'}
    if len(text) == 1:
        if text not in single:
            return False
    else:
        for i in range(len(text)//2):
            if text[i] in single:
                if text[i] != text[-1-i]:
                    return False
            else:
                if text[i] in double.keys():
                    if text[-1-i] != double[text[i]]:
                        return False
                elif text[-1-i] in double.keys():
                    if text[i] != double[text[-1-i]]:
                        return False
                else:
                    return False
    return True

def iterativeMirrordromes(text):
    total = 0
    for i in range(len(text)):
        for j in range(len(text)+1):
            currText = text[i:j]
            if len(currText) < 1:
                continue
            if isMirrordrome(currText):
                total+=1
    return total

def recursiveMirrordromes(text):
    total = 0
    if len(text) < 1:
        return 0
    if isMirrordrome(text):
        total += 1
    total += recursiveMirrordromes(text[1:]) + recursiveMirrordromes(text[:-1]) - recursiveMirrordromes(text[1:-1])
    return total

print(f"""
Mirrordromes:
    Iterative:
        TEST 1: Input: kayak , Output: {iterativeMirrordromes('kayak')}
        TEST 2: Input: dob , Output: {iterativeMirrordromes('dob')}
        TEST 3: Input: totally , Output: {iterativeMirrordromes('totally')}
        TEST 4: Input: zooohzishooos , Output: {iterativeMirrordromes('zooohzishooos')}
        TEST 5: Input: aaszoosk , Output: {iterativeMirrordromes('aaszoosk')}
    Recursive:
        TEST 1: Input: kayak , Output: {recursiveMirrordromes('kayak')}
        TEST 2: Input: dob , Output: {recursiveMirrordromes('dob')}
        TEST 3: Input: totally , Output: {recursiveMirrordromes('totally')}
        TEST 4: Input: zooohzishooos , Output: {recursiveMirrordromes('zooohzishooos')}
        TEST 5: Input: aaszoosk , Output: {recursiveMirrordromes('aaszoosk')}
""")
# Mirrordromes --------------------------------------------

