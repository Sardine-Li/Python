xiaoming_dic = {"name": "小明", 
            "age": 18, 
            "gender": True, 
            "height": 1.75}

# 1、从字典中取值
print(xiaoming_dic["name"])

# 2、增加/修改
xiaoming_dic["age"] = 19
xiaoming_dic["name1"] = "小小明"

# 3、删除
xiaoming_dic.pop("name")

# 统计键值对数量
print(len(xiaoming_dic))

# 合并字典
temp_dic = {"weight": 70, "height": 176}
xiaoming_dic.update(temp_dic)

print(xiaoming_dic)

for keys in xiaoming_dic:
    print("%s: %s" % (keys, xiaoming_dic[keys]))

print("%s 的年龄是%s, 身高是%s" % (xiaoming_dic["name1"], xiaoming_dic["age"], xiaoming_dic["height"]))