import cellphoneclass as P

def main():

    man = input("Enter manufacturer: ")
    mod = input("Enter model: ")
    rp = float(input("Enter retail price: "))

    phone = P.Phone(man,mod,rp)

    phone.set_retail_price(1400)
    
    print(f"Manufacturer: {phone.get_manufact()}")
    print(f"Model: {phone.get_model()}")
    print(f"Retail Price: {phone.get_retail_price()}")


main()