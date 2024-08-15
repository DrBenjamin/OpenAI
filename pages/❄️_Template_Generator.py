##### `❄️_Template_Generator.py`
##### BAS Anzeigen Generator
##### Please reach out to benjamin.gross1@adesso.de for any questions
#### Loading needed Python libraries
import streamlit as st
import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
from snowflake.snowpark import Session
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
    
# Establish Snowflake session
@st.cache_resource
def create_session():
    return Session.builder.configs(st.secrets.snowflake).create()

session = create_session()
st.success("Datenbankverbindung erfolgreich hergestellt.")

# Write data table
def write_data(data, table_name, database, schema):
    # Write data to table
    session.write_pandas(data, table_name=table_name, database=database, schema=schema, overwrite=True)
    st.success("Daten erfolgreich geschrieben.")

# Load data table
@st.cache_data
def load_data(table_name):
    # Read in data table
    table = session.table(table_name)

    # Collect the results. This will run the query and download the data
    table = table.collect()
    return pd.DataFrame(table)

# Web Scraper
def web_scraper(url):
    info_page = requests.get(url)
    info_soup = BeautifulSoup(info_page.content, 'html.parser')
    info = info_soup.get_text()
    info = info.replace('\n', ' ')
    return info

# Title
st.title('❄️ Template Generator')
st.write(f"Streamlit Version: {st.__version__}")
st.write(f"Python Version: {sys.version}")

# Display data table
with st.expander("Datenbankinhalt"):
    df = load_data('OPENAI_DATABASE.PUBLIC.ANZEIGE_PRE')
    st.dataframe(df)
    paragraphs = load_data('OPENAI_DATABASE.PUBLIC.ANZEIGE_PARAGRAPHS')
    st.dataframe(paragraphs)

# Sidebar
sidebar = st.sidebar
with sidebar:
    kunde = st.text_input("Kunde:", value="GWQ ServicePlus AG")
    web = st.toggle("Webscraper", True)
    kunde_url = st.text_input("Kunden-Webseite (z.B. `Über uns`):", value="https://www.gwq-serviceplus.de/ueber-uns")
    if web:
        kunde_info = web_scraper(kunde_url)
    cloud = st.selectbox("Cloud:", ["AWS", "Azure", "Google Cloud"], index=2)
    on = st.toggle("OpenAI ChatGPT", True)
    system = st.text_input("System:", value = f"Du erstellst einzelne Absätze einer Anzeige beim Bundesamt für Soziale Sicherung über die Verarbeitung von Sozialdaten im Auftrag (AVV) nach § 80 Zehntes Sozialgesetzbuch (SGB X). Tausche die Platzhalter (z.B. <Kunde>) durch die entsprechenden Inhalte aus und gebe nur den verbesserten Text in einer sachlichen und formellen Form aus und verzichte auf Phrasen wie z.B. 'Vielen Dank für die Informationen. Hier sind die angepassten Absätze für die Anzeige beim Bundesamt für Soziale Sicherung:'.")
    if not on:
      st.markdown("Local Server Configuration")
      url = st.text_input("URL:", value="http://localhost")
      port = st.number_input("Port:", value=1234, min_value=1, max_value=65535)

