class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        if source == target: return 0
        maxstop = max(max(route) for route in routes)
        if maxstop < target: return -1
        minbus = [float('inf')] * (maxstop + 1)
        minbus[source] = 0
        while True:
            changes = False
            for route in routes:
                min_route = min(minbus[stop] for stop in route) + 1
                for stop in route:
                    if minbus[stop] > min_route:
                        minbus[stop] = min_route
                        changes = True
            if not changes: break
        return minbus[target] if minbus[target] < float('inf') else -1