#create a new list named shopping_list
shopping_list = [] #BEING USED IN A GLOBAL FASHION




def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP' for this help.
    Enter 'SHOW' to see your current list. 
    """)

#create a function named add_to_list that declares a parameter named item
def add_to_list(item):
    #add item to the list
    shopping_list.append(item)
    #Notify user that the item was added and number of items listed currently 
    print("Added: List has {} items.".format(len(shopping_list)))

#define a function named show_list that prints all the items in the list
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)

show_help()
while True: 
    new_item = input("> ")

    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    #enable the SHOW command to show the list. Don't forget to update the HELP documentation.
    #HINT: make sure to run it
    elif new_item == "SHOW":
        show_list() 
        continue #controls flow, if not added then show will appear in shopping list 


    #call add_to_list with new_item as argument  
    add_to_list(new_item)

show_list()
