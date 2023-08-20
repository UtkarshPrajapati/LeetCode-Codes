class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topoSort(nodes, graph, in_degree):
            queue = deque([node for node in nodes if node not in in_degree])
            ans = []
            while queue:
                cur_node = queue.popleft()
                ans.append(cur_node)
                for neighbor in graph[cur_node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0: queue.append(neighbor)
            return ans
        grp_i = defaultdict(list)
        groupId = m
        for i in range(n):
            if group[i] == -1:
                group[i] = groupId
                groupId += 1
            grp_i[group[i]].append(i)
        item_graph = defaultdict(list)
        item_indegree = defaultdict(int)
        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] == group[v]:
                    item_graph[u].append(v)
                    item_indegree[v] += 1
        grp_i_sort = {}
        for groupId in grp_i:
            sorted_items = topoSort(grp_i[groupId], item_graph, item_indegree)
            if len(sorted_items) != len(grp_i[groupId]): return []
            grp_i_sort[groupId] = sorted_items
        group_graph = defaultdict(list)
        group_indegree = defaultdict(int)
        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] != group[v]:
                    group_graph[group[u]].append(group[v])
                    group_indegree[group[v]] += 1
        groups = set(group)
        sorted_groups = topoSort(groups, group_graph, group_indegree)
        if len(groups) != len(sorted_groups): return []
        return [item for groupId in sorted_groups for item in grp_i_sort[groupId]]