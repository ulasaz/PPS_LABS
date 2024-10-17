import math

def main():
    while True:
        print("Please enter 3 coefficients of quadratic equation (a, b, c): ")

        try:
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
        except ValueError:
            print("One of the provided values is not a valid number.")
            if not should_continue():
                print("Bye!")
                break
            continue

        if a == 0:
            print("Coefficient a cannot be zero for a quadratic equation.")
            if not should_continue():
                print("Bye!")
                break
            continue

        d = calculate_delta(a, b, c)

        if d < 0:
            print("The equation doesn't have real solutions.")
        elif d == 0:
            x = -b / (2 * a)
            print(f"The equation has one solution: x = {x}")
        else:
            x1, x2 = calculate_roots(a, b, d)
            print(f"The equation has two solutions: x1 = {x1}, x2 = {x2}")
        
        if not should_continue():
            print("Bye!")
            break

def calculate_delta(a: float, b: float, c: float) -> float:
    delta = math.pow(b, 2) - 4 * a * c
    return delta
def calculate_roots(a: float, b: float, delta: float) -> tuple:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2

def should_continue() -> bool:
    print("Do you want to continue ? y/n: ")
    if(input() == "n"):
        return False
    
    return True      
main()