from inventory.inventory import Inventory

class ResourceCenter:
    def __init__(self):
        ## Prepare the data (Inventory list)
        self.inventory = Inventory() 

    def display_menu(self):
        choice = -1
        while not 1 <= choice <= 5:
            print("\n==============================================")
            print('RESOURCE CENTRE SYSTEM by Lucas:')
            print("1. Add item")
            print("2. Display Inventory")
            print("3. Loan item")
            print("4. Return item")
            print("5. Quit")
            choice = int(input("Enter your choice >"))
            if not 1 <= choice <= 5:
                print("Invalid choice, please enter again.\n")
        return choice

    def print_header(self, message):
        print("\n==============================================")
        print(message)
        print("==============================================")

    def select_item_type(self):
        print("\nItem types:")
        print("1. Digital Camera")
        print("2. Laptop")
        option = int(input("Enter option to select item type >"))
        return option

    def main(self):
        #### Menu driven application ####
        # Display menu and obtain menu choices
        choice = self.display_menu()

        while choice != 5:
            if choice == 1:
                self.print_header("Add an item")
                option = self.select_item_type()
                
                # TO-DO: Write the code to ADD a digital camera or laptop.
                if option == 1:
                    assetTag = input("Enter asset tag >")
                    description = input("Enter description >")
                    opticalzoom = int(input("Enter optical zoom >"))
                    result = self.inventory.addCamera(assetTag, description, opticalzoom)
                    if result:
                        print("Digital camera added.")
                    else:
                        print("Error adding digital camera.") 
                elif option == 2:
                    assetTag = input("Enter asset tag >")
                    description = input("Enter description >")
                    os = input("Enter os >")
                    result = self.inventory.addLaptop(assetTag, description, os)
                    if result:
                        print("Laptop added.")
                    else:
                        print("Error adding laptop.")
                else:
                    print("Invalid item type.")

            elif choice == 2:
                self.print_header("Display all items")
                print(self.inventory.getAvailableCamera())
                print(self.inventory.getAvailableLaptop())

            elif choice == 3:
                self.print_header("Loan an item")
                option = self.select_item_type()

                # TO-DO: Write the code to LOAN a Digital camera or Laptop
                if option == 1:
                    print(self.inventory.getAvailableCamera())
                    assetTag = input("Enter asset tag >")
                    duedate = input("Enter due date >")
                    result = self.inventory.loanCamera(assetTag, duedate)
                    if result:
                        print("Camera", assetTag, "successfully loaned out.")
                    else:
                        print("Error loaning camera.")
                elif option == 2:
                    print(self.inventory.getAvailableLaptop())
                    assetTag = input("Enter asset tag >")
                    duedate = input("Enter due date >")
                    result = self.inventory.loanLaptop(assetTag, duedate)
                    if result:
                        print("Laptop", assetTag, "successfully loaned out.")
                    else:
                        print("Error loaning laptop.")
                else:
                    print("Invalid item type.")

            elif choice == 4:
                self.print_header("Return an item")
                option = self.select_item_type()

                # TO-DO: Write the code to RETURN a camcorder or chrome book

            else:
                print("Invalid choice.")
            
            choice = self.display_menu()

        print("Good bye.")

if __name__ == "__main__":
    app = ResourceCenter()
    app.main()
