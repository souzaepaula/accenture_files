#QA Automation Challenge API
#Rodrigo de Paula
#Oct 2024

#Libs
import requests 

#URL define

LOGIN_URL = "https://demoqa.com/swagger/V1"

USER_URL = "https://demoqa.com/Account/v1/User"

TOKEN_URL = "https://demoqa.com/Account/v1/GenerateToken"

AUTH_URL = "https://demoqa.com/Account/v1/Authorized"

BOOK_LIST_URL = "https://demoqa.com/BookStore/v1/Books"

RENT_BOOKS_URL = "https://demoqa.com/BookStore/v1/Books"


# %%
#Creating user 

#Enter username and password 
username = input("Enter your username:")
password = input("Enter your password:")

def create_user():
    payload = {
        "userName": username,
        "password": password
    }

    response = requests.post(USER_URL, json=payload)

    if response.status_code == 201:
        print("User created successfully!")
        response_data = response.json()

    else:
        print("User creation failure:", response.json())
    
    return response.json()

create_user()

# %%
#Token generation
def get_token():
    payload = {
        "userName": username,
        "password": password
    }
    
    response = requests.post(TOKEN_URL, json=payload)

    if response.status_code == 200:
        token = response.json().get('token')
        print("Token generated successfully!")
        return token
    else:
        print("Token generation failure:", response.json())
        return None
    
get_token()

# %%
#User authentication 
def authentication():
    payload = {
        "userName": username,
        "password": password
    }

    response = requests.post(AUTH_URL, json=payload)

    if response.status_code == 200:
        print("User authentication done!")
    else:
        print("User authentication failure:", response.json())
    
    return response.json()

authentication()

# %%
#Book list generation 
def book_list():
    payload = {
        "userName": username,
        "password": password
    }

    response = requests.get(BOOK_LIST_URL, json=payload)

    if response.status_code == 200:
        print("Book list created!")
        
    else:
        print("Book list failure:", response.json())
    
    return response.json()

book_list()

# %%
#Book list done
def book_titles():
    data = book_list()
   
    if data and 'books' in data:
        titles = [book['title'] for book in data['books'] if 'title' in book]
        return titles
    
    else:
        print("Book list creation failure!")
        return []


book_titles = book_titles()

for titles in book_titles:
    print(titles)


