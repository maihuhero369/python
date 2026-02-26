class Car :
     modle = "X5"
     year = 2020
     color = "Black"
     def __init__(self , modle , year ,color):
          self.modle = modle
          self.year = year
          self.color = color
     def display(self):
            print("Car modle : ", self.modle)
            print("Car year : ", self.year)
            print("Car color : ", self.color) 
     def update(self , modle , year ,color):
          self.modle = modle
          self.year = year
          self.color = color       
c1 = Car("BMW", 2020, "Black")      
c2 = Car("Audi", 2021, "White")
c3 = Car("Mercedes", 2022, "Silver")
c1.display()
c2.display()
c3.display()
c1.update("BMW", 2023, "Red")
c1.display()        
c2.update("Audi", 2024, "Blue")
c2.display()    