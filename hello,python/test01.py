#coding:utf-8
'''
    1.统计每个人的总得分
'''
with open ('data.txt','r') as f:
    lines = f.readlines()
    results = []
    for line in lines:
        data = line.split()
        sum =  0
        for score in data[1:]:
            sum += int(score)
        result = '%s\t:%d\n'%(data[0],sum)
        results.append(result)

output = open('result.txt','w')
output.writelines(results)
output.close()

