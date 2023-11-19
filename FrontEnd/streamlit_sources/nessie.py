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


def create_bill(api_key, account_id, status, payee, nickname, payment_date, payment_amount):
    url = f"http://api.nessieisreal.com/accounts/{account_id}/bills?key={api_key}"
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        "status": status,
        "nickname": nickname,
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
        with open(f"output/billing_history.json", "w") as file:
            json.dump(response.json(), file)
        return "Billing history saved to file"
    else:
        return "Error accessing API"
        
def delete_all_data(api_key):
    accounts_url = f"http://api.nessieisreal.com/accounts?key={api_key}"
    accounts_response = requests.get(accounts_url)
    if accounts_response.status_code == 200:
        accounts = accounts_response.json()
        for account in accounts:
            bills_url = f"http://api.nessieisreal.com/accounts/{account['_id']}/bills?key={api_key}"
            bills_response = requests.get(bills_url)
            if bills_response.status_code == 200:
                bills = bills_response.json()
                for bill in bills:
                    delete_bill_url = f"http://api.nessieisreal.com/accounts/{account['_id']}/bills/{bill['_id']}?key={api_key}"
                    requests.delete(delete_bill_url)

    if accounts_response.status_code == 200:
        for account in accounts:
            delete_account_url = f"http://api.nessieisreal.com/accounts/{account['_id']}?key={api_key}"
            requests.delete(delete_account_url)

    customers_url = f"http://api.nessieisreal.com/customers?key={api_key}"
    customers_response = requests.get(customers_url)
    if customers_response.status_code == 200:
        customers = customers_response.json()
        for customer in customers:
            delete_customer_url = f"http://api.nessieisreal.com/customers/{customer['_id']}?key={api_key}"
            requests.delete(delete_customer_url)

    return "All data deleted"


def main(api_key):
    #create_customer(api_key, 'Dwayne \"The Rock\"', 'Johnson', '99', 'Main St', 'Los Angeles', 'CA', '90210')
    #create_checking_account(api_key, '6559494d9683f20dd51889bc', 'The Rock\'s Checking Account', 0, 1000000)
    #create_bill(api_key, get_checking_account_number(api_key, '6559494d9683f20dd51889bc'), 'completed', 'Louis Vuitton', 'clothing', '11/19/2023', 20000)
    get_billing_account_history(api_key, get_checking_account_number(api_key, '6559494d9683f20dd51889bc'))
    
if __name__ == "__main__":
    main(api_key)