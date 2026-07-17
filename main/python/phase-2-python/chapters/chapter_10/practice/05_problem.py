"""Write a class train which has methods to book a ticket.
get status(no. of seats) and get fare
informatin of train running under indian Railways"""

from random import randint


class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked with train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train No: {self.trainNo} from {fro} to {to} is {randint(22, 3434)}")


t = Train(13299)
t.book("Patna", "America")
t.getstatus()
t.getFare("Patna", "America")