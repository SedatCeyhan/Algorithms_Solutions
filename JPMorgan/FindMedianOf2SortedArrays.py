import math

def findMedianSortedArrays(nums1, nums2):
    if not nums1 and not nums2: return 0
    n, m = len(nums1), len(nums2)

    if n > m:
        temp = nums1
        nums1 = nums2
        nums2 = temp
        n, m = m, n

    # We know nums1 is the smaller array now
    half = int(math.ceil((n + m) / 2))
    min_nums1, max_nums1 = 0, n
    while min_nums1 <= max_nums1:
        i = int((min_nums1 + max_nums1) / 2)
        j = half - i
        print(i)
        print(j)
        if i < n and nums2[j - 1] > nums1[i]:
            min_nums1 += 1

        elif i > 0 and nums1[i - 1] > nums2[j]:
            min_nums1 -= 1

        else:
            if i == 0:
                max_left = nums2[j - 1]
            elif j == 0:
                max_left = nums1[i - 1]
            else:
                max_left = max(nums1[i - 1], nums2[j - 1])
            if (n + m) % 2 == 1:
                return max_left
            else:
                if i == n:
                    return (max_left + nums2[j]) / 2
                elif j == m:
                    return (max_left + nums1[i]) / 2
                else:
                    return (max_left + min(nums1[i], nums2[j]))/2

print(findMedianSortedArrays([1,3], [2,7]))


