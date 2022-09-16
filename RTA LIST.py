n=int(input("Enter the no. of persons came for registraions:\n"))
m=int(input("Enter the total number of registrations per day:\n"))
stri=[]
for i in range(1,n+1):
  if(i<=m):
    print("Enter data:")
    print("Enter data of person",i)
    data=input().split()
    stri.append(data)
  else:
    print(0)
    print("registrations are closed for today")
    print("please come tomorrow")
    print("have a nice day!")

print("name of person  ;  age  ;  phonenumber ;  address ;")
for item in stri:
  print()
  print(item[0]," "*(14-len(item[0])),";",
            item[1]," "*(4-len(item[1])),";",
                     item[2]," "*(11-len(item[2])),";",
            item[3]," "*(8-len(item[3])),";")
print("\n")
