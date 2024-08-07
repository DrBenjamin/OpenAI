def run_streamlit():
##### `ui.py`
##### BAS Anzeigen Generator
##### Please reach out to benjamin.gross1@adesso.de for any questions
#### Loading needed Python libraries
    import streamlit as st
    import pandas as pd
    from snowflake.snowpark.functions import call_udf, col
    from snowflake.snowpark import Session

    # Get the current credentials
    session = Session.builder.getOrCreate()
    
    # Header
    st.title('❄️ BAS Anzeigen Generator')
    st.header('Generiere ein BAS Anzeigen Dokument')
    version = session.call('core.py_version')
    st.write(f"Python Version: {version}")
    st.write(f"Streamlit Version: {st.__version__}")

if __name__ == '__main__':
    run_streamlit()