with st.form("form"):
    st.title("BAS Anzeige")
    st.header("Konfiguration")
    base_informnation = st.container(border=True)
    base_informnation.write("Grundsätzliche Informationen")
    base_informnation_0_0 = base_informnation.text_input("Name des Auftragsverarbeiters?", key="base_informnation_0_0")
    options_1 = st.container(border=True)
    options_1.header("Sozialdaten")
    with options_1.container(border=True):
        st.subheader("Details zu den Sozialdaten")
        options_1_0a = st.toggle("Sollen Sozialdaten verarbeitet werden?", False)
        options_1_0b = st.toggle("Sollen diese persistent gespeichert werden?", False)
        options_1_1 = st.text_input("Welche Art von Sozialdaten?", key="option_1_1")
        options_1_2 = st.text_input("Welcher Kreis von betroffenen Personen?", key="option_1_2")
        options_1_3 = st.text_input("Welcher Zweck und welche konkrete Aufgabe der Datenverarbeitung besteht?", key="option_1_3")
    options_2 = st.container(border=True)
    options_2.header("Auftragsverhältnisse")
    with options_2.container(border=True):
        st.subheader("Unterauftrags-Verhältnisse")
        options_2_0 = st.toggle("Bestehen Unterauftrags-Verhältnisse?", False)
    options_3 = st.container(border=True)
    options_3.header("Verarbeitung")
    with options_3.container(border=True):
        st.subheader("Intranet")
        options_3_0 = st.toggle("Sind die Daten oder Dienste über das Intranet erreichbar?", False)
        options_3_1 = st.text_input("Daten", key="option_3_1")
        options_3_2 = st.text_input("Dienste", key="option_3_2")
    with options_3.container(border=True):
        st.subheader("Internet")
        options_3_3 = st.toggle("Sind die Daten oder Dienste über das Internet erreichbar?", False)
        options_3_4 = st.text_input("Daten", key="option_3_4")
        options_3_5 = st.text_input("Dienste", key="option_3_5")
    with options_3.container(border=True):
        st.subheader("Anbieterzugang")
        options_3_6 = st.toggle("Muss beim Anbieter ein Zugang beantragt werden?", False)
    with options_3.container(border=True):
        st.subheader("Webzugang")
        options_3_7 = st.toggle("Sind die Daten oder Dienste mit einem Webbrowser erreichbar?", False)
        options_3_8 = st.text_input("Daten", key="option_3_8")
        options_3_9 = st.text_input("Dienste", key="option_3_9")
    with options_3.container(border=True):
        st.subheader("App-Zugang")
        options_3_10 = st.toggle("Sind die Daten oder Dienste mit einer App für Smartphones, Tablets oder PCs / Mac erreichbar?", False)
        options_3_11 = st.toggle("Ist diese Lösung von BITMARK bereitgestellt?", False)
        options_3_12 = st.toggle("Handelt es sich um einen Speicherplatz für Daten, der bereitgestellt wird?", False)
    with options_3.container(border=True):
        st.subheader("KI-Tools und -Services")
        options_3_13 = st.toggle("Werden KI-Tools oder -Services verwendet?", False)
    with options_3.container(border=True):
        st.subheader("Risiko- und Compliance-Bewertung")
        options_3_14 = st.toggle("Werden Services zur Risiko- und Compliance-Bewertung eingesetzt?", False)
    with options_3.container(border=True):
        st.subheader("Herausgabe der Daten an US-Behörden")
        options_3_15 = st.toggle("Kann der Anbieter Daten unverschlüsselt an US-amrikanische Behörden übergeben?", False)
    with options_3.container(border=True):
        st.subheader("Datenverarbeitung in der EU")
        options_3_16 = st.toggle(f"Werden alle {cloud}-SaaS-Dienste speziell für die Einhaltung von § 80 Abs. 2 SGB X konfiguriert, um eine Datenverarbeitung innerhalb der EU sicherzustellen?", False)
    with options_3.container(border=True):
        st.subheader("Machine Learning")
        options_3_17 = st.toggle("Werden ML-Modelle zur Datenanalyse eingesetzt?", False)
        options_3_18 = st.toggle("Wird sichergestellt, dass ML-Modelle in Infrastruktur, Tools und Workflows ausschließlich in der EU gehostet und genutzt werden?", False)
        options_3_19 = st.toggle("Unterstützt der Anbieter die Erstellung von sicheren und konformen Machine Learning (ML)-Modellen im Sozial- und Gesundheitswesen?", False)
    with options_3.container(border=True):
        st.subheader("Landing Zone")
        options_3_20 = st.toggle("Ist das Landing Zone Konzept Bestandteil der Cloud-Architektur?", False)
        if cloud == 'AWS':
            options_3_21 = st.toggle("Folgt die Architektur dem AWS Well-Architected Framework?", False)
        if cloud == 'Azure':
            options_3_22 = st.toggle("Folgt die Architektur dem Azure Well-Architected Framework?", False)
        if cloud == 'Google Cloud':
            options_3_23 = st.toggle("Folgt die Architektur dem Google Cloud Architecture Framework?", False)
        options_3_24 = st.text_input("Wie wurde die Landing Zone aufgebaut?", key='options_3_24')
        options_3_25 = st.toggle("Wurde dafür ein Tool genutzt?", False)
        options_3_26 = st.text_input("Wie werden Identitäten und Zugriffsrechte innerhalb der Landing Zone verwaltet?", key='options_3_26')
        options_3_27 = st.toggle("Werden Maßnahmen zur Netzwerksicherheit in der Architektur der Landing Zone umgesetzt?", False)
    with options_3.container(border=True):
        st.subheader("Rechtliche Anforderungen")
        options_3_28 = st.text_input(f"Welche Maßnahmen ergreift {cloud}, um sicherzustellen, dass die Datenverarbeitung und -speicherung den rechtlichen Anforderungen entspricht, auch im Hinblick auf US-amerikanische Auskunftsrechte?", key='option_3_28')
        options_3_29 = st.text_input(f"Wie adressiert {cloud} die Anforderungen an die Datenverarbeitung von SaaS-Diensten in Drittländern, insbesondere in Bezug auf das Schrems-II-Urteil und § 80 Abs. 2 SGB X?", key='options_3_29')
        options_3_30 = st.text_input(f"Wie können GKV-Träger sicherstellen, dass die Nutzung von {cloud}-SaaS-Diensten die Datenverarbeitung auf die EU beschränkt, in Übereinstimmung mit § 80 Abs. 2 SGB X?", key='options_3_30')
        options_3_31 = st.text_input("Wie wird die Übermittlung von Daten in Drittländer gehandhabt, insbesondere im Hinblick auf das Schrems-II-Urteil?", key='options_3_31')
        options_3_32 = st.text_input(f"Wie schützt {cloud} Kundendaten vor Zugriffen durch US-amerikanische Behörden?", key='options_3_32')
        options_3_33 = st.text_input("Wie unterstützt {cloud} die Einhaltung des Bundesdatenschutzgesetzes und der DSGVO?", key='options_3_33')
        options_3_34 = st.text_input(f"Wie gewährleistet {cloud} die Einhaltung der DSGVO und des BDSG für GKV-Daten?", key='options_3_34')
        options_3_35 = st.text_input(f"Wie gewährleistet {cloud} die Einhaltung von § 80 SGB X und DSGVO beim Umgang mit Sozialdaten?", key='options_3_35')
    with options_3.container(border=True):
        st.subheader("Compliance Anforderungen")
        options_3_36 = st.text_input(f"Wie können GKV-Träger {cloud}-Tools nutzen, um Compliance-Anforderungen zu überwachen und zu erfüllen?", key='options_3_36')
    with options_3.container(border=True):
        st.subheader("Backup-Strategien")
        options_3_37 = st.text_input(f"Welche {cloud}-Dienste nutzt die GKV im Bereich Hochverfügbarkeit?", key='options_3_37')
        options_3_38 = st.text_input(f"Welche {cloud}-Dienste nutzt die GKV im Bereich Disaster Recovery?", key='options_3_38')
    with options_3.container(border=True):
        st.subheader("Cloud Agnostik")
        options_3_39 = st.text_input("Welche Mechanismen bietet der Anbieter hinsichtlich eines Umzugs in eine andere Cloud (Cloud-Switching)?", key='options_3_39')
    with options_3.container(border=True):
        st.subheader("Faire Datennutzung")
        options_3_40 = st.toggle("Gibt es bereits Mechanismen zur Gewährleistung von European Data Act?", False)
        options_3_41 = st.text_input(f"Wie nutzt die GKV {cloud}-Dienste, um eine feingranulare Zugriffssteuerung und Governance zu implementieren?", key='options_3_41')
    with options_3.container(border=True):
        st.subheader("IT-Sicherheit")
        st.write("Sicherheit")
        options_3_42 = st.text_input(f"Welche Maßnahmen ergreift {cloud} zum Schutz vor internen und externen Angriffen?", key='options_3_42')
        options_3_43 = st.text_input("Wie können GKV-Träger die Anforderungen an die physische Sicherheit und den Zugangsschutz in Rechenzentren überprüfen?", key='options_3_43')
        options_3_44 = st.text_input("Wie plant ihre Organisation, dies zu tun?", key='options_3_44')
        options_3_45 = st.text_input(f"Ist für die {cloud}-Lösung ein C5-Testat ausgestellt?", key="options_3_45")
        st.write("Verschlüsselung")
        options_3_46 = st.text_input(f"Welche Maßnahmen trifft {cloud}, um Daten vor unbefugtem Zugriff durch Dritte, einschließlich {cloud} selbst, zu schützen?", key='options_3_46')
        options_3_47 = st.text_input(f"Wie unterstützt {cloud} die Verschlüsselung von Daten at-rest, in-transit und in-use?", key='options_3_47')
        options_3_48 = st.text_input(f"Wie unterstützt {cloud} die Verschlüsselung von Daten in-transit?", key='options_3_48')
        options_3_49 = st.text_input(f"Welche Bedeutung hat {cloud}-Verschlüsselungs-Dienst für die Verschlüsselung in-use?", key="options_3_49")
        options_3_50 = st.selectbox(label="Verschlüsselungs-Dienst", options=['AWS Nitro', 'Azure Managed HSM', 'Google Cloud KMS'])

        options_3_51 = st.text_input(f"Welche Mechanismen stellt die {cloud}-Lösung zur Verschlüsselung von Patientendaten zur Verfügung? Wie werden Schlüssel gemanaged?", key="options_3_51")

    st.header("Template")
    template = st.container(border=True)
    with template.container(border=True):
        st.subheader("Optionen")
        st.write("Bitte wähle die gewünschten Optionen aus 🔘")
        st.selectbox("Format", options=["Word"])
    with template.container(border=True):
        st.subheader("Absätze")
        st.write("Bitte wähle die Absätze aus 📒")
        paragraph_list = df["PARAGRAPH"].tolist()
        paragraph_title_list = df["PARAGRAPH_TITLE"].tolist()
        combined_list = [f"{p} - {t}" for p, t in zip(paragraph_list, paragraph_title_list)]    
        st.multiselect("Absätze", options=combined_list, default=combined_list)
    submitted = st.form_submit_button("Template generieren")

