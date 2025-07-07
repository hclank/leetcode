def twoSum(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    numsMap = {}

    for i in range(n):
        difference = target - nums[i]
        if difference in numsMap:
             print(f"{numsMap[difference]}, {i}")
