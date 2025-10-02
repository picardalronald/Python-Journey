#print array, and then push a new item using array push or equivalent

names  = [
 'Ronald',    
 'jenny',
 'picardal',
 'roque',
     
 ]
  
for index, value  in enumerate(names):
    print(f"{index} : {value}")
 #inserting index and name in array
names.insert(0, 'love')

print("Updated names", names)
