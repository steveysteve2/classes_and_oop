import InsectClass as I

def main():
       
       hf = I.Insect(2,4,'housefly')
       hf.lenflight() 
       length = hf.get_len()
       print(f'The {hf.get_name()} can fly {length} miles')

       mos = I.Insect(2,4,'mosquito')
       mos.lenflight() 
       length = mos.get_len()
       print(f'The {mos.get_name()} can fly {length} miles')

# Call the main function.

main()