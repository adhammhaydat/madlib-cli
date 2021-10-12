from typing import _SpecialForm
import re


# print("""hellow dev
# we will play a small game 
# i will give you a text and you will fill the { } by the correct word
# """)
# lets_go=input("""
# are you ready to play
# if yes enter y
# if no enter q
# """)
def read_template(path):
    
    print("this is the text")
    # with open('assets/dark_and_stormy_night_template.txt','r') as f:
    # print(f.readlines())
    f=open(path)
    file=f.read()
    return file
    
def parse_template(text):
    x=re.sub("{.*?}","{}",text) 
    
    y=re.findall(r"(?<=\{).+?(?=\})", text) 
    
    return (str(x),tuple(y))

# parse_template("It was a {Adjective} and {Adjective} {Noun}."
    # )            
    #     def read_template():
    # while(lets_go !="q"):
    #     try:
    #         print("this is the text")
    #         with open('assets/dark_and_stormy_night_template.txt','rb') as f:
    #             print(f.readlines())
    #             file=f.read()
    #             print({}.find(file))
    #             return file
    #     except FileNotFoundError :
    #         print("path error")
    #     finally:
    #         f.close()
    #         break
# def parse_template():

#     with open('assets/dark_and_stormy_night_template.txt','rb') as f:
#         file=f.read()
#     with open('assets/brain.copy.txt', 'wb') as f2:
#         f2.write(file)   


# def merge():
#     print("now enter each word in separate line")
#     list_of_words=[]
#     for i in range(2):
#         list_of_words.append(input())
#     txt="I the {Adjective} and {Adjective} {A_First_Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find."
#     file=txt.format(Adjective=list_of_words[0],A_First_Name=list_of_words[1]) 
#     print(file)
# read_template()
# parse_template()
# merge()