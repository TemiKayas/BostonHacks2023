import requests
import json

api_key = 'c4339d9d4f473684a342b04bcbb2ccf1'
BASE_URL = 'http://api.nessieisreal.com'

def create_customer(api_key, first_name, last_name, street_number, street_name, city, state, zip_code):
    url = f"http://api.nessieisreal.com/customers?key={api_key}"
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "address": {
            "street_number": street_number,
            "street_name": street_name,
            "city": city,
            "state": state,
            "zip": zip_code
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        return response.json()
    else:
        return "Error"
    
def create_checking_account(api_key, customer_id, nickname, rewards, balance):
    url = f"http://api.nessieisreal.com/customers/{customer_id}/accounts?key={api_key}"
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        "type": "Checking",
        "nickname": nickname,
        "rewards": rewards,
        "balance": balance
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        return response.json()
    else:
        return "Error"


def create_bill(api_key, account_id, status, payee, payment_date, payment_amount):
    url = f"http://api.nessieisreal.com/accounts/{account_id}/bills?key={api_key}"
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        "status": status,
        "payee": payee,
        "payment_date": payment_date,
        "payment_amount": payment_amount
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
    if response.status_code == 201:
        return response.json()
    else:
        return "Error"
    

def get_all_bills_for_accountDONOTUSE(api_key, account_id):
    url = f"http://api.nessieisreal.com/accounts/{account_id}/bills?key={api_key}"
    response = requests.get(url)
    print(response.json())
    if response.status_code == 200:
        return response.json()
    else:
        return "Error"

def get_customer_account(customer_id, api_key):
    url = f"http://api.nessieisreal.com/customers/{customer_id}/accounts?key={api_key}"
    
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"

def get_checking_account_number(api_key, customer_id):
    url = f"http://api.nessieisreal.com/customers/{customer_id}/accounts?key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        accounts = response.json()
        for account in accounts:
            if account['type'] == 'Checking':
                return account['_id']
        return "No checking account found"
    else:
        return "Error accessing API"
    
def get_billing_account_history(api_key, account_id):
    url = f"http://api.nessieisreal.com/accounts/{account_id}/bills?key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"billing_history.json", "w") as file:
            json.dump(response.json(), file)
        return "Billing history saved to file"
    else:
        return "Error accessing API"
        