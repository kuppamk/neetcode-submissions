class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = [(task[0], task[1], i ) for i, task in enumerate(tasks)]
        indexed_tasks.sort()
        current_time = 0
        avail_tasks = []
        output = []
        task_index = 0
        while task_index < len(tasks) or avail_tasks:
            while  task_index < len(tasks) and indexed_tasks[task_index][0] <= current_time:
                _, proc_time, idx = indexed_tasks[task_index]
                heapq.heappush(avail_tasks, (proc_time, idx))
                task_index += 1
            if avail_tasks:
                proc_time, idx = heapq.heappop(avail_tasks)
                current_time += proc_time
                output.append(idx)
            else:
                if task_index < len(tasks):
                    current_time = indexed_tasks[task_index][0]
        return output

            


        