import streamlit as st

def hello():
    return " Primeniro deploy com sucesso"
def main():
    st.write(hello())

if __name__ == "__main__":
    main()