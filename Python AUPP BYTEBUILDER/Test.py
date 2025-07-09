# more sophisticated version
def print_table(num:float, from_range:int = 1, to_range:int = 12) -> None:
    """
    This function outputs a multiplication table of up to 12 to standard out.
    
    num (float): a number to multiply with and generate the corresponding multiplication table
    from_range (int): the lowerbound of the enumeration. 1 by default
    to_range (int): the upperbound of the enumeration. 12 by default
    
    return: None
    """
    for i in range(from_range, to_range+1):
        # round the results to 2 decimal places
        print(f"{num} * {i} = {num*i:.02f}")
    
def get_number_from_user() -> float:
    """
    This function allows the user to enter a number, loop until a valid number is entered and returns that value. 
    """
    
    while not (user_input:=input("Enter your number: ")).replace('.', '', 1).replace('-', '', 1).isdigit():
        # checks whether the value entered is valid
        pass

    return float(user_input)
    
    

if __name__ == "__main__":
    print_table(get_number_from_user())