"""
Problem : Find the cheapest number of cars that can be rented base on the type of car , seat capacity and price.

The default value of car rental data is the following :

Small Car  
seat capacity : 5 
price in php : 5000

Medium Car  
seat capacity : 10 
price in php : 8000

Large Car  
seat capacity : 15 
price in php : 12000


Input : No of seats needed assuming all inputs are positive integers ONLY and no 0 integer input.

Process : Find the type and no of cars needed to get the cheapest rental car.

Output : Print out the type of car and no of cars needed and the total amount.

"""


import math

class RentalCarsCls:
    def __init__(self,input_car_capacity):
        self.input_car_capacity = input_car_capacity

        # Default value 
        self.different_cars_list ={
        "small_car" : {"seat_capacity":5, "price_php": 5000},
        "medium_car" : {"seat_capacity":10, "price_php": 8000},
        "large_car" : {"seat_capacity":15, "price_php": 12000}
        }

    
    def check_rental_cars_mth(self):
        """
        Check if the seat capacity is < or == the following type of cars
        """

        # Get all car capacity 
        self.small_car_capacity = self.different_cars_list["small_car"]["seat_capacity"]
        self.medium_car_capacity = self.different_cars_list["medium_car"]["seat_capacity"]
        self.large_car_capacity = self.different_cars_list["large_car"]["seat_capacity"]

        # Get all car price
        self.small_car_price = self.different_cars_list["small_car"]["price_php"]
        self.medium_car_price = self.different_cars_list["medium_car"]["price_php"]
        self.large_car_price = self.different_cars_list["large_car"]["price_php"]
       

        if self.input_car_capacity <= self.small_car_capacity:
            print("Small Car x 1")
            print(f"TOTAL AMOUNT = PHP {self.small_car_price}")

        elif self.input_car_capacity <=  self.medium_car_capacity:
            print("Medium Car x 1")
            print(f"TOTAL AMOUNT = PHP {self.medium_car_price}")

        elif self.input_car_capacity <=  self.large_car_capacity:
            print("Large Car x 1")
            print(f"TOTAL AMOUNT = PHP {self.large_car_price}")

        else:
            self.find_combination_seat_capacity_mth()



    def find_combination_seat_capacity_mth(self):
        """
        Find the type of car that have the cheapest price base on seat capacity 
        """
        # Get the number of cars needed base on the type of car
        # Get number of input divide by the car capacity and round up 
        no_small_cars  = math.ceil(self.input_car_capacity/self.small_car_capacity)
        no_medium_cars = math.ceil(self.input_car_capacity/self.medium_car_capacity)
        no_large_cars = math.ceil(self.input_car_capacity/self.large_car_capacity)

        # Get the all the total price base on cars 
        small_cars_total_price = no_small_cars * self.small_car_price
        medium_cars_total_price = no_medium_cars * self.medium_car_price
        large_cars_total_price = no_large_cars * self.large_car_price
    


        if small_cars_total_price <= medium_cars_total_price and small_cars_total_price <= large_cars_total_price:
            print(f"Small Car x {no_small_cars}")
            print(f"TOTAL AMOUNT = PHP {small_cars_total_price}")

        elif medium_cars_total_price <= small_cars_total_price and  medium_cars_total_price <= large_cars_total_price:
            print(f"Medium Car x {no_medium_cars}")
            print(f"TOTAL AMOUNT = PHP {medium_cars_total_price}")

        elif large_cars_total_price <= small_cars_total_price and  large_cars_total_price <= medium_cars_total_price:
            print(f"Large Car x {no_large_cars}")
            print(f"TOTAL AMOUNT = PHP {large_cars_total_price}")
        



        # Comment out if you wanna check over all result
        # print("Overall result for comparison")
        
        # print(f"Small Car x {no_small_cars}")
        # print(f"TOTAL AMOUNT = PHP {small_cars_total_price}")


        # print(f"Medium Car x {no_medium_cars}")
        # print(f"TOTAL AMOUNT = PHP {medium_cars_total_price}")
        
        # print(f"Large Car x {no_large_cars}")
        # print(f"TOTAL AMOUNT = PHP {large_cars_total_price}")
    


    def change_small_car_mth(self,seat_capacity= 5, price_php = 5000):
        """
        Change the small car seat capacity and price base on the arguments.
        """

        self.different_cars_list["small_car"]["seat_capacity"] = seat_capacity
        self.different_cars_list["small_car"]["price_php"] = price_php 
       
        
        
    def change_medium_car_mth(self,seat_capacity= 10, price_php = 8000):
        """
        Change the medium car seat capacity and price base on the arguments.
        """
        
        self.different_cars_list["medium_car"]["seat_capacity"] = seat_capacity
        self.different_cars_list["medium_car"]["price_php"] = price_php


    def change_large_car_mth(self,seat_capacity= 15, price_php = 12000):
        """
        Change the large car seat capacity and price base on the arguments.
        """
        self.different_cars_list["large_car"]["seat_capacity"] = seat_capacity
        self.different_cars_list["large_car"]["price_php"] = price_php





if __name__ == '__main__':

    user_input_no_seats = int(input("Please input no of seats :"))
    rent_cars_obj = RentalCarsCls(user_input_no_seats)

    # You can change cars price and capacity by commenting this out and changing it values
    # rent_cars_obj.change_small_car_mth(seat_capacity= 4, price_php = 4000)
    # rent_cars_obj.change_medium_car_mth(seat_capacity= 9, price_php = 7000)
    # rent_cars_obj.change_large_car_mth(seat_capacity= 14, price_php = 11000)

    rent_cars_obj.check_rental_cars_mth()
