import csv
import re
import csv_writer_refine

p = re.compile('[\-.0-9]+')
p_cd = re.compile('[0-9]+')

# 1 - temperture_data.csv
# date: C14 ~ C3721 (2021-02-24 ~ 2011-01-01); 내림차순
# avgMaxTemp: E
# avgMinTemp: H (csv이기에 I, J, ... 로 간혹 이동함)
f_temp = open(r'proj_lin_reg\data\temp_data.csv', 'r')
rdr_temp = csv.reader(f_temp)

l_avgtemp = []
l_maxtemp = []
l_mintemp = []
for line in rdr_temp:
    if len(line) > 10:
        l_avgtemp.append(line[3])
        l_maxtemp.append(line[4])
        if len(p.findall(line[7])) == 0:
            if len(p.findall(line[8])) == 0:
                if len(p.findall(line[9])) == 0:
                    if len(p.findall(line[10])) == 0:
                        print("Too long str!!!")
                    else:
                        l_mintemp.append(line[10])
                else:
                    l_mintemp.append(line[9])
            else:
                l_mintemp.append(line[8])
        else:
            l_mintemp.append(line[7])
f_temp.close()


# 2 - rainfall_data.csv
# date: C15 ~ C3722 (2021-02-24 ~ 2011-01-01); 내림차순
# rainfall: D
f_rain = open(r'proj_lin_reg\data\rain_data.csv', 'r')
rdr_rain = csv.reader(f_rain)

l_rain = []
for line in rdr_rain:
    if len(line) > 3:
        if len(p.findall(line[3])) == 1:
            l_rain.append(line[3])
        else:
            continue
f_rain.close()


# 3 - cost_data.csv (cabbage cost)
# date: A2 ~ A3709 (2011-01-01 ~ 2021-02-24); 오름차순
# cost: B
l_date = []
l_cost = []
l_season = []
l_interest = []

f_cost = open(r'proj_lin_reg\data\cost_data.csv', 'r')
rdr_cost = csv.reader(f_cost)

