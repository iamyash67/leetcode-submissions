class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {}
        minheap = []
        for num in nums:
            if num in countmap:
                countmap[num] += 1
            else:
                countmap[num] = 1

        for num, count in countmap.items():
            heapq.heappush(minheap, (count,num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        result = []
        for count,num in minheap:
            result.append(num)
        return result

        