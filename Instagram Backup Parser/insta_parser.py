import json
import sqlite3
import datetime
import pytz
mess=open("messages.json","r", encoding='utf8', errors='ignore')
data=json.load(mess)
instaid=input("Enter your Insta ID: ")
for partips in data:
    print(partips['participants'])
print()
print("Select an user from the List")
acc=input("Enter the username of the friend: ")
def zonecon(year,month,date,hour,mins,millisec):
    dt_today =  datetime.datetime(year,month,date,hour,mins,millisec)   # Local time
    dt_India = pytz.timezone('Asia/Kolkata')
    Ind_dt=pytz.utc.localize(dt_today).astimezone(dt_India)
    return Ind_dt
conn=sqlite3.connect(acc+'.sqlite')
cur=conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Messages;
CREATE TABLE Messages (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    Username    TEXT,
    Chat  TEXT,
    Date_GMT TEXT,
    Time_GMT TEXT,
    Date_IST TEXT,
    Time_IST TEXT
)
''')
def tablecreate(userid,chatted,dte,tme,dist,tist):
    cur.execute('''INSERT INTO Messages(Username,Chat,Date_GMT,Time_GMT,Date_IST,Time_IST) VALUES(?,?,?,?,?,?)''',(userid,chatted,dte,tme,dist,tist))
    conn.commit()

c=0
# mess=open("messages.json","r", encoding='utf8', errors='ignore')
# data=json.load(mess)
# # acc=input("Enter the username of the friend: ")
# print("Select an user from thr List")
# for partips in data:
#     print(partips['participants'])
print()

for parts in data:
    if(parts['participants']==[instaid, acc]) or (parts['participants']==[acc,instaid]):
         print("Participants of this Chat are:" ,parts['participants'])
         print()
         line=parts['conversation']
         for lines in reversed(line):
              chat=""


              for key in reversed(lines):


                  if (key=='text'):
                      c=c+1
                      chat=str(lines[key])
                      username=lines['sender']
                      dt=lines['created_at'].split('T')
                      date=dt[0]
                      time=dt[1].split('.')  #2019-03-31T13:34:01.764979+00:00
                      timing=time[0]
                      dt=lines['created_at']
                      i=dt.index('T')
                      j=dt.index('.')

                      date1=dt[0:i]
                      time1=dt[(i+1):j]

                      ds=date1.split('-')
                      ts=time1.split(':')
                      # ts.pop()
                      dtfl=ds+ts
                      # print(dtfl)
                      yr=int(dtfl[0])
                      mn=int(dtfl[1])
                      dte=int(dtfl[2])
                      hur=int(dtfl[3])
                      minu=int(dtfl[4])
                      mss=int(dtfl[5])
                      IST=zonecon(yr,mn,dte,hur,minu,mss)
                      zonesplit=str(IST).split('+')
                      # print(zonesplit)
                      dtsplit=zonesplit[0].split(' ')
                      # print(dtsplit)

                      print(lines['sender']," ",end='')
                      print(repr(chat.strip('\n\r'))," ",date," ",timing," ",dtsplit[0]," ",dtsplit[1])

                      # print(lines['created_at'])
                      print('')
                      tablecreate(username,chat,date,timing,dtsplit[0],dtsplit[1])
                      break

                  else:
                      continue


         break

# print(data[1]['participants'])



        # print(lines)
print("Total Number of Chats or Conversations in your acc:",len(data))
print("Total Number of Messages with",acc,"=",c)
