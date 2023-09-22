def is_palindrome(text):
    text = text.upper()
    return text == text[::-1]



if __name__ == "__main__":
    print("Ingrese una palabra")
    text = input()
    very = is_palindrome(text)
    
    if very == True:
        print(f"La palabra {text} es palindromo")
    else:
        print(f"La palabra {text} no es palindromo")