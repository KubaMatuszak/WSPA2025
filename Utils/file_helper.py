import os

class File_helper:
    def file_manager(self, inp):
        args = inp.split()
        command = args[0]

        match command:
            case "q":
                print("Wychodzisz do głównego menu.")
                return False

            case "ls":
                for item in os.listdir():
                    print(item)
                return True

            case "cd":
                if len(args) > 1:
                    try:
                        os.chdir(args[1])
                        print("Jesteś teraz w katalogu: " + os.getcwd())
                    except FileNotFoundError:
                        print("Katalog" + args[1] + "nie istnieje.")

                    except PermissionError:
                        print("Brak uprawnień do otwarcia" + args[1])
                else:
                    print("Nie podano katalogu.")
                return True

            case "pwd":
                print("Bieżąca ścieżka:" + os.getcwd())
                return True

            case "head":
                if len(args) > 1:
                    try:
                        with open(args[1], "rb") as file:
                            data = file.read(512)
                            print(data.decode(errors="??"))
                    except FileNotFoundError:
                        print("Plik: " + args[1] + " nie istnieje.")
                    except PermissionError:
                        print("Brak dostępu do pliku" + args[1])
                    except Exception as e:
                        print(e)
                else:
                    print("Nie podano pliku.")
                return True
            case _:
                print("Nieznane polecenie.")
                return True
