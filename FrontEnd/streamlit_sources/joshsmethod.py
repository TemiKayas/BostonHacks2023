def parse():
    labels = {}
    billing_history = read_billing_history()

    for index, value in enumerate(billing_history):
        if value["nickname"] not in labels:
            labels[value["nickname"]] = value["payment_amount"]
        else:
            labels[value["nickname"]] = labels[value["nickname"]] + value["payment_amount"] 

    keys = list(labels.keys())
    values = list(labels.values())