from Utils.calculator import Calculator as Calc
from Utils.file_helper import File_helper as Fh
calculator = Calc()
file_helper = Fh()

while True:
    print("Co chcesz zrobić?")
    inp = input()

    match inp:
        case "quit":
            break
        case "calc":
            print("Co chcesz zrobić?")
            x = input()
            while calculator.select_operation(x):
                print("Co chcesz zrobić?")
                x=input()
        case "files":
            print("Co chcesz zrobić?")
            x = input()
            while file_helper.file_manager(x):
                print("Co chcesz zrobić?")
                x=input()
        case _:
            print("Nieprawidłowa komenda")
