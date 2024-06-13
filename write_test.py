# Define the Python script content
python_script = """
import streamlit as st

def main():
    st.title('My Streamlit App')
    st.write('Hello, Streamlit!')

if __name__ == '__main__':
    main()
"""

# Write the Python script to a file
with open('test.py', 'w') as file:
    file.write(python_script)

print('Python script written to test.py')
