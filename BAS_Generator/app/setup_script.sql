-- This is the setup script that runs while installing a Snowflake Native App in a consumer account.
-- For more information on how to create setup file, visit https://docs.snowflake.com/en/developer-guide/native-apps/creating-setup-script

-- A general guideline to building this script looks like:
-- 1. Create application roles
CREATE APPLICATION ROLE IF NOT EXISTS app_public;

-- 2. Create a versioned schema to hold those UDFs/Stored Procedures
CREATE OR ALTER VERSIONED SCHEMA core;
GRANT USAGE ON SCHEMA core TO APPLICATION ROLE app_public;

-- 3. Create UDFs and Stored Procedures using the python code you wrote in src/module-add, as shown below.
CREATE OR REPLACE FUNCTION core.add(x NUMBER, y NUMBER)
  RETURNS NUMBER
  LANGUAGE PYTHON
  RUNTIME_VERSION=3.10
  PACKAGES=('snowflake-snowpark-python', 'pandas', 'langchain', 'langchain-community', 'langchain-core', 'openai')
  IMPORTS=('/module-add/add.py')
  HANDLER='add.add_fn';

  CREATE OR REPLACE PROCEDURE core.py_version()
  RETURNS STRING
  LANGUAGE PYTHON
  RUNTIME_VERSION=3.10
  PACKAGES=('snowflake-snowpark-python', 'pandas', 'langchain', 'langchain-community', 'langchain-core', 'openai')
  IMPORTS=('/module-add/add.py')
  HANDLER='add.py_version_proc';

  CREATE OR REPLACE FUNCTION get_secret_username_password()
  RETURNS STRING
  LANGUAGE PYTHON
  RUNTIME_VERSION = 3.8
  HANDLER = 'get_secret_username_password'
  EXTERNAL_ACCESS_INTEGRATIONS = (external_access_integration)
  SECRETS = ('OPENAI_KEY' = credentials_secret )
  AS
  $$
  import _snowflake

  def get_secret_username_password():
    username_password_object = _snowflake.get_username_password('OPENAI_KEY');

    username_password_dictionary = {}
    username_password_dictionary["Username"] = username_password_object.username
    username_password_dictionary["Password"] = username_password_object.password

    return username_password_dictionary
  $$;

-- 4. Grant appropriate privileges over these objects to your application roles. 
GRANT USAGE ON FUNCTION core.add(NUMBER, NUMBER) TO APPLICATION ROLE app_public;
GRANT USAGE ON FUNCTION get_secret_type() TO APPLICATION ROLE app_public;
GRANT USAGE ON PROCEDURE core.py_version() TO APPLICATION ROLE app_public;

-- 5. Create a streamlit object using the code you wrote in you wrote in src/module-ui, as shown below. 
-- The `from` value is derived from the stage path described in snowflake.yml
CREATE STREAMLIT core.ui
     FROM '/streamlit/'
     MAIN_FILE = 'ui.py';

-- 6. Grant appropriate privileges over these objects to your application roles. 
GRANT USAGE ON STREAMLIT core.ui TO APPLICATION ROLE app_public;

-- A detailed explanation can be found at https://docs.snowflake.com/en/developer-guide/native-apps/adding-streamlit 