if submitted:
    # Set up memory
    msgs = StreamlitChatMessageHistory(key="langchain_messages")
    if len(msgs.messages) == 0:
        msgs.add_ai_message(f"""Ich schreibe den Text in einer sachlichen und formellen
                                Form um und ersetze <Kunde> mit {kunde}, 
                                <Cloud-Anbieter> mit {cloud}.""")

    view_messages = st.expander("Zeige mir die Paragraphen an")

    # Set up the LangChain, passing in Message History
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", f"{system}"),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )

    # Setting the LLM
    if on:
        chain = prompt | ChatOpenAI(
            model="gpt-4o-mini",
            api_key=st.secrets["openai"]["key"]
        )
    else:
        server_url = f"{url}:{str(port)}/v1"
        chain = prompt | ChatOpenAI(
            base_url=server_url,
            model="llama-3-8b-chat-doctor-Q4_K_M_v2",
            temperature=0.5,
            max_tokens=4000,
            api_key="lm-studio"
      )

    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: msgs,
        input_messages_key="question",
        history_messages_key="history",
    )

    # Render current messages from StreamlitChatMessageHistory
    for msg in msgs.messages:
        st.chat_message(msg.type).write(msg.content)

    # If user inputs a new prompt, generate and draw a new response
    for text in df["PARAGRAPH_TEXT"]:
        if '<Kundeninfo>' in text and web:
            prompt = text.replace('<Kunde>', str(kunde)).replace('<Cloud-Anbieter>', str(cloud)).replace('<Kundeninfo>', str(kunde_info))
        else:
            prompt = text.replace('<Kunde>', str(kunde)).replace('<Cloud-Anbieter>', str(cloud))
        if '<§' or '<Art.' in prompt:
            for paragraph in paragraphs["PARAGRAPH"]:
                # Checking for matching paragraph
                if paragraph in prompt:
                    prompt = prompt.replace(f"<{paragraph}>", paragraphs[paragraphs['PARAGRAPH'] == paragraph].drop(columns=paragraphs.columns[-1]).to_string(index=False, header=False))
                    paragraph_info = web_scraper(paragraphs[paragraphs['PARAGRAPH'] == paragraph].drop(columns=paragraphs.columns[:2]).to_string(index=False, header=False))
                    paragraph_info = paragraph_info.replace('\n', ' ')
                    prompt += paragraph_info
        st.chat_message("human").write(prompt)
        
        # Note: new messages are saved to history automatically by Langchain during run
        config = {"configurable": {"session_id": "any"}}
        response = chain_with_history.invoke({"question": prompt}, config)
        st.chat_message("ai").write(response.content)

    # Draw the messages at the end, so newly generated ones show up immediately
    with view_messages:
        """
        Message History initialized with:
        ```python
        msgs = StreamlitChatMessageHistory(key="langchain_messages")
        ```

        Contents of `st.session_state.langchain_messages`:
        """
        view_messages.json(st.session_state.langchain_messages)

    # Convert to dataframe
    messages = st.session_state.langchain_messages
    anzeige_temp = pd.DataFrame(columns=['PARAGRAPH', 'PARAGRAPH_TEXT'])
    counter = -1
    paragraph = -1
    for index, message in enumerate(messages):
        for key, value in message:
            if key == "content":
                counter += 1
                if counter > 0 and counter % 2 == 0:
                    paragraph += 1
                    anzeige_temp = anzeige_temp._append(pd.DataFrame([{'PARAGRAPH': df['PARAGRAPH'][paragraph], 'PARAGRAPH_TEXT': value}]), ignore_index=True)

    st.dataframe(anzeige_temp)
    write_data(anzeige_temp, table_name='ANZEIGE_TEMP', database='OPENAI_DATABASE', schema='PUBLIC')
    with st.expander("Datenbankinhalt", expanded=False):
        df = load_data('OPENAI_DATABASE.PUBLIC.ANZEIGE_TEMP')
        st.dataframe(df)
