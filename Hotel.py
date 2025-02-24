class Customer:
    counter = 1000

    def __init__(self, customer_name, address, no_of_days):
        Customer.counter += 1
        self.customer_id = Customer.counter
        self.customer_name = customer_name
        self.address = address
        self.no_of_days = no_of_days
        self.room = None  

    def get_cust_id(self):
        return self.customer_id

    def get_cust_name(self):
        return self.customer_name

    def get_no_of_days(self):
        return self.no_of_days

    def get_address(self):
        return self.address


class Room:
    counter = 100 

    def __init__(self, price):
        Room.counter += 1
        self.price = price
        self.occupied = False
        self.assigned_customer = None
        self.room_id = None  

    def calculate_room_rent(self, no_of_days):
        raise NotImplementedError("Subclasses must override calculate_room_rent")


class LuxuryRoom(Room):
    def __init__(self, price):
        super().__init__(price)
        self.room_id = "L" + str(Room.counter)

    def calculate_room_rent(self, no_of_days):
        total = self.price * no_of_days
        if no_of_days > 5:
            total *= 0.95 
        return total


class StandardRoom(Room):
    def __init__(self, price):
        super().__init__(price)
        self.room_id = "S" + str(Room.counter)

    def calculate_room_rent(self, no_of_days):
        return self.price * no_of_days


class Hotel:
    def __init__(self, room_list, location):
        self.room_list = room_list  
        self.location = location

    def get_room_list(self):
        return self.room_list

    def get_location(self):
        return self.location

    def check_in(self, customer, room_type):
        for room in self.room_list:
            if room_type.lower() == "luxury" and isinstance(room, LuxuryRoom) and not(room.occupied):
                room.occupied = True
                room.assigned_customer = customer
                customer.room = room
                return True
            elif room_type.lower() == "standard" and isinstance(room, StandardRoom) and not(room.occupied):
                room.occupied = True
                room.assigned_customer = customer
                customer.room = room
                return True
        return False

    def check_out(self, customer):
        room = customer.room
        if room and room.occupied and room.assigned_customer == customer:
            rent = room.calculate_room_rent(customer.get_no_of_days())
            room.occupied = False
            room.assigned_customer = None
            customer.room = None
            return rent
        else:
            return False



room1 = LuxuryRoom(500)
room2 = LuxuryRoom(500)
room3 = StandardRoom(300)
room4 = StandardRoom(300)

hotel = Hotel([room1, room2, room3, room4], "Hogwarts School Of Magic")

cust = Customer("Alice", "123 Main St", 7)

if hotel.check_in(cust, "luxury"):
    print(f"Customer {cust.get_cust_name()} checked in to room {cust.room.room_id}.")
else:
    print("No available room of the desired type.")

rent = hotel.check_out(cust)
if rent is not False:
    print(f"Customer {cust.get_cust_name()} checked out. Total rent: {rent}")
else:
    print("Customer was not checked in.")


