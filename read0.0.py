import pickle
import string

a = pickle.load(open('data.pkl','rb'));

print(len(a))


title = a[0]
a.pop(0);
#a = sorted(a,key= lambda x: int(x[0]))

#中类
middle = []
middle_title = [ title[0],title[3],title[7],title[13] ]
#['custid', '中类编码', '销售日期', '销售数量']
for i in range(0,len(a)):
    try:
        middle.append([ int(a[i][0]), int(a[i][3]), a[i][7], float(a[i][13]) ])
    except:
        print('error in',a[i])



sorted_middle = sorted(middle,key= lambda x: (x[1]))

#对1001类

count_by_day_1001 = {}

for i in sorted_middle:
    if(i[1]==1001):
        if(i[2] in count_by_day_1001):
            count_by_day_1001[i[2]] += i[3]
            pass
        else:
            count_by_day_1001[i[2]] = i[3]
        pass
    else:
        break


sorted_count_by_day_1001 = sorted(count_by_day_1001)

for i in sorted_count_by_day_1001:
    print(i,'%3f'%count_by_day_1001[i])
