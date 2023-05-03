# Toy Shopping App Development

## illustrate：

This application is a toy shopping site with a hierarchy of permissions. Users need to register to access the site to make purchases. Regular users can click on Add to Cart to complete their shopping. The app has a general search and an advanced search function to filter items.If the user wants to view the details of the product, they need to click on the item hyperlink to jump to the detail page. The details page contains information on the origin of the product and a graph of the price movements of the product, as well as information on the different products sold on that day. Of course, the details page requires admin rights to view.


    

## ** matters needing attention：**

As this application has hierarchical permissions, we need to create a super user to access the product details page before using this application, so we need to enter the following code to create a super user:


    python3 manage.py createsuperuser
        
            

# Step 1: Install the environment

cd into the folder via the terminal and execute these commands:

    pyenv local 3.7.0 # this sets the local version of python to 3.7.0
    python3 -m venv .venv # this creates the virtual environment for you
    source .venv/bin/activate # this activates the virtual environment
    pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
   
we also need install plotly:

    pip install plotly
    

# Step 2: we need data migration：

    python3 manage.py migrate
    
    
After a short wait, when all commands are OK, we enter the following code：

First, we ask Django to generate the migration file with the command:

 
    python3 manage.py makemigrations shopping
    

    
This will read the models.py file and generate a migration file based on changes found there.

Second, we run the generated migration with the command:
 
    python3 manage.py migrate shopping   
    
With this we can drop the data from the table, and then load it in, as required. We don't use any libraries for this as we want to pull specific fields from the file. Run the file with the command:

    python3 manage.py parse_csv

# Step 3: Start the Server： 

We so this using the manage.py command tool by entering this command in the terminal:


    python3 manage.py runserver
    
If you're doing this on another platform, then you might need to use this instead (change the port number from 8000 as required):


    python3 manage.py runserver 0.0.0.0:8000 
    
# Step 4: Using the tests： 

There are some basic tests here too, so that you can see how you can test the code works correctly. They are in the 'tests' folder, and cover model and view tests. There is some repeated code to load the test database, which can probably be refactored out into a sepaate file that is called by the test files. Run the tests with the command:

    python3 manage.py test   
    
   
You can also add '/admin' after the home page to access the backend admin system to re-bid items, delete items etc
    
