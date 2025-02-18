from sqlalchemy import create_engine
import pandas as pd
import streamlit as st

engine = create_engine('mysql+pymysql://gastos:gastos@uuubuntu/gastos')
query = "select numero,nombre from yapero"
df = pd.read_sql(query, con=engine)

edited_df = st.data_editor(df, use_container_width=True, disabled=('id'), num_rows='dynamic')
edited_df.to_sql('yapero', con=engine, if_exists='replace', index=False)