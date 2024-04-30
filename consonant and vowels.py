# Given an alphanumeric string, find the sum of those numbers whose preceding
# character should be consonant or exceeding character should be vowels.
# Note : If any one of the condition is true you should consider that number
# If no numbers satisfy the condition return 0. An alphanumeric string is a string which
# contains alphabets and numbers combined.

lst=str(input("Enter the string"))
vowel=['A','E','I','O','U']
count=[]
res=[]
for i in range (len(lst)):
    if lst[i].isdigit() :
        if lst[i-1] not in vowel or lst[i+1] in vowel:
            while lst[i].isdigit():
                res.append(lst[i])
                i+=1
            n=len(res)-1
            count.append(res[0:n])
            res.clear()




            # for j in range(i,len(lst)):
            #     if lst[j].isdigit() and lst[j+1].isalpha() :
            #         res.append(lst[i:j])
print(count)


