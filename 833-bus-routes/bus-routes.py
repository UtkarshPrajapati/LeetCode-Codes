class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target: return 0
        max_stop = max(max(route) for route in routes)
        if max_stop < target: return -1
        min_buses_to_reach = [float('inf')] * (max_stop + 1)
        min_buses_to_reach[source] = 0
        while True:
            prev = list(min_buses_to_reach)
            for route in routes:
                mini = min(min_buses_to_reach[stop] for stop in route) + 1
                for stop in route:
                    min_buses_to_reach[stop] = min(min_buses_to_reach[stop], mini)
            if prev == min_buses_to_reach: break
        return min_buses_to_reach[target] if min_buses_to_reach[target] < float('inf') else -1