# 금리
for i_line in rdr_cost:
    i_strdate = p_cd.findall(i_line[0])
    if len(i_strdate) == 3:
        
        if int(i_strdate[0]) == 2011:
            if int(i_strdate[1]) == 1:
                if int(i_strdate[2]) < 13:
                    l_interest.append("2.50")
                elif int(i_strdate[2]) >= 13:
                    l_interest.append("2.75")
            elif int(i_strdate[1]) == 2:
                l_interest.append("2.75")
            elif int(i_strdate[1]) == 3:
                if int(i_strdate[2]) < 10:
                    l_interest.append("2.75")
                elif int(i_strdate[2]) >= 10:
                    l_interest.append("3.00")
            elif int(i_strdate[1]) == 4:
                l_interest.append("3.00")
            elif int(i_strdate[1]) == 5:
                l_interest.append("3.00")
            elif int(i_strdate[1]) == 6:
                if int(i_strdate[2]) < 10:
                    l_interest.append("3.00")
                elif int(i_strdate[2]) >= 10:
                    l_interest.append("3.25")
            elif 7 <= int(i_strdate[1]) <= 12:
                l_interest.append("3.25")
        elif int(i_strdate[0]) == 2012:
            if 1 <= int(i_strdate[1]) <= 6:
                l_interest.append("3.25")
            elif int(i_strdate[1]) == 7:
                if int(i_strdate[2]) < 12:
                    l_interest.append("3.25")
                elif int(i_strdate[2]) >= 12:
                    l_interest.append("3.00")
            elif 8 <= int(i_strdate[1]) <= 9:
                l_interest.append("3.00")
            elif int(i_strdate[1]) == 10:
                if int(i_strdate[2]) < 11:
                    l_interest.append("3.00")
                else:
                    l_interest.append("2.75")
            else:
                l_interest.append("2.75")
        elif int(i_strdate[0]) == 2013:
            if 1 <= int(i_strdate[1]) <= 4:
                l_interest.append("2.75")
            elif int(i_strdate[1]) == 5:
                if int(i_strdate[2]) < 9:
                    l_interest.append("2.75")
                elif int(i_strdate[2]) >= 9:
                    l_interest.append("2.50")
            else:
                l_interest.append("2.50")
        elif int(i_strdate[0]) == 2014:
            if 1 <= int(i_strdate[1]) <= 7:
                l_interest.append("2.50")
            elif int(i_strdate[1]) == 8:
                if int(i_strdate[2]) < 14:
                    l_interest.append("2.50")
                elif int(i_strdate[2]) >= 14:
                    l_interest.append("2.25")
            elif int(i_strdate[1]) == 9:
                l_interest.append("2.25")
            elif int(i_strdate[1]) == 10:
                if int(i_strdate[2]) < 15:
                    l_interest.append("2.25")
                elif int(i_strdate[2]) >= 15:
                    l_interest.append("2.00")
            else:
                l_interest.append("2.00")
        elif int(i_strdate[0]) == 2015:
            if 1 <= int(i_strdate[1]) <= 2:
                l_interest.append("2.00")
            elif int(i_strdate[1]) == 3:
                if int(i_strdate[2]) < 12:
                    l_interest.append("2.00")
                elif int(i_strdate[2]) >= 12:
                    l_interest.append("1.75")
            elif 4 <= int(i_strdate[1]) <= 5:
                l_interest.append("1.75")
            elif int(i_strdate[1]) == 6:
                if int(i_strdate[2]) >= 11:
                    l_interest.append("1.50")
                else:
                    l_interest.append("1.75")
            else:
                l_interest.append("1.50")
        elif int(i_strdate[0]) == 2016:
            if 1 <= int(i_strdate[1]) <= 5:
                l_interest.append("1.50")
            elif int(i_strdate[1]) == 6:
                if int(i_strdate[2]) >= 9:
                    l_interest.append("1.25")
                else:
                    l_interest.append("1.50")
            else:
                l_interest.append("1.25")
        elif int(i_strdate[0]) == 2017:
            if 1 <= int(i_strdate[1]) <= 10:
                l_interest.append("1.25")
            elif int(i_strdate[1]) == 11:
                if int(i_strdate[2]) >= 30:
                    l_interest.append("1.50")
                else:
                    l_interest.append("1.25")
            else:
                l_interest.append("1.50")
        elif int(i_strdate[0]) == 2018:
            if 0 <= int(i_strdate[1]) <= 10:
                l_interest.append("1.50")
            elif int(i_strdate[1]) == 11:
                if int(i_strdate[2]) >= 30:
                    l_interest.append("1.75")
                else:
                    l_interest.append("1.50")
            else:
                l_interest.append("1.75")
        elif int(i_strdate[0]) == 2019:
            if 1 <= int(i_strdate[1]) <= 6:
                l_interest.append("1.75")
            elif int(i_strdate[1]) == 7:
                if int(i_strdate[2]) >= 18:
                    l_interest.append("1.50")
                else:
                    l_interest.append("1.75")
            elif 8 <= int(i_strdate[1]) <= 9:
                l_interest.append("1.50")
            elif int(i_strdate[1]) == 10:
                if int(i_strdate[2]) >= 16:
                    l_interest.append("1.25")
                else:
                    l_interest.append("1.50")
            else:
                l_interest.append("1.25")
        elif int(i_strdate[0]) == 2020:
            if 1 <= int(i_strdate[1]) <= 2:
                l_interest.append("1.25")
            elif int(i_strdate[1]) == 3:
                if int(i_strdate[2]) >= 17:
                    l_interest.append("0.75")
                else:
                    l_interest.append("1.25")
            elif int(i_strdate[1]) == 4:
                l_interest.append("0.75")
            elif int(i_strdate[1]) == 5:
                if int(i_strdate[2]) >= 28:
                    l_interest.append("0.50")
                else:
                    l_interest.append("0.75")
            else:
                l_interest.append("0.50")
        elif int(i_strdate[0]) == 2021:
            l_interest.append("0.50")
        else:
            pass
f_cost.close()


