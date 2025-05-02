def isAnagram(s: str, r: str) -> bool:
    if len(s) != len(r):
        return False
    return sorted(s) == sorted(r)

isAnagram("race", "care")