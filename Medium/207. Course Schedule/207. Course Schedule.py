# https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 0 = not visited
        # 1 = currently visiting
        # 2 = completely processed
        state = [0] * numCourses

        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        def dfs(course):
            # We found a cycle
            if state[course] == 1: return False

            # Already processed successfully
            if state[course] == 2: return True

            # Mark as currently visiting
            state[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            # Finished processing this course
            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True