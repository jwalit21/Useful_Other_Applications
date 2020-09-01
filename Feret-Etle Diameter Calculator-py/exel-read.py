#================developed by=====================#
#================Jwalit Shah======================#

import xlrd
import math
loc = ("C:\\Users\\Jwalit Shah\\Downloads\\VRAJ.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

ans={}
i=1
while(sheet.cell_value(i,0) and sheet.cell_value(i,1)):
    
    x=sheet.cell_value(i,0)
    inner_d = {}
    flag=0
    
    while(True):
        
        ele = sheet.cell_value(i,1)
        if(inner_d.__contains__(ele)):
            inner_d[ele]+=1
        else:
            inner_d.setdefault(ele,1)
        
        i+=1
        
        if(not(sheet.cell_value(i,1))):
            flag=1
            break
        if(sheet.cell_value(i,0)):
            break
    
    if(flag==1):
        break
    
    upper_sum=0
    denom_sum = 0
    for j in inner_d:
        upper_sum += (j*j*inner_d[j])
        denom_sum += inner_d[j]
    ans.setdefault(x,(math.sqrt(upper_sum)/denom_sum))

while(True):
    
    print("Do you want to continue ? (y|Y|n|N) : ",end="")
    ip=input()
    if(ip=="Y" or ip=="y"):
        pass
    elif(ip=="N" or ip=="n"):
        print("Thank you")
        break
    else:
        print("Invalid input")
        continue
    
    print("Enter the Area : ",end="")
    try:
        area = (float)(input())
    except ValueError as e:
        print ('Invalid input')
        continue
    
    if(ans.__contains__(area)):
        print("Feret : ",ans[area])
    else:
        print("Area is not available")

