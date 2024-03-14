
def get_input(prompt):
    while True:
        try:
            input_val = input(prompt)
            int_val = int(input_val)
            if isinstance(int_val, int):
                return int_val
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number")
    

def main():
    radius = get_input("Enter length of the circle's radius: ")
    if radius:
        area = (radius**2) * 3.14
        print(f"Area of the circle is {area:.2f}")

if __name__ == '__main__':
    main()
