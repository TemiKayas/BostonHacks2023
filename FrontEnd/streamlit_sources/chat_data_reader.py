import json
def read_and_format_financial_data(file_path='./output/billing_history.json'):
    try:
        with open(file_path, 'r') as file:
            billing_history = json.load(file)

        financial_info = 'Here is your recent financial data:\n'
        for item in billing_history:
            payment_date = item.get('payment_date', 'Unknown date')
            payment_amount = item.get('payment_amount', 0)
            nickname = item.get('nickname', 'Unknown category')
            financial_info += f"Date: {payment_date}, Amount: {payment_amount}, Category: {nickname}\n"
        return financial_info

    except FileNotFoundError:
        return "Error: Billing history file not found."
    except json.JSONDecodeError:
        return "Error: Problem decoding the billing history file."
