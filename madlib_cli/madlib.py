from typing import _SpecialForm
import re



def read_template():
    
    print("this is the text")
    
    f=open('assets/brain.copy.txt','r')
    file=f.read()
    return file
    
def parse_template(file):
      
    x=re.sub("{.*?}","{}",file) 
    print(file)
    y=re.findall(r"(?<=\{).+?(?=\})", file)
    return x,y
    



def merge(x,y):
    formated=x.format(*y)
    f2=open('assets/new_copy.txt', 'w') 
    f2.writelines(formated)
    return formated

print("""hellow dev
we will play a small game 
i will give you a text and you will fill the { } by the correct word
""")
lets_go=input("""
are you ready to play
if yes enter y
if no enter q
""")   
while lets_go !="q":
    new_list=[]
      
    file=read_template()
    x,y=parse_template(file)
    for i in y:
        new_list.append(input())
    print(merge(x,new_list))
    break
