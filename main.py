def medians(nums1, nums2):
    nums = sorted(nums1 + nums2)
    if len(nums) % 2 == 0:
        ind = int(len(nums)/2)
        median = (nums[ind - 1] + nums[ind])/2
    else:
        ind = int(len(nums)/2)
        median = nums[ind]
    return median


while True:
    print("Вход (введите значения списка через пробел): ")
    nums1 = [int(i) for i in input('nums1 = ').split()]
    nums2 = [int(i) for i in input('nums2 = ').split()]
    print("Вывод: ", medians(nums1, nums2))
