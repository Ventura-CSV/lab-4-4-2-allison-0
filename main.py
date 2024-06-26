def main():
    while True:
        try: 
           number = input("Enter a numeric value: ")
           isNummeric = float(number)
        except ValueError:
            print("Invalid, try again.")
        else:
            print(f"{number} is a valid numeric value.")
            break



    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
