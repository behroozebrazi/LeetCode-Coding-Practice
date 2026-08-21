# https://leetcode.com/problems/minimum-genetic-mutation

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        genes = "ACGT"
        bank = set(bank)

        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        visited = set([startGene])

        while queue:
            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for i, ch in enumerate(gene):
                for g in genes:
                    if g == ch:
                        continue

                    new_gene = gene[:i] + g + gene[i + 1:]

                    if new_gene in bank and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, mutations + 1))

        return -1