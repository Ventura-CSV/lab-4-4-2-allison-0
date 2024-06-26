def main():
    while True:
        try: 
           number = int(input("Enter a numeric value: "))   
        except ValueError:
            print(f"{number} is not a numeric value, try again.")
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
