def main():
    while True:
        try: 
           number = int(input("Enter a numeric value: "))   
        except ValueError:
            print("Invalid input.")
            continue
        else:
            print(number)
            break



    ########################################
    # Do not delete the return statement
    ########################################
    return number


if __name__ == '__main__':
    main()
