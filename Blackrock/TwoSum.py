
# public int[] twoSum(int[] nums, int target) {
#     Map<Integer, Integer> map = new HashMap<>();
#     for (int i = 0; i < nums.length; i++) {
#         int complement = target - nums[i];
#         if (map.containsKey(complement)) {
#             return new int[] { map.get(complement), i };
#         }
#         map.put(nums[i], i);
#     }
#     throw new IllegalArgumentException("No two sum solution");
# }


def twoSum(nums, target):
    numToIdx = {}
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in numToIdx:
            return [numToIdx[comp], i]
        numToIdx[nums[i]] = i
    return []