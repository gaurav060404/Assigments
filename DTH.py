from abc import ABC, abstractmethod
class DTH(ABC):
    counter = 101
    def __init__(self,consumer_name):
        self.consumer_name = consumer_name
        self.consumer_no = DTH.counter
        DTH.counter += 1
    def get_consumer_name(self):
        return self.consumer_name
    def get_consumer_no(self):
        return self.consumer_no
    @abstractmethod
    def calculate_monthly_rent(self):
        pass

class BasePackage(DTH):
    def __init__(self,consumer_name,base_pack_name,subscription_period):
        super().__init__(consumer_name)
        self.base_pack_name = base_pack_name.lower().capitalize()
        self.subscription_period = subscription_period
    
    def get_pack_name(self):
        return self.base_pack_name
    def get_subscription_period(self):
        return self.subscription_period
    def validate_base_pack(self):
        if ["silver","gold","platinum"].count(self.base_pack_name.lower()) == 0:
            self.base_pack_name = "Silver"
            print("Base package name is incorrect , set to Silver")
            return
        print(f"The pack {self.base_pack_name} is valid")
    def calculate_monthly_rent(self):
        if self.subscription_period < 1 or self.subscription_period > 24:
            return -1
        else:
            self.validate_base_pack()
            pack_price = {"Silver":350,"Gold":440,"Platinum":560}
            self.discount = 0
            if self.subscription_period > 12:
                self.discount = pack_price[self.base_pack_name]*(self.subscription_period - 12)
            self.monthlyrent = ((pack_price[self.base_pack_name] * self.subscription_period)-self.discount)/self.subscription_period
            return self.monthlyrent

cust = BasePackage("Gaurav","Gold",13)
print(cust.get_pack_name())
print(cust.get_consumer_name())
print(f"Monthly rent is : {cust.calculate_monthly_rent():.2f}")





