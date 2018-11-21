#   1.已知有两个等长的列表
#      list1 = [1001, 1002, 1003, 1004]
#      list2 = ["Tom", "Jerry", "Spike", "Tyke"]
#     写程序生成如下字典:
#       {"Tom": 1001, "Jerry":1002, "Spike":1003, "Tyke": 1004}

list1 = [1001, 1002, 1003, 1004]
list2 = ["Tom", "Jerry", "Spike", "Tyke"]

# d = {}
# for i in range(len(list1)):
#     d[list2[i]] = list1[i]

d = {list2[i]: list1[i]
     for i in range(len(list1))}

print(d)

