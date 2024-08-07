# This is where you can create python functions, which can further
# be used to create Snowpark UDFs and Stored Procedures in your setup_script.sql file.
import sys
from snowflake.snowpark import Session
from snowflake.snowpark.functions import lit
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

# UDF example:
def add_fn(x: int, y: int) -> int:
    return x + y

# Stored Procedure example:
def increment_by_one_fn(session: Session, x: int) -> int:
    df = session.create_dataframe([[]]).select((lit(1) + lit(x)).as_('RESULT'))
    return df.collect()[0]['RESULT']
  
def py_version_fn() -> str:
    return sys.version
