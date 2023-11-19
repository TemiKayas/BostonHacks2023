import pandas as pd
import json

def read_financial_data(account_number, file_path='./output/billing_history.json'):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Filter by account number
        # Ensure both the account number from user and from JSON are of the same type (str)
        df = df[df['account_id'] == str(account_number)]

        # Check if there is data after filtering
        if df.empty:
            return pd.DataFrame(columns=['payment_date', 'payment_amount'])

        # Convert 'payment_date' to datetime and sort
        df['payment_date'] = pd.to_datetime(df['payment_date'])
        df.sort_values('payment_date', inplace=True)

        return df[['payment_date', 'payment_amount']]
    except FileNotFoundError:
        print(f"File not found: {file_path}")  # Or use a logging mechanism
        return pd.DataFrame(columns=['payment_date', 'payment_amount'])
    except Exception as e:
        print(f"Error reading financial data: {e}")  # Or use a logging mechanism
        return pd.DataFrame(columns=['payment_date', 'payment_amount'])
