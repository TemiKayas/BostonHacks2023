import get_bills from nessie
import pandas as pd
import json
import matplotlib.pyplot as plt

# Sample JSON data
# You can replace this with your own JSON source


# Convert JSON to DataFrame
account_id = xyz
data = pd.json_normalize(json.loads(get_bills(account_id)))

# Streamlit app
st.title('JSON Data Graph')

# Display the DataFrame
st.write(data)

# Plotting
fig, ax = plt.subplots()
ax.bar(data['category'], data['value'])
ax.set_xlabel('Category')
ax.set_ylabel('Value')
st.pyplot(fig)