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



def get_sum_of_everyday(number, sorted_middle):

    count_by_day = {}

    for i in sorted_middle:
        if(i[1]==number):
            if(i[2] in count_by_day):
                count_by_day[i[2]] += i[3]
                pass
            else:
                count_by_day[i[2]] = i[3]
            pass
        else:
            pass
    return count_by_day;



#对1001类
count_by_day_1001 = get_sum_of_everyday(1001,sorted_middle);
sorted_count_by_day_1001 = sorted(count_by_day_1001)
for i in sorted_count_by_day_1001:
    print(i,'%3f'%count_by_day_1001[i])


#file=open('1001.txt','w')
for i in range (0,len(sorted_count_by_day_1001)):
    string = ( sorted_count_by_day_1001[i]+ ' 1 '+ #常数项
           ((i+3)%7)*' 0 '+ ' 1 '+ (7-((i+3)%7)-1)*' 0 '+ #独热码表示周几
           '%3f'%count_by_day_1001[sorted_count_by_day_1001[i]] )
    print(string)
#    file.write(string+'\n')
#file.close()

