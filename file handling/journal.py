Filename = 'journal.txt'
def write_entry():
    entry = input("enter youo text")
    with open(Filename,'a') as file:
        file.write(entry)

def read_all():
    with open (Filename,'r') as file:
        print("ALL DATA")
        print(file.read())

def search():
    keyword =input("enter word to be search") 

    with open(Filename,'r') as file:
        all_lines = file.readlines()
        for line in all_lines:
            if keyword.lower() in line.lower():
                print(line.strip()) #strip is used to skip the extra spaces and words
                return
            print("no matching entities")


def main_menu():
    while True:

        print("File journal menu")
        print('1.ADD ENTRY')
        print('2.read all entry')
        print('3.search entries')
        print('4.exit')

        choice = input("Enter option 1 to 4")

        if choice == '1':
            write_entry()
        elif choice == '2' :
            read_all()
        elif choice == '3':
            search()
        elif choice == '4':
            print("GOOD BYE")
            break
        else:
            print("Invalid choices")

if __name__=="__main__":
    main_menu()











