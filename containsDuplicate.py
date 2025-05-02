def containsDuplicate(nums: list[int]) -> bool:
    Storage = set()
    for i in nums:
        if i in Storage:
            return True
        Storage.add(i)
    return False
