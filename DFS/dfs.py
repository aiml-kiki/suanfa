from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()   # 双端队列保存节点
    search_queue += graph[name]
    # 保存已检查过的节点
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        # 查询未检查过的节点
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]  # 将新的节点信息加入队列
                # 标记检查过的节点
                searched.add(person)
    return False


graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
search("you")
