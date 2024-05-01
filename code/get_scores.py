import math
def handle_data(file_path):
    item_count = {}
    with open(file_path,'r') as f:
        for l in f.readlines():
            if len(l) > 0:
                l = l.strip('\n').split(' ')
                # 获取所有的物品除去用户
                items = [int(i) for i in l[1:]]
                for i in items:
                    if i in item_count:
                        item_count[i]['count'] += 1
                    else:
                        item_count[i] = {'count':1,'scores':0}
    # 权重分数计算
    yuzhi = 2.197 # 阈值
    w = 0.5 # 奖惩权重
    for key, value in item_count.items():
        # print(key,value)
        x = math.atan(value['count'])
        pi = math.log(yuzhi,math.e)
        if x > pi:
            s = x - w*pi
        else:
            s = x + w*pi
        item_count[key]['scores'] = round(s,5)
    return item_count


# result = handle_data(train_file)

# print(f"结果-->{result}")