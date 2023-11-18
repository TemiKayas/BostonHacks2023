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

def create_bill(account_id, amount, payee):
    url = f"{BASE_URL}/accounts/{account_id}/bills?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "status": "pending",
        "payee": payee

    }
    response = requests.post(url, data=json.dumps(payload), header=headers)

    if response.status_code == 201:
        return response.json()
    else:
        return response.text

def get_bills(account_id):
    url = f"{BASE_URL}/accounts/{account_id}/bills?key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return response.text    


def deposit(account_id, amount):
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

def main():
    create_account(123, 'checking', 'Henry Van Hove', 0, 1000)
    #create_bill(123, 50, 'dominoes pizza')
    get_bills(123)

if __name__ == "__main__":
    main()