# 24절기
f_cost = open(r'proj_lin_reg\data\cost_data.csv', 'r')
rdr_cost = csv.reader(f_cost)
for line in rdr_cost:
    strdate = p_cd.findall(line[0])
    if len(strdate) == 3:
        
        if int(strdate[1]) == 1: # 1월
            if int(strdate[2]) < 6:
                l_season.append("동지")
            elif int(strdate[2]) >= 6:
                l_season.append("소한")
            elif int(strdate[2]) >= 20:
                l_season.append("대한")
        elif int(strdate[1]) == 2:   # 2월
            if int(strdate[2]) < 4:
                l_season.append("대한")
            elif int(strdate[2]) >= 4:
                l_season.append("입춘")
            elif int(strdate[2]) >= 19:
                l_season.append("우수")
        elif int(strdate[1]) == 3:   # 3월
            if int(strdate[2]) < 6:
                l_season.append("우수")
            elif int(strdate[2]) >= 6:
                l_season.append("경칩")
            elif int(strdate[2]) >= 21:
                l_season.append("춘분")
        elif int(strdate[1]) == 4:   # 4월
            if int(strdate[2]) < 5:
                l_season.append("춘분")
            elif int(strdate[2]) >= 5:
                l_season.append("청명")
            elif int(strdate[2]) >= 20:
                l_season.append("곡우")
        elif int(strdate[1]) == 5:   # 5월
            if int(strdate[2]) < 6:
                l_season.append("곡우")
            elif int(strdate[2]) >= 6:
                l_season.append("입하")
            elif int(strdate[2]) >= 21:
                l_season.append("소만")
        elif int(strdate[1]) == 6:   # 6월
            if int(strdate[2]) < 6:
                l_season.append("소만")
            elif int(strdate[2]) >= 6:
                l_season.append("망종")
            elif int(strdate[2]) >= 22:
                l_season.append("하지")
        elif int(strdate[1]) == 7:   # 7월
            if int(strdate[2]) < 7:
                l_season.append("하지")
            elif int(strdate[2]) >= 7:
                l_season.append("소서")
            elif int(strdate[2]) >= 23:
                l_season.append("대서")
        elif int(strdate[1]) == 8:   # 8월
            if int(strdate[2]) < 8:
                l_season.append("대서")
            elif int(strdate[2]) >= 8:
                l_season.append("입추")
            elif int(strdate[2]) >= 23:
                l_season.append("처서")
        elif int(strdate[1]) == 9:   # 9월
            if int(strdate[2]) < 8:
                l_season.append("처서")
            elif int(strdate[2]) >= 8:
                l_season.append("백로")
            elif int(strdate[2]) >= 23:
                l_season.append("추분")
        elif int(strdate[1]) == 10:  # 10월
            if int(strdate[2]) < 9:
                l_season.append("추분")
            elif int(strdate[2]) >= 9:
                l_season.append("한로")
            elif int(strdate[2]) >= 24:
                l_season.append("상강")
        elif int(strdate[1]) == 11:  # 11월
            if int(strdate[2]) < 8:
                l_season.append("상강")
            elif int(strdate[2]) >= 8:
                l_season.append("입동")
            elif int(strdate[2]) >= 23:
                l_season.append("소설")
        elif int(strdate[1]) == 12:  # 12월
            if int(strdate[2]) < 7:
                l_season.append("소설")
            elif int(strdate[2]) >= 7:
                l_season.append("대설")
            elif int(strdate[2]) >= 22:
                l_season.append("동지")
        else:
            pass
        
        date = strdate[0] + strdate[1] + strdate[2]
        l_date.append(date)
        l_cost.append(line[1])
f_cost.close()

del l_date[-1:]
del l_cost[-1:]
del l_season[-1:]

# Finale - dataset exporting
dic_list = []
for i in range(len(l_date)):
    dic_list.append({
        
        "date": l_date[i], 
        "season": l_season[i],
        "avgTemp": l_avgtemp[-(i+1)], 
        "minTemp": l_mintemp[-(i+1)], 
        "maxTemp": l_maxtemp[-(i+1)], 
        "rainfall": l_rain[-(i+1)], 
        "interest": l_interest[i],
        "cost": l_cost[i]

            })

csv_writer_refine.save_to_file(dic_list)   # raw.csv