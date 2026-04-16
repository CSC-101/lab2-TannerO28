def checked_access(L:list[int], idx:int)->[int]:
    test= idx >=0 and idx < len(L) #Test is False on first call, and true on second call
    if test: #This check is preventing test returning True/False
        return L[idx]
    else:
        return None

first = checked_access([1, 0, 1], 9) #first = None
second = checked_access([1, 0, 1], 2) #Second = 1
print(first)
print(second)

def length_sum(L:list[str])->int:
    if len(L)> 2:
        result = len(L[0]) + len(L[1]) + len(L[2]) # evaluated in first call, values added are the length of the string in the 0 1 and 2 spot in list
    elif len(L) > 1:
        result = len(L[0]) + len(L[1]) #evaluated in third call, values added are length of string in 0 and 1 of list
    elif len(L) > 1:
        result = len(L[0]) #evaluated in second call, value is length of the 0 in list
    else:
        result = 0
    return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print(first)
print(second)
print(third)

def suprising(L: list[str], other:str)->list[str]:
    L.append(other.upper())
    return L

words = ["this", "is", "confusing", "code."]
first = suprising(words, "Avoid")
second = suprising(words, "such.")
#Words is ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
#First and second are the same at this point, just has two names
#Function suprsing appends the "AVOID" in first call and then "SUCH." in second call
print(first)
print(second)