class Hotel:
    counter = 100
    
    def __init__(self, room_type):
        self.room_id = f"{'L' if room_type == 'Luxury' else 'S'}{Hotel.counter}"
        Hotel.counter += 1
        self.room_type = room_type
        
    def get_room_id(self):
        return self.room_id
    
    def get_room_type(self):
        return self.room_type

class Room(Hotel):
    def __init__(self, room_type, price_per_day):
        super().__init__(room_type)
        self.price_per_day = price_per_day
    
    def calculate_room_rent(self, no_of_days):
        return self.price_per_day * no_of_days

class LuxuryRoom(Room):
    def __init__(self, price_per_day=5000):
        super().__init__('Luxury', price_per_day)
    
    def calculate_room_rent(self, no_of_days):
        rent = super().calculate_room_rent(no_of_days)
        if no_of_days > 5:
            rent *= 0.95 
        return rent

class StandardRoom(Room):
    def __init__(self, price_per_day=3000):
        super().__init__('Standard', price_per_day)
    
    def calculate_room_rent(self, no_of_days):
        return super().calculate_room_rent(no_of_days)

class Customer:
    counter = 1000
    
    def __init__(self, name, address, no_of_days):
        self.customer_id = Customer.counter
        Customer.counter += 1
        self.name = name
        self.address = address
        self.no_of_days = no_of_days
        self.room = None
    
    def assign_room(self, room):
        self.room = room
    
    def get_bill(self):
        if self.room:
            return self.room.calculate_room_rent(self.no_of_days)
        return 0
    
    def get_details(self):
        return {
            'Customer ID': self.customer_id,
            'Name': self.name,
            'Address': self.address,
            'Room ID': self.room.get_room_id() if self.room else None,
            'Room Type': self.room.get_room_type() if self.room else None,
            'Total Bill': self.get_bill()
        }


customer1 = Customer("Gourav Singh", "Madhavpura , Vadodara", 7)
luxury_room = LuxuryRoom()
customer1.assign_room(luxury_room)
print(customer1.get_details())
