import streamlit as st

def main():
    
    st.set_page_config(page_title = 'FinOctopus *ink* Assitant', layout = 'wide')
    
    color = "#29abe2"
    background_color = "#f0f2f6"
    
    st.image("finoctopus.webp", use_column_width = True)
    
    st.header("Octopus Banker... ")
    # chat_placeholder =
    
    user_input = st.text_input("Aye Aye Sailor! How can I help you set sail on your financial journey today?")

if __name__ == "__main__":
    main()