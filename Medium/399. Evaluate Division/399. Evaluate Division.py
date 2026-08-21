# https://leetcode.com/problems/evaluate-division

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        visited = set()

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        def dfs(current, target, product):
            if current == target:
                return product

            visited.add(current)

            for neighbor, weight in graph[current]:
                if neighbor not in visited:
                    answer = dfs(neighbor, target, product * weight)

                    if answer != -1:
                        return answer

            return -1

        result = []

        for start, end in queries:
            if start in graph and end in graph:
                visited.clear()
                result.append(dfs(start, end, 1.0))
            else:
                result.append(-1.0)

        return result