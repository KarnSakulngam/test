# class Calculator:                                               # set class for function
#     def __init__(self) -> None:                                 # initiate def(self)
#         pass                                                    # what the fuck
#         self.history = []


#     def choosefunction(self):                                   # define choose function
#         print("1=multiply\n2=add\n3=subtract\n4=divide")        # int choose function print int
#         while True:                                             # while loop for picking * + - /
#             a = int(input("Pick a number: "))                   # specify to be 'int' , insert input
#             if a in [1,2,3,4]:                                  # if in [] , then...
#                 break                                           # if input works , BREAK
#             else:                                               # if isn't in [] , then...
#                 print("ERROR, choose the one that matched! ")   # make them pick again
#         return a                                                # return a
    
#     def multiplynum(self):                                      # define *
#         b = int(input("Pick the first number: "))               # specify to be 'int' , input first #
#         c = int(input("Pick the second number: "))              # specify to be 'int' , input second #
#         print(b*c)
#         self.history.append(b*c)  
#         print(self.history)    
                                           

#     def addnum(self):                                           # define +
#         b = int(input("Pick the first number: "))               # specify to be 'int' , input first #
#         c = int(input("Pick the second number: "))              # specify to be 'int' , input second #
#         print(b+c)                                              
#         self.history.append(b+c)  
#         print(self.history)  

#     def subtractnum(self):                                      # define -
#         b = int(input("Pick the first number: "))               # specify to be 'int' , input first #
#         c = int(input("Pick the second number: "))              # specify to be 'int' , input second #
#         print(b-c)                                              
#         self.history.append(b-c)  
#         print(self.history)  

#     def dividenum(self):
#         b = int(input("Pick the first number: "))               # specify to be 'int' , input first #
#         c = int(input("Pick the second number: "))              # specify to be 'int' , input second #
#         print(b/c)     
#         self.history.append(b/c)  
#         print(self.history)  

#     def run(self):                                              # define run command
#         while True: 
#             d = self.choosefunction()
#             if d == 1:
#                 self.multiplynum()
#             elif d ==2:
#                 self.addnum()
#             elif d ==3:
#                 self.subtractnum()
#             elif d ==4:
#                 self.dividenum()


# cal = Calculator()
# cal.run()

# list = [1, "what", 2,3]
# list[2:]

# list1 = ["Pleum"," a"," is"," dok"," dek"," and","he","love","to","eat","curry."]

# print(list1[0] + list1[2] + list1[1] + list1[4] + list1[3] + " ".join(list1[5:]))

# str

# 1. has variabe self.history, able to access anywhere
# 2. print history after actions
# 3. before printing, add element to list (results)

import turtle

tur = turtle.Turtle()

tur.fillcolor('black')
tur.begin_fill()

tur.left(90)
tur.forward(200)

tur.left(90)
tur.forward(50)

tur.right(90)
tur.forward(50)

tur.right(90)
tur.forward(200)

tur.right(90)
tur.forward(50)

tur.right(90)
tur.forward(50)

tur.left(90)
tur.forward(200)

tur.right(90)
tur.forward(100)

tur.end_fill()
tur.hideturtle()

turtle.getscreen()._root.mainloop()  # <-- run the Tkinter main loop


