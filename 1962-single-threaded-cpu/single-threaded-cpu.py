class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minheap = []
        extendtask = []
        for i in range(len(tasks)):
            extendtask.append([tasks[i][0],tasks[i][1],i])
        extendtask.sort(key = lambda x:x[0])
        curstart = 0
        curidx = 0
        res = []
        while curidx < len(tasks) or minheap:
            if not minheap and curstart < extendtask[curidx][0]:
                curstart = extendtask[curidx][0]
            while curidx < len(tasks) and extendtask[curidx][0] <= curstart:
                heapq.heappush(minheap,(extendtask[curidx][1],extendtask[curidx][2]))
                curidx += 1
            processtime, originidx = heapq.heappop(minheap)
            curstart += processtime
            res.append(originidx)
        return res