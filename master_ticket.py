SURCHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SURCHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?  ")
    number_of_tickets = input("Hello, {}! How many tickets would you like to buy?  ".format(name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {} Please try again.".format(err))
    else:
        amount_due = calculate_price(number_of_tickets)  
        print("Your total is ${}.".format(amount_due))
        proceed = input("Would you like to proceed with the purchase Y/N?  ")
        if proceed.lower() == "y":
            print("SOLD!")
            tickets_remaining -= number_of_tickets
        else:
            print("Thank you anyways, {}.".format(name))

print("Sorry, we are sold out of tickets.")
