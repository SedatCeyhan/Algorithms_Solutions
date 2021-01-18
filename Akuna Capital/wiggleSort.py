# def wiggleSort(nums) :
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#
#     nums = sorted(nums)
#     median = nums[int(len(nums)/2)]
#     first_half = nums[:nums.index(median)]
#     second_half = nums[len(nums) - nums[::-1].index(median):]
#     nums[1::2] = second_half
#     if len(nums) % 2 == 0:
#         for i in range(len(nums) - 2, (len(nums) - 2) - 2 * (len(first_half) - 1) - 1, -2):
#             