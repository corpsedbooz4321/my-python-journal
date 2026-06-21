# Traffuc light code


def traffic_light(colour):
    colour = colour.lower()  # makes it case sesitive

    if colour == "red":
        return "stop!"
    elif colour == "yellow":
        return "go slow"
    elif colour == "green":
        return "begone"
    else:
        return "invalid colour!"

    # return colour


while True:
    colour = input("Enter the name of your colour: ")

    if colour == "done":
        break

    print(traffic_light(colour))
