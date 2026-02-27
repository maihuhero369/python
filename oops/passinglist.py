class PassingList:
    list = [ 23 , 45 , 67 ,89 , 90 , 34 , 56 ]
    def __init__ (self, lst):
        self.lst = lst
    def display(self):
        print("The List is : ", self.lst)
    def modify(self):
        for i in range(len(self.lst)):
            self.list[i] = self.lst[i]+ 10
        print("The Modified List is : ", self.list)
class main:
    lst = [ 23 , 45 , 67 ,89 , 90 , 34 , 56 ]
    obj = PassingList(lst)
    obj.display()
    obj.modify()            