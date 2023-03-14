# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 09:45:48 2023

@author: MK
"""

def plainTextConversion(s,key):
    
    i = 0
   
    sList = list(s.strip())
    n = len(sList)
    while(n>0):
       temp=[]
       checkSame=False
       #print(sList,'sList')
       for j in range(0,2):
           if j<len(sList) and sList[j] not in temp :
              temp.append(sList[j])
              checkSame = False
           elif j<len(sList) and sList[j] in temp :
              temp.append('x')
              checkSame = True
           else:
               checkSame = False
               continue
       #print(temp,'temp')
       sList.remove(sList[0])
      # print(checkSame)
       if len(temp)>1 and checkSame == False:
          sList.remove(sList[0])
          plainText.append(temp)
          n=n-2
       elif len(temp)>1 and checkSame == True:
           #do noting
          plainText.append(temp)
          n=n-1
       elif len(temp)<1 and checkSame == True:
           # do nothing
          plainText.append(temp) 
       else:
          temp.append('x')
          plainText.append(temp)
          n=n-2
          
      
       #print(n,'n')
       
       #print(plainText,'plainText')  
        
 print(plainText,'final')
res = playFairCipher(plainText,key)

return res
if  __name__ == '__main__':
 s = input ('enter plainText : ')
 key = input('enter key text : ')
 s = ''.join(s.split())
 key = ''.join(key.split())
 print(s,'[s]')
 result = plainTextConversion(s,key) 
 print (result)