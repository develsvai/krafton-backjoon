class UnionFind:
    def __init__(self, n):
        # 각 노드의 부모를 가리키는 배열을 초기화한다.
        # 처음에는 모든 정점이 자기 자신을 부모로 가지므로,
        # parent[i] = i 로 초기화된다.
        self.parent = list(range(n))

        # 각 정점의 랭크(트리의 깊이)를 나타내는 배열을 초기화한다.
        # 초기에는 모든 트리의 높이가 1이므로 rank[i] = 1 로 초기화된다.
        # rank 는 각 노드의 우선 순위를 말한다.
        self.rank = [1] * n

    def find(self, u): # 노드의 부모를 찾는 메소드
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v): # 두 간선을 하나로 합치는 부분
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal(V, edges):
    uf = UnionFind(V)
    edges.sort(key=lambda x: x[2])#w(가중치) 를 기준으로 edges 를 정렬
    mst_weight = 0 # 총 가중치 초기화
    mst_edges = 0 # 총 간선 초기화

    for u, v, weight in edges:
        u -= 1  # 1-indexed에서 0-indexed로 맞추기 위해
        v -= 1  # 1-indexed에서 0-indexed로 맞추기 위해
        if uf.find(u) != uf.find(v): # u와 v 가 같은 그룹 인지 확인 , 만약 서로 다른 그룹 이라면
            uf.union(u, v) # 서로 같은 그룹으로 합친다.
            mst_weight += weight #mst 의 총 가중치에 누적 합계
            mst_edges += 1 #mst에 포함 된 간선의 개수 누적 합계
            if mst_edges == V - 1: # mst의 간선의 개수가 v(노드의 수) 와 동일한지 확인하여 mst가 완성되었는지 확인
                break # 완성 되었으면 탈출

    return mst_weight


if __name__ == "__main__":
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        A, B, C = map(int, input().split())
        edges.append((A, B, C))

    result = kruskal(V, edges)
    print(result)
