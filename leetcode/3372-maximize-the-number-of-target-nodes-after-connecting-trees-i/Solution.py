class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        def build_adj(size, edges):
            adj = [[] for _ in range(size)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def count_nodes(start, max_dist, adj):
            if max_dist < 0:
                return 0
            
            queue = deque([(start, 0)])
            visited = {start}
            count = 0
            
            while queue:
                node, dist = queue.popleft()
                count += 1
                
                if dist < max_dist:
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append((neighbor, dist + 1))
            return count

        adj1 = build_adj(n, edges1)
        adj2 = build_adj(m, edges2)

        max_from_tree2 = max((count_nodes(j, k - 1, adj2) for j in range(m)), default=0)
        return [count_nodes(i, k, adj1) + max_from_tree2 for i in range(n)]
