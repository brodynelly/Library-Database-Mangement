Hello, my name is Brody Nelson, and this is my final project in CMP_SC 3380. The purpose of this project is to pose a 
library management system for a library to store records of books, keep track of librarians, patrons and record the transactions
between books leaving and returning from the Library. This project utilizes MySQL for the DBMS and the application uses python
to work as the backend to pose the necessary SQL queuries to retrieve the necessary data from the database. 

Deploying the Database and Utilizing the Library Application, can be done in two different segments. 

First, when deploying the database I tried to make it process as easy as possible for anyone who might be using this application. 
Personally, in creating this application I was working with MySQL from my local computer and created a new user and instance. 
If you havn't already done this, I would recommend dowloading mySQL and creating an instance and a user keeping track of the username and 
password and the name you used for your host, after you have done this, you can follow these steps to deploy the DATABASE: 

1. Go into ./Database directory from the root file, and change the information in database.py to corespond to your created mySQL user,
password and host. there are some instructions in database.py to help you run the code and deploy the database and poplute the databse
with artificial data. 
(p.s., you are able to tinker with the populated data in databse.py by adding more rows to the INSERT INTO commands)

Secondly, is interacting with the database that you have just created with the LibraryApp application coded in python. This is an application that
allows for different end users/different views to interact with the Library Management database. To actually use the database application, you must only do two things,
which are: 

1. navigate to ./LibraryApp and in sqlqueries.py please change the information in connect_to_database() to accomodate to your instance of MySQL
that you created in database.py in the previous set of directions. 
2. After changing this, you are ready to connect to your created database and start using the library application, to do this, run the python file main.py 
and enjoy the application. 