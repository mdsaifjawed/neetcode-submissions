class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    if i > j:
                        L.append(j)
                        L.append(i)
                        return L
                    else:
                        L.append(i)
                        L.append(j)
                        return L
        

        