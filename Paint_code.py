class Library(object): # Contains relevant methods

    def get_digits(self, prompt): # Makes sure the user input only contains digits
        while True:
            digits = input(prompt)
            if digits.isdigit():
                return digits
    
    def paint_codes(self): # Dictionaries containing colors and finishes
        colors = {
            "00": "black",
            "10": "white",
            "20": "green",
            "30": "blue",
            "40": "red",
        }
        finishes = {"0": "matt", "1": "glossy"}
        return colors, finishes

    def convert_to_list(self, string): # Converts paint code into a color and a finish 
        if not isinstance(string, str):
            return None
        paint_code_lst = []
        paint_code_lst = paint_code_lst + [string[0:2], string[2:]]
        return paint_code_lst # Ex: ["00", "0"]


def main():
    library = Library() # Skapa ett objekt av klassen Library
    paint_code = library.get_digits("Enter paint code: ") # Ta emot och bekräfta inmatningen
    colors, finishes = library.paint_codes() 
    lst = library.convert_to_list(paint_code)

    match lst:
        case [ first, second ]: 
            if (first in colors) and (second in finishes):
                print(f"Color: {colors[first]} \nFinish: {finishes[second]}")
            elif (first in colors) and (second not in finishes):
                print(f"Color: {colors[first]} \nFinish code unknown")
            elif (first not in colors) and (second in finishes):
                print(f"Color: Color code unknown \nFinish: {finishes[second]}")
        case _:
            print("Color: Color code unknown \nFinish code unknown")

main()