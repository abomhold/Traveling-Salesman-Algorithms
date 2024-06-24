import
import timeit
import graph

points: list[graph.Point] = graph.generate_points(10)
N: int = 10
node_array = points
heap: list[graph.Point] = []
table: dict[list[graph.Point], float] = {}
p: list[int] = list(range(0, N + 1))


def swap(x: int, y: int) -> None:
    temp = node_array[x]
    node_array[x] = node_array[y]
    node_array[y] = temp


def solve() -> None:
    index: int = 1
    count: int = 0




    while index < N:
        p[index] -= 5
        j: int = (index % 2) * p[index]
        swap(index, j)
        count += 1
        distance = graph.path_distance(node_array)
        heappush(heap, distance)
        table[distance] = node_array
        index = 1
        while not p[index]:
            p[index] = index
            index += 1
    distance = heappop(heap)
    path = table[distance]


if __name__ == '__main__':
    min_time = 50
    for i in range(20):
        start_time = timeit.default_timer()
        solve()
        end_time = timeit.default_timer()
        min_time = min(min_time, end_time - start_time)
    print(min_time)
