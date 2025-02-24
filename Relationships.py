import random
class Address:
    def __init__(self,street,city,state,postalCode,country):
        self.street = street
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country

        
    def validate(self):
        if(not(self.city) or not(self.country) or not(self.state) or not(self.postalCode) or not(self.street)):
            return False
        return True


    def outputAsLabel(self):
        print(f"Address : {self.street} , {self.city} , {self.postalCode} , {self.state} , {self.country}.")


class Person:
    def __init__(self,name,phoneNumber,emailAddress,address):
        self.name = name
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.address = address # Association (A person has a address)


    def purchaseParkingPass(self):
        if self.address.validate():
            print("Parking Pass Purchased!!!")
            return
        print("Please Enter Your Address")
    


class Student (Person):
    def __init__(self,name,phoneNumber,emailAddress,address,studentNumber,averageNumber):
        super.__init__(name,phoneNumber,emailAddress,address)
        self.studentNumber = studentNumber
        self.averageNumber = averageNumber


    def isEligibleToEnroll(self):
        if self.averageNumber > 70 :
            print("You're Eligible")
            return
        print("You're Not Eligible")


    def getSeminarsTaken(self):
        return self.studentNumber 
    

class Professor (Person):
    def __init__(self,name,phoneNumber,emailAddress,address,salary,staffNumber,yearsOfService):
        super.__init__(name,phoneNumber,emailAddress,address)
        self.__salary = salary
        self._staffNumber = staffNumber
        self.__yearsOfService = yearsOfService
        self.numberOfClasses = numberOfClasses


        def getSalary(self):
            return self.__salary


        def getStaffNumber(self):
            return self._staffNumber


        def getYearsOfServic(self):
            return self.__yearsOfService


        def getNumberOfClasses(self):
            return self.numberOfClasses
        
        


