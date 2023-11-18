import requests
import json

API_KEY = 'c4339d9d4f473684a342b04bcbb2ccf1'
BASE_URL = 'http://api.nessieisreal.com'

def create_account(user_id, account_type, fullname, rewards, balance):
    url = f"{BASE_URL}/customers/{user_id}/accounts?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "type": account_type,
        "nickname": fullname,
        "rewards": rewards,
        "balance": balance
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 201:
        return response.json()
    else:
        return response.text

def create_bill(account_id, amount, payee, payment_date, recurring_date, expense_type):
    url = f"{BASE_URL}/accounts/{account_id}/bills?key={API_KEY}"

    headers = {'Content-Type': 'application/json'}

    payload = {
        "status": "pending",
        "payee": payee,
        "nickname": expense_type,
        "payment_date": payment_date,
        "recurring_date": recurring_date,
        "payment_amount": amount
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 201:
        return response.json()  
    else:
        return response.text 

def get_bills_from_account(account_id):
    url = f"{BASE_URL}/accounts/{account_id}/bills?key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return response.text    


def deposit_to_account(account_id, amount):
    url = f"{BASE_URL}/accounts/{account_id}/deposits?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "medium": "balance", 
        "transaction_date": "2023-11-18",  
        "status": "pending",
        "amount": amount,
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 201:
        return response.json()
    else:
        return response.text


def get_billing_history_of_all_users():
    customers_response = requests.get(f"{BASE_URL}/customers?key={API_KEY}")
    if customers_response.status_code != 200:
        return 'error'

    customers = customers_response.json()
    all_bills = {}

    for customer in customers:
        customer_id = customer['_id']
        accounts_response = requests.get(f"{BASE_URL}/customers/{customer_id}/accounts?key={API_KEY}")
        if accounts_response.status_code == 200:
            accounts = accounts_response.json()
            for account in accounts:
                account_id = account['_id']
                bills_response = requests.get(f"{BASE_URL}/accounts/{account_id}/bills?key={API_KEY}")
                if bills_response.status_code == 200:
                    bills = bills_response.json()
                    all_bills[account_id] = bills

    return all_bills

def main():
    create_account(1, 'checking', 'Henry Van Hove', 0, 1000)
    create_account(2, 'checking', 'John Doe', 0, 1000)
    create_account(3, 'checking', 'Anthony Hopkins', 0, 1000)
    create_account(4, 'checking', 'Artemios Kayas', 0, 1000)
    create_account(5, 'checking', 'Evan', 0, 1000)
    create_account(6, 'checking', 'Brad Pitt', 0, 1000)
    create_account(7, 'checking', 'Joe Biden', 0, 1000)
    create_account(8, 'checking', 'George Santos', 0, 1000)
    create_account(9, 'checking', 'The Rock', 0, 1000)
    create_account(10, 'checking', 'Sam Altman', 0, 1000)
    create_bill(1, 100, 'Dominoes Pizza', 11-18-2023, 0, 'food')
    

if __name__ == "__main__":
    main()