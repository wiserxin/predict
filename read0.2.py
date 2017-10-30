import pickle
import time

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

def date_to_gray(date):
    
    t = time.strptime(date,"%Y%m%d")
    n = t.tm_wday #周一为0
    string = n*' 0 ' + ' 1 ' + (6-n)*' 0 '
    return string

#########################################################################

all_middle_num = []
for i in middle:
    if str(i[1]) not in all_middle_num:
        all_middle_num.append(str(i[1]))

count = 0
for i in all_middle_num:
    count+=1
    count_by_day = get_sum_of_everyday(int(i),sorted_middle);
    sorted_count_by_day = sorted(count_by_day)
    file=open('data\\'+i+'.txt','w')    
    for j in range (0,len(sorted_count_by_day)):
        string = (sorted_count_by_day[j] + ' 1 '+
                  date_to_gray(sorted_count_by_day[j])+
                  ' %3f'%count_by_day[sorted_count_by_day[j]]
                  )
        file.write(string+'\n')
    file.close()
    
print(count)
