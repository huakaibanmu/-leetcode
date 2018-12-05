class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        s = len(nums1)+len(nums2)
        if(s%2==0):
            return (self.binary_search(0,nums1,0,nums2,s//2)+self.binary_search(0,nums1,0,nums2,s//2+1))/2
        else:
            return self.binary_search(0,nums1,0,nums2,s//2+1)
        #定义跳出条件
    def binary_search(self,i,nums_1,j,nums_2,k):#  i为nums_1可比较元素序列最左端的索引，j为nums_2可比较元素序列最左端的索引，k为在nums_1和nums_2里，要取第几大的数
        len1= len(nums_1)
        len2 = len(nums_2)
        if(i >= len1):#将越界范围判断放到最前面，注意这里返回的是一个数
            return nums_2[j+k-1]
        if(j >= len2):
            return nums_1[i+k-1]
        if(k==1):
            return nums_1[i] if nums_1[i]<nums_2[j] else nums_2[j]

        m = i+k//2-1 #i 和 m 分别是从nums_1中取出来k个元素的左右两端索引值，即取出nums_1[i]...nums_1[m],注意判断m或者n超出数组范围的情况
        n = j + k//2-1#i 和 n 分别是从nums_2中取出来k个元素的左右两端索引值，即取出nums_2[j]...nums_2[n]
        p1 = nums_1[m] if m<len1 else 100000000#防止越界
        p2 = nums_2[n] if n<len2 else 100000000
        if(p1< p2):
            return self.binary_search(m+1,nums_1,j,nums_2,k-k//2)#逻辑为王
        else:
            return self.binary_search(i,nums_1,n+1,nums_2,k-k//2)
