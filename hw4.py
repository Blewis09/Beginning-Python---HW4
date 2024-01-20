# Your parking garage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# By the end of this project each student should be able to:
# - Explain and/or demonstrate creating classes
# - Explain and/or demonstrate creating class methods
# - Explain and/or demonstrate class instantiation

# Make sure that your program runs like a program. It should have a while loop that repeats until the user decides to quit.

# When the project is completed, commit the final changes and submit your GitHub link.


class ParkingGarage():

        def __init__(self,space = 10):
                self.tickets = set(range(1,space+1))
                self.parkingSpaces = [0] * space
                self.currentTicket = {}

        def takeTicket(self):
                ticketNumber = self.tickets.pop()
                self.parkingSpaces[ticketNumber-1] = 1
                print(ticketNumber)
                self.currentTicket[ticketNumber] = False

        def payForParking(self):
                ticketNumber = int(input("Please enter your ticket number"))
                self.currentTicket[ticketNumber] = True
                print("Thanks, you have 15 mins to exit the parking garage")

        def leaveGarage(self):
                ticketNumber = int(input("Please insert your ticket"))
                if ticketNumber in self.currentTicket and self.currentTicket[ticketNumber] == True:
                        print("Thank you, have a nice day") 
                        self.tickets.add(ticketNumber)
                        self.parkingSpaces[ticketNumber-1] = 0
                        del self.currentTicket[ticketNumber]  
                else:          
                        print("Please go back and pay")

        def runProgram(self):
                while True:
                        XXX = input("Please enter an option to either take a ticket, pay for your ticket, leave or quit")
                        if XXX == "take a ticket":
                               self.takeTicket()
                        elif XXX == "pay for your ticket":
                               self.payForParking()
                        elif XXX == "leave":
                               self.leaveGarage()
                        elif XXX == "quit":
                                break 


g1 = ParkingGarage()
g1.runProgram()