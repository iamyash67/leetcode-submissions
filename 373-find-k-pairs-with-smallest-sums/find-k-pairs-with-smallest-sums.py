class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        minheap = []
        for i in range(min(len(nums1),k)):
            cursum = nums1[i] + nums2[0]
            heapq.heappush(minheap, (cursum, i ,0))

        res_list = []
        while len(minheap) > 0 and len(res_list) < k:
            totalsum, nums1idx, nums2idx = heapq.heappop(minheap)
            res_list.append([nums1[nums1idx],nums2[nums2idx]])
            nextnum2idx = nums2idx + 1
            if nextnum2idx < len(nums2):
                nextsum = nums1[nums1idx] + nums2[nextnum2idx]
                heapq.heappush(minheap, (nextsum, nums1idx , nextnum2idx))

        return res_list
        