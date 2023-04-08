# Inventory Web Application

This is a web application built with Python and Django framework for managing inventory. It allows users to log in, view dashboard, create, edit and delete suppliers, products, purchase orders, clients and client orders.

## Features

- User authentication
- If you are not register
![registration](https://user-images.githubusercontent.com/94300302/230700085-91e4c718-80b9-4f6b-834f-2dc140739d00.png)

then

#### Login
![login](https://user-images.githubusercontent.com/94300302/230700114-20382b6b-e813-40f5-ac9f-aadbc63e1ee4.png)
#### Dashboard
- Dashboard with graphical representation of the quantity of products and client orders
![dashboard](https://user-images.githubusercontent.com/94300302/230700162-72a2cbd1-34f1-4d6e-9d8e-19a32bba7504.png)

#### Supplier management: create, edit and delete suppliers
![supplier](https://user-images.githubusercontent.com/94300302/230700195-0044c898-059e-44b9-9e8b-95923b3b1887.png)

#### Product management: create, edit and delete products
![product](https://user-images.githubusercontent.com/94300302/230700210-ba7d4f08-258f-4ed2-be54-cf2cb146e3b0.png)

#### Purchase order management: create and view purchase orders
![purchaseorder](https://user-images.githubusercontent.com/94300302/230700221-d1f7f66f-73e3-4f8b-938e-c09016e3704e.png)

#### Client management: create, edit and delete clients
![client](https://user-images.githubusercontent.com/94300302/230700238-e6e88172-fdee-415f-bc71-d9c1c356b159.png)

#### Client order management: create and view client orders
![clientorder](https://user-images.githubusercontent.com/94300302/230700253-56a25b4a-b26c-49aa-8eb0-bd1f378590e6.png)


<hr>

#### Features that can be added to the inventory:

1. Posibility for the user to search orders(Supplier or Client) by date, code, product, supplier name or client
name. And display in a table all the data.
2. Add  the option to the user to add image in the product description. 
<hr>

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of Python
- You have installed Django and other required packages
- You have a basic understanding of Python and Django

### Installation

To install and run this application, follow these steps:

1. Clone the repository to your local machine
2. Open a terminal and navigate to the root folder of the project
3. Run `python manage.py migrate` to create the database tables
4. Run `python manage.py runserver` to start the server
5. Open a web browser and go to http://localhost:8000/ to view the login page
6. If you are a new user, click on "Register" in the top right corner to register a new account
7. After registration, you will be redirected to the login page
8. Log in with your credentials to access the dashboard

### Usage

On the dashboard, you will see a graphical representation of the quantity of products and client orders. There are several buttons that allow you to perform different operations:

- "Suppliers": click on this button to view the list of suppliers. You can create, edit and delete suppliers from here.
- "Products": click on this button to view the list of products. You can create, edit and delete products from here.
- "Purchase Orders": click on this button to create a new purchase order. You will be asked to select the category and product from the list of available products. You can view a list of all purchase orders from here.
- "Clients": click on this button to view the list of clients. You can create, edit and delete clients from here.
- "Client Orders": click on this button to create a new client order. You will be asked to select the product and enter the quantity. You can view a list of all client orders from here.

### Development

If you want to contribute to this project, you can follow these steps:

1. Fork the repository
2. Clone your forked repository to your local machine
3. Create a new branch for your changes
4. Make your changes and commit them
5. Push your changes to your forked repository
6. Create a pull request



## Inventory Web App using Django Framework

This is an Inventory Web Application developed using the Django framework. The application allows users to manage their inventory, suppliers, products, purchase orders, clients, and client orders.

### Getting Started

#### Prerequisites

- Python 3.10
- Django 4.2

#### Installation

1. Clone the repository: `git clone https://github.com/CiscoMerchan/Inventory_with_django.git`
2. Navigate to the project directory: `cd <Inventory_with_django>`
3. Create a virtual environment: `python3 -m venv env`
4. Activate the virtual environment: `source env/bin/activate`
5. Install the dependencies: `pip install -r
<hr>

#### Personal Note
I created this inventory app because I initially developed a desktop app with Python and Tkinter as the GUI. For some reason that I am still trying to figure out, I was unable to translate it from .py to .exe. So, because it was something I wanted to finish, I recreated it as a web app. At the same time, it allowed me to practice and deepen my knowledge of the principles of the Django framework. This project allowed me to understand how easy it is to work with models (db) and forms using Django and how it simplifies the hard work behind the scenes. I had previously worked on some small Flask projects and found that the main difference between the two frameworks is that Django is very opinionated, which is very helpful for someone like me at my current level.

The biggest challenge I encountered was understanding form queries without using SQL syntax and rendering the forms in a static manner. Fortunately, Django documentation is pretty good, and StackOverflow is a lifesaver. The benefit for me was learning how to read documentation.
As inspiration I saw a youtube video and I add my own touch.


