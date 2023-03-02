"""CRUD operations."""

from model import db, Customer,Payment, Order,OrderItem, MenuItem, connect_to_db


def create_customer(name,email,password,phone,street,city,state,zipcode):
    """Create and return a new customer."""

    customer = Customer(name=name, email=email, password=password, phone=phone, street=street, city=city, state=state, zipcode=zipcode)
    return customer


def create_payment(card_number,orders):
    payment = Payment(card_number=card_number,orders=orders)
    return payment


    
def create_order(customer,payment,order_items):
    order = Order(customer=customer, payment=payment, order_items=order_items)
    return order



def create_order_item(quantity, price, orders,  menu_item):
    order_item = OrderItem(quantity=quantity, price=price, orders=orders,  menu_item=menu_item)
    return order_item


def create_menu_item(name,price,image,order_item):
    menu_item = MenuItem(name=name, price=price,image=image, order_item=order_item)
    return menu_item




if __name__ == '__main__':
    from server import app
    connect_to_db(app)