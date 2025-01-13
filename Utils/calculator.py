import math as m
class Calculator:
    def is_correct(self,arr):
        for x in arr:
            if not x.isdigit():
                return False
        return True
    def secure_for_divide(self, arr):
        for y in arr[1:]:
            if y == 0:
                return False
        return True
    def select_operation(self, op):
        match op:
            case "+":
                ##Przykłady bez literowania
                print("Podaj liczby do dodania oddzielone przecinkiem")
                x = input().split(",")
                if (self.is_correct(x) == False):
                    print("Wprowadzone liczby nie są poprawne")
                else:
                    int_x = list(map(int, x))
                    print(sum(int_x))
                    with open("log.txt","a") as log:
                        log.write("liczby: "+ " ".join(x)+" operacja: "+' + '+"wynik:" + str(sum(int_x))+"\n")
                return True

            case "-":
                print("Podaj liczby do odjęcia oddzielone przecinkiem")
                x = input().split(",")
                if (self.is_correct(x) == False):
                    print("Wprowadzone liczby nie są poprawne")
                else:
                    int_x = list(map(int, x))
                    print(int_x[0]-sum(int_x[1:]))
                    with open("log.txt", "a") as log:
                        log.write("liczby: "+ " ".join(x) +" operacja: "+ ' - ' +"wynik: " + str((int_x[0]-sum(int_x[1:])))+"\n")
                return True


            case "*":
                ##Przykłady z literacją
                print("Podaj liczby do mnożenia oddzielone przecinkiem")
                x = input().split(",")
                if (self.is_correct(x) == False):
                    print("Wprowadzone liczby nie są poprawne")
                else:
                    int_x = list(map(int, x))
                    rtn = 1
                    for i in int_x:
                        rtn *= i
                print(rtn)
                with open("log.txt", "a") as log:
                    log.write("liczby: "+" ".join(x) +" operacja: "+ ' * '+"wynik: " + str(rtn)+"\n")
                return True

            case "/":
                print("Podaj liczby do dzielenia oddzielone przecinkiem")
                x = input().split(",")
                int_x = list(map(int, x))
                if (self.is_correct(x) == False):
                    print("Wprowadzone liczby nie są poprawne")
                elif (self.secure_for_divide(int_x) == False):
                    print("Nie można dzielić przez zero")
                else:
                    rtn = int_x[0]
                    for i in int_x[1:]:
                        rtn /= i
                    print(rtn)
                    with open("log.txt", "a") as log:
                        log.write("liczby: "+" ".join(x) +" operacja: " + ' / '+"wynik: " + str(rtn)+"\n")
                return True

            case "!":
                ##Przykład z wykorzystaniem biblioteki
                print("Podaj liczbe do silni")
                x = input()
                if(x.isdigit()):
                    print(m.factorial(int(x)))
                    with open("log.txt", "a") as log:
                        log.write("liczby: "+" ".join(x) + " operacja:"+' ! '+"wynik: " + str(m.factorial(int(x)))+"\n")
                else:
                    print("Wprowadzona liczba jest niepoprawna")
                return True

            case "^":
                ##Przykład z literacją
                print("Podaj liczby do potęgowania oddzielone przecinkiem(najpierw podstawa, później wykładniki")
                x = input().split(",")
                int_x = list(map(int, x))
                if (self.is_correct(x) == False):
                    print("Wprowadzone liczby nie są poprawne")
                else:
                    rtn = int_x[0]
                    for i in int_x[1:]:
                        rtn = rtn**i
                    print(rtn)
                    with open("log.txt", "a") as log:
                        log.write("liczby: " +" ".join(x) +" operacja:" + ' ^ '+"wynik: " + str(rtn)+"\n")
                return True

            case "q":
                print("powrót do ekranu głównego")
                return False
            case _:
                print("Nieprawidłowa komenda")
                return True