# You pass an array in, and it gets converted to a set.
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

stations = dict()
stations["kone"] = {"id", "nv", "ut"}
stations["ktwo"] = {"wa", "id", "mt"}
stations["kthree"] = {"or", "nv", "ca"}
stations["kfour"] = {"nv", "ut"}
stations["kfive"] = {"ca", "az"}

final_stations = set()

while states_needed:  # 集合非空
    best_station = None  # 最优站点-覆盖最多
    states_covered = set()  # 覆盖区域
    for station, states_for_station in stations.items():  # 遍历站点
        covered = states_needed & states_for_station  # 新覆盖区域
        if len(covered) > len(states_covered):  # 找出最优站点及最优覆盖
            best_station = station
            states_covered = covered

    states_needed -= states_covered  # 移除被覆盖的区域
    final_stations.add(best_station)  # 结果中加入最优站点

print(final_stations)
