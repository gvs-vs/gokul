class GroceryItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price

#creating store class with their attributes

class GroceryStore:
    def __init__(self):
        self.inventory = [ 
            GroceryItem("Apples", 1.20),

            GroceryItem("Banana", 0.50),

            GroceryItem("Bread", 2.00),

            GroceryItem("Milk", 1.50)
        ]
        
        self.cart =[]

#defining methods to display items

    def display_items(self):

        print("\nAvailable items: ")

        for index, item in enumerate(self.inventory):

            print(f"{index + 1}. {item.name} - {item.price: 2f}")

    
#defining method for add to cart
    def add_to_cart(self, item_number, quantity):
        if 0 < item_number <= len(self.inventory):

            item = self.inventory[item_number - 1]
            self.cart.append((item, quantity))

            print(f"Added {quantity} x {item.name} to your cart.")
        
        else:
            print("Invalid item number")

#defining method to view cart   
    def view_cart(self):

        if not self.cart:
            print("Your cart is empty. ")
        
        else:

            print('\nYour cart: ')

            total_cost = 0

            for item, quantity  in self.cart:

                cost = item.price * quantity

                print(f"{quantity} x {item.name} - {cost: 2f}")

                total_cost += cost
            print(f"Total: {total_cost: 2f}")

     #defining method to checkout
    
    def checkout(self):

        if not self.cart:
            print("Your cart is empty")
        
        else:

            self.view_cart()
            print("\nProceeding to checkout...")


            self.cart = []

#user interference:

def main():

    store = GroceryStore()

    while True:

        print("\n1. View items")
        print("2. Add to cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")

        choice= input("\nEnter your choice (1-5): ")

        if choice =='1':

            store.display_items()

        elif choice == '2':
            store.display_items()

            item_number = int(input("Enter item number to add to cart: "))

            quantity = int(input("Enter quantity : "))

            store.add_to_cart(item_number, quantity)

        elif choice == '3':
            store.view_cart()

        elif choice == '4':
            store.checkout()

        elif choice == '5':
            print("Thanks for your shopping" )

            break

        else:
            print("Invalid Choice")

#adding code to run
if __name__ == "__main__":
    main()

        
           

    