# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1

from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1  # If endGene is not in the bank, mutation is impossible
        
        bank_set = set(bank)  # Convert bank list to set for quick lookup
        queue = deque([(startGene, 0)])  # BFS queue with (gene, mutation_count)
        gene_chars = ['A', 'C', 'G', 'T']  # Possible mutations

        while queue:
            current, mutations = queue.popleft()

            if current == endGene:
                return mutations  # Found the shortest path

            # Try mutating each character in the gene string
            for i in range(len(current)):
                for char in gene_chars:
                    if char != current[i]:  # Ensure mutation
                        mutated_gene = current[:i] + char + current[i+1:]
                        if mutated_gene in bank_set:
                            queue.append((mutated_gene, mutations + 1))
                            bank_set.remove(mutated_gene)  # Avoid revisiting

        return -1  # No valid mutation path