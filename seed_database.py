import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb food_name")
os.system('createdb food_name')
model.connect_to_db(server.app)
server.app.app_context().push()

model.db.create_all()


    
customer = crud.create_customer(name="Jhon", email="jhon@hotmail.com", password="test", phone="567-767-6767", street="applause place", city="sf", state="CA", zipcode="98692")
model.db.session.add(customer)

    

        

model.db.session.commit()