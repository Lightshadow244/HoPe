import os
directory = "/home/adam/logs/"
result = {}
month = ""
new_ip = ""
old_ip = ""
new_minute = ""
old_minute = ""
for f in os.listdir(directory):
        if f.endswith('.log'):
                file = open(f,"r")
                for l in file:
                        if(l.find("/de/a/home") != -1 or l.find("/en/a/home") != -1):
                                pos = l.find("[",2) + 5
                                month = l[pos:pos + 3]
                                new_minute = l[pos+10:pos + 12]
                                new_ip = l[l.find("]")+2:l.find("(")-1]
                                #print(l)
                                if(old_ip != new_ip):
                                        #print("new ip")
                                        if month not in result:
                                                result[month]=1
                                        else:
                                                result[month] += 1
                                else:
                                        #print("old ip")
                                        if(old_minute != new_minute):
                                                #print("new minute")
                                                if month not in result:
                                                        result[month]=1
                                                else:
                                                        result[month] += 1
                                old_ip = new_ip
                                old_minute = new_minute
print(result)
