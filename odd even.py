# Function to check if the number is odd or even
def check_odd_even():
    # Input a number from the user
    number = int(input("Enter a number: "))
    
    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

# Start the function
if __name__ == "__main__":
    check_odd_even()