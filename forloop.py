
age = [-12,13,-14,15,-16]
username = ["juan", "pedro", "james", "sagaad", "fuego"]
for dataAge in age:
    if dataAge > 0:
        print(str(dataAge) + "negative")
    elif dataAge < 0:
        print(str(dataAge) + "positive")
        break

    for userdata in username:
        if userdata == "james":
            print("james dela cruz")
        else:
            print("james the bad")