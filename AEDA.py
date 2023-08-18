import streamlit as st
import pandas as pd
import numpy as np
#to open web
#  py -m streamlit run c:/Users/HP/Desktop/AEDA.py

#add title
st.title("Automated EDA")
st.subheader("Enter File ")

#########upload files and get data frame##############
data_file = st.file_uploader("upload file", type=['csv','xlsx','xls','sql'], label_visibility="visible")
if data_file is not None:


    st.success("file is succesfully uploaded")
    file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
    st.write(file_details)
    if file_details["FileType"] == "text/csv":
        df = pd.read_csv(data_file)
        #df.reset_index(drop=True,inplace=True)
        st.write("dataframe before preprocessing process")
        st.write(df)
        st.write(df.shape)
    elif file_details["FileType"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or file_details["FileType"] == "application/vnd.ms-excel":
        df = pd.read_excel(data_file)
        #df.reset_index(drop=True,inplace=True)
        st.write(df)
        st.write(df.shape)
    elif file_details["FileType"] == "application/octet-stream":
        pass


#############data pre-processing###################

    #remove any nan columns
    df.dropna(how='all', axis=1, inplace=True)
    df_type = df.dtypes
    st.write(df_type)
    for col in df.columns:
        st.write(col)
        if df_type[col] == 'int64':
            st.write(df_type[col])
            st.write(df[col].isna().sum())
            if df[col].isna().sum() > 0:
                st.warning("ther is {} of null values".format(df[col].isna().sum()))
                df = df[col].fillna(df[col].mean())
        elif df_type[col] == 'object':
            st.write(df_type[col])
            st.write(df[col].isna().sum())
            if df[col].isna().sum() > 0:
                st.warning("ther is {} of null values".format(df[col].isna().sum()))

    st.write("dataframe after preprocessing process")
    st.write(df)
    st.write(df.shape)



        


