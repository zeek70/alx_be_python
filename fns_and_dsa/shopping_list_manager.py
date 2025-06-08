def display_menu():
    print("Shopping list manager")
    print("1. To add an item")
    print("2. To remove an item ")
    print("3. View list ")
    print("4. exit ")
def main ():
    shopping_list=[]
    while True:
        display_menu()
        choice=input("enter a choice")
        if choice == "1":
            item=input("enter item name: ").strip()
            if item:
                shopping_list.append(item)
                print(f"{item} has been added to shpping list")
            else:
                print("item cannot be empty")

        elif choice == "2":
            item=input("enter an item name to remove").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from shpping list")
            else:print(f"{item} cannot be found")

        elif choice == "3":
            if shopping_list:
                print(shopping_list)
            else:
                print ("shopping list is empty")

        elif choice== "4":
            print("Goodbye!")
            break
        else:
            print("invalid selection")
        
if __name__ == "__main__":
    main()
