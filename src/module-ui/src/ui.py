def run_streamlit():
    ##### `ui.py`
    ##### BAS Anzeigen Generator
    ##### Please reach out to benjamin.gross1@adesso.de for any questions
    #### Loading needed Python libraries
    import streamlit as st
    import pandas as pd
    import sys
    from snowflake.snowpark.functions import call_udf, col
    from snowflake.snowpark.context import get_active_session

    # Get the current credentials
    session = get_active_session()
    st.success("Datenbankverbindung erfolgreich hergestellt.")
    
    # Load data table
    @st.cache_data
    def load_data(table_name):
        # Read in data table
        st.write(f"Beispieldaten von `{table_name}`:")
        table = session.table(table_name)
    
        # Do some computation on it
        table = table.limit(100)
        
        # Collect the results. This will run the query and download the data
        table = table.collect()
        st.success("Daten erfolgreich gelesen.")
        return pd.DataFrame(table)
      
    def write_data(table_name):
        # Write data to table
        data = pd.DataFrame(
                            {
                              "PRAGRAPGH": ["1.0"],
                              "PARAGRAPH_TEXT": ["Die GWQ ServicePlus AG (GWQ) ist ein Dienstleister an der Schnittstelle zwischen Krankenkassen und den Erbringern medizinischer Versorgung."]
                            }
                           )
        session.write_pandas(data, table_name, auto_create_table=True)
        st.success("Daten erfolgreich geschrieben.")

    # Sidebar
    sidebar = st.sidebar
    with sidebar:
        st.markdown("Einstellungen")
        kunde = st.text_input("Anbieter:", value="GWQ ServicePlus AG")
        cloud = st.selectbox("Cloud:", ["AWS", "Azure", "Google Cloud"], index=2)
        on = st.toggle("OpenAI ChatGPT", True)
        system = st.text_input("System:", value = f"Du erstellst einzelne Absätze einer Anzeige beim Bundesamt für Soziale Sicherung über die Verarbeitung von Sozialdaten im Auftrag (AVV) nach § 80 Zehntes Sozialgesetzbuch (SGB X). Tausche <Variabel_Name> durch die entsprechenden Inhalte aus und gebe nur den Text aus und verzichte auf Phrasen wie z.B. 'Vielen Dank für die Informationen. Hier sind die angepassten Absätze für die Anzeige beim Bundesamt für Soziale Sicherung:'.")
        token = ""
        if on:
            st.markdown("OpenAI API Konfiguration")
            token = st.text_input("Token:", value="sk-")
        url = ""
        port = ""
        if not on:
            st.markdown("Lokaler Server Konfiguration")
            url = st.text_input("URL:", value="http://localhost")
            port = st.number_input("Port:", value=1234, min_value=1, max_value=65535)
        
    # Header
    st.title('❄️ BAS Anzeigen Generator')
    st.header('Generiere ein BAS Anzeigen Dokument')
    st.write(f"Python Version: {sys.version}")
    st.write(f"Streamlit Version: {st.__version__}")
    
    # Select and display data table
    table_name = "OPENAI_BENJAMINGROSS1.PUBLIC.ANZEIGE_PRE" #"OPENAI_DATABASE.PUBLIC.ANZEIGE_PRE"

    # Display data table
    with st.expander("Datenbankinhalt"):
        df = load_data(table_name)
        st.dataframe(df)

    # Generator
    data_frame = session.create_dataframe([[]]).select(call_udf('core.add', kunde, cloud, system, on, token, url, port).alias('RESULT'))
    output = data_frame.to_pandas()
    st.write(f"UDF Ausgabe: {output['RESULT'][0]}")

if __name__ == '__main__':
    run_streamlit()
