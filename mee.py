class Calculator: # set class for function
    def __init__(self) -> None: # initiate def(self)
        pass # what the fuck
        self.history = [] # 

    def choosefunction(self):                               # define choose function
        print("1=multiply\n2=add\n3=subtract\n4=divide")    # int choose function print int
        while True:                                         # while loop for picking * + - /
            a = int(input("Pick a number: "))               # specify to be 'int' , insert input
            if a in [1,2,3,4]:                              # if in [] , then...
                break                                           # if input works , BREAK
            else:                                             # if isn't in [] , then...
                print("ERROR, choose the one that matched! ") # make them pick again
        return a # return a
    
    def multiplynum(self): # define *
        b = int(input("Pick the first number: ")) # specify to be 'int' , input first #
        c = int(input("Pick the second number: ")) # specify to be 'int' , input second #
        print(b*c) # print

    def addnum(self): # define +
        b = int(input("Pick the first number: ")) # specify to be 'int' , input first #
        c = int(input("Pick the second number: ")) # specify to be 'int' , input second #
        print(b+c) # print
    
    def subtractnum(self): # define -
        b = int(input("Pick the first number: ")) # specify to be 'int' , input first #
        c = int(input("Pick the second number: ")) # specify to be 'int' , input second #
        print(b-c) # print

    def dividenum(self):
        b = int(input("Pick the first number: ")) # specify to be 'int' , input first #
        c = int(input("Pick the second number: ")) # specify to be 'int' , input second #
        print(b/c) # print

    def run(self): # define run command
        while True: # 
            d = self.choosefunction()
            if d == 1:
                self.multiplynum()
            elif d ==2:
                self.addnum()
            elif d ==3:
                self.subtractnum()
            elif d ==4:
                self.dividenum()


cal = Calculator()
cal.run()
