#print a defined array, then remove the last item using array pop or equivalent

names  = [
 'Ronald',    
 'jenny',
 'picardal',
 'roque',
     
 ]
  
for index, value  in enumerate(names):
    print(f"{index} : {value}")

remove = names.pop(0)
print("Removed this name: ", remove)


print("Updated names", names)
