def run_streamlit():
    ##### `ui.py`
    ##### BAS Anzeigen Generator
    ##### Please reach out to benjamin.gross1@adesso.de for any questions
    #### Loading needed Python libraries
    import streamlit as st
    import pandas as pd
    from _snowflake import get_username_password
    from _snowflake import get_generic_secret_string
    from snowflake.snowpark.functions import call_udf, col
    from snowflake.snowpark.context import get_active_session

    # Get the current credentials
    session = get_active_session()
        
    # Header
    st.title('❄️ BAS Anzeigen Generator')
    st.header('Generiere ein BAS Anzeigen Dokument')
    version = session.call('core.py_version')
    st.write(f"Python Version: {version}")
    st.write(f"Streamlit Version: {st.__version__}")
    try:
        openai_key = get_generic_secret_string('OPENAI_KEY')
        st.write(f"OpenAI API Token: {openai_key}")
    except:
        st.write("OpenAI API Token: Not Found")
    try:
        openai_key = get_username_password('OPENAI_KEY')
        st.write(f"OpenAI API Token: {openai_key}")
    except:
        st.write("OpenAI API Token: Not Found")

    # Sidebar
    sidebar = st.sidebar
    with sidebar:
      kunde = st.text_input("Anbieter:", value="GWQ ServicePlus AG")
      cloud = st.selectbox("Cloud:", ["AWS", "Azure", "Google Cloud"], index=2)
      on = st.toggle("OpenAI ChatGPT", True)
      system = st.text_input("System:", value = f"Du erstellst einzelne Absätze einer Anzeige beim Bundesamt für Soziale Sicherung über die Verarbeitung von Sozialdaten im Auftrag (AVV) nach § 80 Zehntes Sozialgesetzbuch (SGB X). Tausche <Variabel_Name> durch die entsprechenden Inhalte aus und gebe nur den Text aus und verzichte auf Phrasen wie z.B. 'Vielen Dank für die Informationen. Hier sind die angepassten Absätze für die Anzeige beim Bundesamt für Soziale Sicherung:'.")
      if not on:
        st.markdown("Local Server Configuration")
        url = st.text_input("URL:", value="http://localhost")
        port = st.number_input("Port:", value=1234, min_value=1, max_value=65535)

if __name__ == '__main__':
    run_streamlit()
