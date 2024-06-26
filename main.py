def main():
    while True:
        try: 
           number = input("Enter a numeric value: ")
           isNumeric = float(number)
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
