import pandas

fails = pandas.read_excel("description.xlsx", sheet_name="LookupAREA") 
info_list = fails.values.tolist()

get_info=input('Ievadīt reģionu ')
print(get_info)

reg_id=0
for row in info_list:
    if row[1]==get_info:
        reg_id=row[0]
        break
print(reg_id)

if reg_id==0:
    print('Reģions nav atrasts')
    exit()

zip=[]
csv=open('data.csv', 'r')
for line in csv:
    zip.append(line.rstrip().split(','))

geo_count=[]
for line in zip:
    if line[1]==reg_id:
        geo_count.append(int(line[3]))

print(sum(geo_count))