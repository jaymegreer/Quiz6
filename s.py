class Order: #defines what an order needs
    def __init__(self, order_details, total_amount):
        self.order_details = order_details
        self.total_amount = total_amount

class OrderDetails: #defines what is needed for an order
    def __init__(self, customer_info, items, shipping_address):
        self.customer_info = customer_info
        self.items = items
        self.shipping_address = shipping_address

class PriceCalculator: #calculates price including tax
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate

    def calculate_total(self, order): #does the actual calculating 
        subtotal = sum(order.order_details.items[item] for item in order.order_details.items)
        tax = subtotal * self.tax_rate
        return subtotal + tax

class ValidateData: #validates if an item is available 
    def __init__(self, inventory):
        self.inventory = inventory

    def validate_order(self, order): #actually does the validating..if item is not in inventory or it = 0, then it's not available
        for item in order.order_details.items:
            if item not in self.inventory or self.inventory[item] == 0:
                print(f"Error: Item '{item}' not available.")
                return False
        return True #otherwise it is

class OrderConfirmation: #class that sends email confirmation 
    def send_confirmation(self, order, email):
        confirmation_message = f"{order.order_details.items} will be shipped to {order.order_details.shipping_address}."
        print(f"Email sent to {email}: {confirmation_message}")

class UpdateInventory: #updates inventory to subtract 1 from quantity after being purchased
    def update_inventory(self, order):
        for item in order.order_details.items:
            order.inventory[item] -= 1
        print("Inventory updated.")

def main(): #demonstrates usage
    #dummy values
    customer_info = "Jayme Greer"
    items = {"Item1": 1, "Item2": 1} 
    shipping_address = "123 Cougar St, Edwardsville"
    tax_rate = 0.1
    inventory = {"Item1": 5, "Item2": 3}

    #instances of classes
    order_details = OrderDetails(customer_info, items, shipping_address)
    order = Order(order_details, total_amount=0) 
    order.inventory = inventory  

    price_calculator = PriceCalculator(tax_rate)
    validate_data = ValidateData(inventory)
    order_confirmation = OrderConfirmation()
    update_inventory = UpdateInventory()

    #usage
    if validate_data.validate_order(order):
        total_cost = price_calculator.calculate_total(order)
        order_confirmation.send_confirmation(order, "jaymgre@siue.edu")
        update_inventory.update_inventory(order)
        print(f"Total cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
