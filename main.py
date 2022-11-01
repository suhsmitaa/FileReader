import streamlit as st
import pandas as pd
import js2py as js

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



global df
def main():

    uploaded_file = st.file_uploader(label="Upload your CSV or Xls file",
                    type=['csv','xls'])
#uploading file
    if uploaded_file is not None:
        try:
            df=pd.read_csv(uploaded_file)
            if df['Phone'].isnull().values.any():
                st.write('Mobile Column is null')
            else:
                st.write(df)
                st.download_button(label="Download file", data=df.to_csv(), mime='text/csv')

        except Exception as e:
            print(e)
            df=pd.read_excel(uploaded_file)

            if df['Phone'].isnull().values.any():
                st.write('Mobile Column is null')
            else:
                st.write(df)
                st.download_button(label="Download file", data=df.to_csv(), mime='text/csv')




if __name__ == '__main__':
    main()
    #download()

js