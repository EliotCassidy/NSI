def palindrome(word: str) -> bool:
    filterd_text = "".join(i.lower() for i in word if i.isalpha())
    if len(filterd_text) < 2:
        return True
    return filterd_text[0] == filterd_text[-1] and palindrome(filterd_text[1:-1])

print(palindrome("No lemon, no melon!"))