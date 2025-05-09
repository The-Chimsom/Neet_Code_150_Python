# first trial
def isPalindrome(s: str) -> bool:
    n = ''.join(char.lower() for char in s if char.isalnum() )
    revInput = str[::-1]
    if revInput == n:
        return True
    return False