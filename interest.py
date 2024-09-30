from colorama import Fore, Style
def get_amount():
    while True:
        try:
            amount = float(input("Enter loan amount: "))
        except ValueError:
            print("Invalid input. Enter a positive number.")
            continue
        return amount

def get_rate():
    while True:
        try:
            amount = float(input("Enter Annual Percentage Rate: "))
            rate = amount / 100
        except ValueError:
            print("Invalid input. Enter a positive number.")
            continue
        return rate
    
def calc(amount, rate):
    total = amount
    apr = total * rate
    for i in range(10):
        total += apr
        apr = total * rate
        print(f"Year {i + 1} is {round(total, 2)}")
    interest = total - amount
    print(f"\nYou paid ${interest:.2f} in interest!" + Style.RESET_ALL)

amount = get_amount()
rate = get_rate()

print(Fore.CYAN + f"\nLoan Calculator\n\n${amount:.0f} over 10 years at {rate * 100:.0f}% APR\n")

calc(amount, rate)