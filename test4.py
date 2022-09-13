
true = 'NaN'
list = [1, False, True, 0.2, "a lot of", true, 'NaN']
print (list)
print (list[4])
list[6] = "all"
print (list)
list[1:3] = [20, "is true", False, True, 0.11, 25, ' ']
print (list)
list = list[1:4].copy()
print (list)
print (list[1:], list[-3])
print (list + list + list)
list = [list[-3], list[1:3], list[2:]]
print (list)
list = list[-3]
print ("list[-3] is:", list)
print (list + list + 1)
list = [list + list + list + 1]
print (list)
list[0] = true, 11, "none"
print (list)
list.insert(0, 222)
list.insert(1, 737)
list.insert(2, 777)
print ('list after insertion:', list)
list[0:2] = ['list', 'insert', "maybe", 'this', 12, False].copy()
print(list)
list = list.copy() + list
print(list)
list.append(True)
print(list)
list.extend(list.copy())
print(list)
list[4:9] = [True,False,True,False,'else',True]
print (list)
list1 = list[3:10]
print (list1, 'followed by', list)
list = list[3:10]
print (list)
list.extend(list)
list.remove(False)
list.remove(False)
list.remove("this")
list.remove('this')
list.pop(7)
list.append(true)
print (list)
for e in list:
 print (e)
for i in range(10, -1, -1):
 print (i)
print (range(10, 1, 1))
print (len(list))
print (list)
while i == 0 or i < len(list):
 for e in list:
  list.pop(i)
  if e == 'NaN':
    list[i] = true, "Hello"
#  i += 1
 i += 1
print ("while & for loop:", list)
list.clear()
print (list)
list.insert(0, "A320")
print (list)
list.insert(0, "B737")
list.insert(0, "B777")
list.sort()
print (list)
lst = list
lst[1] = "B738"
print (list, lst)
lst = list.copy()
lst[0] = "B789"
lst = (lst + list)
print (lst + list)
import time
time.sleep(0.2)
print (lst)
lst.extend(list.copy())
print (lst)
lst = lst[0:4]
print("lst is list:", lst)
(plane1, plane2, plane3, plane4) = lst
time.sleep(0.2)
print (plane2)
tuple = lst
time.sleep(0.2)
print (tuple)
(plane1, plane2, plane3, plane4) = tuple
time.sleep(0.2)
print(plane1)
tpl = tuple
tpl = list
tpl.append("A380")
tpl = tuple + tpl
time.sleep(0.1)
print (tpl)
list.clear()
tpl = tpl[0:4:2]
time.sleep(0.1)
print(tpl)
del tuple, list
tpl = tuple(tpl)
time.sleep(0.1)
print(tpl)
tpl = list(tpl)
plane = 'B737'
tpl.insert(0, plane)
tpl.insert(2, plane)
tpl.insert(3, plane)
tpl = tuple(tpl)
time.sleep(0.1)
print (tpl)
tpl = set(tpl)
print (tpl)
print ("B777" in tpl)
addon = print ("B767" in tpl)
print (addon)
st = tpl
st.add(addon)
print (st)
st.remove(addon)
st.add(addon)
time.sleep(0.5)
print (st)
st.discard("B789")
st.discard("B789")
print (st)
print ("\r" is "\n")
print ("\r")
print ("\n")
#####
print (st)
(aircraft1, aircraft2, aircraft3) = st
print (aircraft2)

dct = list(st)
#dct = dict(dct)

while i == 0 or i < len(dct):

 for e in dct:
  dct[i] = dct[i],": 123"
 i += 1
print (dct)
dct = {
 "A320": "Plane1",
 "B737": "Plane2",
 "B747": "Plane3"
 }
print (dct)
print (dct["A320"][0],dct["A320"][1],dct["A320"][2],dct["A320"][3],dct["A320"][4],dct["A320"][5],dct["A320"][0:6])
dct["A320"] = "Aircraft 1" 
dct["A380"] = "Aircraft 4"
dct["None"] = "None"
print (dct)
dct.pop("None")
print (dct)
for i in dct.keys() or dct.values():
 print ("or", i)
for i in dct.keys() and dct.values():
 print ("and", i)
time.sleep(0.5)
for i in dct.keys(), dct.values():
 print (",", i)



