# https://leetcode.com/problems/course-schedule-ii

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = []
        indegree = []
        order = []
        queue = deque()

        for _ in range(numCourses):
            graph.append([])
            indegree.append(0)

        for course, prerequisite in prerequisites:
            # prerequisite -> courses that depend on it
            graph[prerequisite].append(course)
            # Number of prerequisites for each course
            indegree[course] += 1

        # Courses with no prerequisites can be taken first
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            order.append(course)

            # Remove this course as a prerequisite
            for next_course in graph[course]:
                indegree[next_course] -= 1

                # All prerequisites are now satisfied
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # If we couldn't process every course, there is a cycle
        return order if len(order) == numCourses else []