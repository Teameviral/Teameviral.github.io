import upipayment

# Define a list to store the items in the cart
cart = []

# Define a function to add an item to the cart
def add_to_cart(item):
    cart.append(item)
    print(f'{item} has been added to your cart.')

# Define a function to handle the checkout process
def checkout():
    total_cost = 0
    for item in cart:
        total_cost += item['price']
    print(f'Your total cost is {total_cost}.')

    # Collect the user's UPI ID
    upi_id = input('Please enter your UPI ID: ')

    # Initialize the UPI payment object
    upi = upipayment.UPI()

    # Prepare the transaction
    txn = upi.prepare_transaction(upi_id, total_cost)

    # Send the transaction
    txn_response = upi.send_transaction(txn)

    # Check the transaction status
    if txn_response.status == 'SUCCESS':
        print('Transaction successful!')
    else:
        print(f'Transaction failed: {txn_response.message}')

# Example usage:
item1 = {'name': 'Product 1', 'price': 100}
add_to_cart(item1)

item2 = {'name': 'Product 2', 'price': 200}
add_to_cart(item2)

checkout()
