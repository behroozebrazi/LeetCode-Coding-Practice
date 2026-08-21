# https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node == None:
            return

        nodeList = []
        visited = dict()
        stack = [node]

        while stack:
            curr = stack.pop()

            if curr not in visited:
                visited[curr] = len(nodeList)
                nodeList.append(curr)

                if curr.neighbors:
                    stack.extend(curr.neighbors)

        newGraph = [Node(n.val) for n in nodeList]

        for i, n in enumerate(nodeList):
            if n.neighbors:
                for neighbor in n.neighbors:
                    index = visited[neighbor]
                    newGraph[i].neighbors.append(newGraph[index])
 
        return newGraph[0]