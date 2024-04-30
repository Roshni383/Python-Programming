def palindrome(str):
    for i in range(0, int((len(str)) / 2)):
        if str[i] != str[len(str) - i - 1]:
            if str[i] != str[int((len(str)) / 2)]:
                return False
        else:
            return True
inp = str(input())
ans = palindrome(inp)
if ans == True:
    print('The string is palindrome')
if ans == False:
    print('The string is symmetrical')


def is_palindrome(word):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_word = ''.join(word.split()).lower()

    return cleaned_word == cleaned_word[::-1]

