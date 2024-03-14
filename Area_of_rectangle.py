import sys
sys.path.append("..")
from Reusable_code.Must_contain import Get_Input 
    
def main():
    Get_input = Get_Input() # Create object of Get_Input class
    side_a = Get_input.get_input("Enter length of side a: ")
    side_b = Get_input.get_input("Enter length of side b: ")

    area = (side_a * side_b) # Calculate area of the triangle
    print(f"Area of the rectangle is {area}.")

if __name__ == '__main__':
    main()