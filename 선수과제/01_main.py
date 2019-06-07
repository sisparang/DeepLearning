def is_palindrome(word):
    list_word = list(word)
    for i in range(0, len(list_word) // 2) :
        if list_word[i] == list_word[len(list_word) -1 -i]:
            continue
        else:
            return False

    return True
        

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))