##### `add.py`
##### BAS Anzeigen Generator
##### Please reach out to benjamin.gross1@adesso.de for any questions
#### Loading needed Python libraries
import sys
from snowflake.snowpark import Session
from snowflake.snowpark.functions import lit
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

# UDF
def add_fn(x: int, y: int) -> int:
    return x + y

# Stored Procedure
def py_version_fn() -> str:
    return sys.version
