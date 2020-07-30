import Graph_gen


class Graph:
    def minDistance(self, dist, queue):
        minimum = float("Inf")
        min_index = -1
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index

    def printPath(self, parent, end, path):
        if parent[end] == -1:
            path.append(end)
            return
        self.printPath(parent, parent[end], path)
        path.append(end)

    def dijkstra(self, graph, src, end, path):
        row = len(graph)
        col = len(graph[0])
        dist = [float("Inf")] * row
        parent = [-1] * row
        dist[src] = 0
        queue = []
        for i in range(row):
            queue.append(i)
        while queue:
            u = self.minDistance(dist, queue)
            queue.remove(u)
            for i in range(col):
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u
        self.printPath(parent, end, path)


def give_path(n, src, end, index):
    print("DJkistra")
    g = Graph_gen.baap_baap(n, index)
    path = []
    Graph().dijkstra(g, src, end, path)
    print(path)
    return path
