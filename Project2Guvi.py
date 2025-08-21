# import pandas as pd
# import numpy as np
# import streamlit as st


# st.title('Missing Data Cleaning App')
# # st.markdown('''
# #             #### this app helps you to find missing data and fill them using different methods''', True)

# st.text('this app helps you to find missing data and fill them using different methods')
# st.subheader('Upload your CSV file')

# data = st.file_uploader('Upload CSV', type='csv')

# if data is not None:
#     st.success('Dataset Uploaded Successfully')
#     try:
#         df = pd.read_csv(data, encoding="utf-8")
#     except UnicodeDecodeError:
#         try:
#             df = pd.read_csv(data, encoding="utf-8-sig")
#         except UnicodeDecodeError:
#             df = pd.read_csv(data, encoding="latin1")  # fallback


#     df_original = df.copy()
        
#     missing_columns = []
#     for i in df.columns:
#         if df[i].isnull().sum() >0:
#             missing_columns.append(i)
        
        
#     num_cols = df.select_dtypes(include=['number']).columns.to_list()
#     missing_num_cols = list(set(missing_columns).intersection(num_cols))
    
#     if st.checkbox('show missing values at each columns'):
        
#         if len(missing_num_cols) == 0:
#             st.info('your dataset has no missing numerical columns')
#         else:
#             st.table(df.isnull().sum())    

              
# # st.write('Columns with missing values:', missing_columns)        
            

# st.sidebar.header('choose a method to fill missing data')
# method = st.sidebar.selectbox('Select Method', ['choose','mean', 'median', 'mode'])


# if data is not None:
    
    
    
#     if method == 'mean':
#         df = df_original.copy()
#         for col in missing_num_cols:
#             df[col] = df[col].fillna(df[col].mean())
        
            
#     elif method == 'median':
#         df = df_original.copy()
#         for col in missing_num_cols:
#             df[col] = df[col].fillna(df[col].median())
        
        
#     elif method == 'mode':
#         df = df_original.copy()
#         for col in missing_num_cols:
#             df[col] = df[col].fillna(df[col].mode()[0])

            
        
#     st.write('Data after filling missing values using', method, 'method:')
#     st.dataframe(df)
    
#     if st.checkbox('show missing values at each columns after clean'):
    
#         st.table(df.isnull().sum())    

#     # Export cleaned dataset as CSV
#     csv = df.to_csv(index=False).encode('utf-8')

#     st.download_button(
#         label="📥 Download Cleaned CSV",
#         data=csv,
#         file_name='cleaned_dataset.csv',
#         mime='text/csv',
#     )

# else:
#     st.warning('Upload Your Dataset')


     


import pandas as pd
import numpy as np
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🧹 Missing Data Cleaning App",
    layout="wide"
)

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align: center;'>🧹 Missing Data Cleaning App</h1>", unsafe_allow_html=True)
st.markdown("✨ This app helps you find and clean missing data using different methods.")

# ---------------- FILE UPLOADER ----------------
st.subheader("📂 Upload your CSV file")
data = st.file_uploader("⬆️ Upload CSV", type="csv")

if data is not None:
    st.success("✅ Dataset Uploaded Successfully")

    # Safe reading with encodings
    try:
        df = pd.read_csv(data, encoding="utf-8")
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(data, encoding="utf-8-sig")
        except UnicodeDecodeError:
            df = pd.read_csv(data, encoding="latin1")  # fallback

    df_original = df.copy()

    # ---------------- MISSING VALUES ----------------
    missing_columns = [i for i in df.columns if df[i].isnull().sum() > 0]
    num_cols = df.select_dtypes(include=["number"]).columns.to_list()
    missing_num_cols = list(set(missing_columns).intersection(num_cols))

    with st.expander("🔍 Show Missing Values Summary"):
        if len(missing_num_cols) == 0:
            st.info("🎉 Your dataset has no missing numerical columns.")
        else:
            st.table(df.isnull().sum())

else:
    st.warning("⚠️ Please upload your dataset to begin.")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Cleaning Options")
method = st.sidebar.selectbox("Select Method", ["choose", "mean", "median", "mode"])

# ---------------- CLEANING PROCESS ----------------
if data is not None:
    if method == "mean":
        df = df_original.copy()
        for col in missing_num_cols:
            df[col] = df[col].fillna(df[col].mean())

    elif method == "median":
        df = df_original.copy()
        for col in missing_num_cols:
            df[col] = df[col].fillna(df[col].median())

    elif method == "mode":
        df = df_original.copy()
        for col in missing_num_cols:
            df[col] = df[col].fillna(df[col].mode()[0])

    if method != "choose":
        st.subheader(f"📊 Data after filling missing values using **{method}** method:")
        st.dataframe(df)

        with st.expander("📉 Missing Values After Cleaning"):
            st.table(df.isnull().sum())

        # Export cleaned dataset
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Cleaned CSV",
            data=csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv",
        )


    
