# 定义图
graph = dict()
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# 花费
infinity = float("inf")
costs = dict()
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# 父节点
parents = dict()
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # 遍历每个节点
    for node in costs:
        cost = costs[node]
        # 如果节点为花费最少接待你而且没被检查过
        if cost < lowest_cost and node not in processed:
            # 把它最为新的最小花费节点
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 找到未处理节点中最小花费节点
node = find_lowest_cost_node(costs)
# 遍历整个图
while node is not None:
    cost = costs[node]
    # 找到节点的所有邻居
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # 经该节点到邻居花费更小
        if costs[n] > new_cost:
            # 更新邻居节点的开销
            costs[n] = new_cost
            # 将邻居节点父节点设置为当前节点
            parents[n] = node
    # 标记当前节点
    processed.append(node)
    # 找到接下来要处理的节点，并循环
    node = find_lowest_cost_node(costs)

print("Cost from the start to each node:")
print(costs)

