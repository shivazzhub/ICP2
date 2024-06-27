def Fullname(First_name, last_name):
  return First_name +" "+ last_name
def string_alternative(Full_name):
  res =''
  for i in range(0,len(Full_name),2):
    res+= Full_name[i]
  return res
First_name = input()
last_name = input()
Full_name = Fullname(First_name, last_name)
print(Full_name)
alt = string_alternative(Full_name)
print(alt)
