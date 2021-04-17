customer = "Robert"

index = 1 #Index to check how many times did they called customer
while True:
    print("{0}, Your order is ready.".format(customer))
    index += 1

    if index >= 3:
        print("We called you {0} times".format(index - 1))
        if index >= 15:
            print("This is final call. Your order will dispose soon.")
            if index >= 16:
                print("Your order has been disposed")
                break