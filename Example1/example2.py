from time import gmtime, strftime
import time
print("\nGMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
print("Local: "+strftime("%a, %d %b %Y %I:%M:%S %p %Z\n"))

from datetime import date
first_date = date(2023, 10, 2)
second_date = date(2023, 10, 30)
delta = second_date - first_date
print(delta)

d =  dict(x=[1,2,3], y = [4,5,6], z = [7,8,9])
import json
json.dumps(d)
print(json.dumps(d, indent=4))

#task2
class People:
    def __init__(self, date_rosh, name, contact_tel, city):
        self.name = name,
        self.date_rosh = date_rosh,
        self.contact_tel = contact_tel,
        self.city = city
    def getDannie(self):
        try:
            return self.name, self.date_rosh, self.contact_tel, self.city
        except:
            print('No name, no date_rosh, no contact_tel, nop city')
d1 = People("Sam", "10.07.2006", "+998994954934", "Uzbekistan")
print(d1.name, d1.date_rosh, d1.contact_tel, d1.city)


a = 5
b = 5
print(a + b)