import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
from sklearn import tree
#

print('تخمين قيمت خودرو شما')
model=input('مدل ماشين:')
#
for i in range(1,201):
    r=requests.get('https://www.truecar.com/used-cars-for-sale/listings/%s/?page=%i'%(model,i))
    

    soup=BeautifulSoup(r.text , 'html.parser')
    cars=soup.find_all('li',attrs={'class' :"margin-top-3 d-flex flex-grow col-md-6 col-xl-4" })
    list=[]
    for car in cars:
        a=re.findall(r'(\d*,\d{3})(\d{2,3},\d*)',car.text)
        year=(car.text).split()[0]
        b=re.findall(r'(\d+)',year)
        for i in a:
            list.append((int(i[0].replace(',','')),int(i[1].replace(',',''))))
#
for i in list:
    cnx=mysql.connector.connect(user='root',password='',host='127.0.0.1',database= 'cars_information')
    cursor=cnx.cursor()
    cursor.execute('insert into price valuse(\'%i\')'%(i[0])) 
    cnx.commit()
    cnx.close()
#
for i in list:
    cnx=mysql.connector.connect(user='root',password='',host='127.0.0.1',database= 'cars_information')
    cursor=cnx.cursor()
    cursor.execute('insert into milesyear valuse(\'%i\',\'%i\')'%(i[1],b[0])) 
    cnx.commit()
    cnx.close()

#




x=[]
y=[]

#
cnx=mysql.connector.connect(user='root',password='',host='127.0.0.1',database= 'cars_information')
cursor=cnx.cursor()
query = 'SELECT * FROM price;'
cursor.execute(query)
for price in cursor:
    y.append(price)
cnx.close()
#
cnx=mysql.connector.connect(user='root',password='',host='127.0.0.1',database= 'cars_information')
cursor=cnx.cursor()
query = 'SELECT * FROM milesyear ;'
cursor.execute(query)
for miles_and_year in cursor:
    x.append(miles_and_year)
cnx.close()
#
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
new_data=[[int(input('ميزان کارکرد ماشين:')),int(input('سال ساخت ماشين:'))]]
answer=clf.predict(new_data)
print('قيمت احتمالي ماشين شما:',answer)





