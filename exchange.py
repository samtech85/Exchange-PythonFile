

print("***************************************")
print("*******WELCOME to E-XchangePro*********\n")
todayRate = int(input("What is the rate today: \n"))


print("Press 'G' if you have Gourdes, or")
print("Press 'D' if you have USD \n")

askIfChange= input(":")




if askIfChange == "g":
    inputAmount = input("Enter Your gourde's Amount (in dollars HT): \n")

elif askIfChange == "d":
    inputAmount = input("Enter Your Dollar's Amount: \n")
    




# Conditions


if askIfChange == "g":
    ExchangeToUs = (int(inputAmount) * 5) / todayRate
    print("***************************************")
    print(inputAmount, "HT is :", ExchangeToUs, "USD")
    print("***************************************")


elif askIfChange == "d":
    ExchangeToGdes = (int(inputAmount) * todayRate)
    ExchangeToDollarsHt = ExchangeToGdes / 5
    print("***************************************")
    print(inputAmount, "USD is :", ExchangeToGdes, "HT ***(", ExchangeToDollarsHt , ")****" )
    print("***************************************")
