def main():
    while True:
        try: 
           number = input(int("Enter a numeric value: "))   
        except ValueError:
            print(f"{number} is not a numeric value, try again.")
        else:
            print(f"{number} is a valid numeric value.")
            break



    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
