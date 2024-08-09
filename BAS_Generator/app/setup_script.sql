-- This is the setup script that runs while installing a Snowflake Native App in a consumer account.
-- For more information on how to create setup file, visit https://docs.snowflake.com/en/developer-guide/native-apps/creating-setup-script

-- A general guideline to building this script looks like:
-- 1. Create application roles
CREATE APPLICATION ROLE IF NOT EXISTS app_public;

-- 2. Create a versioned schema to hold those UDFs/Stored Procedures
CREATE OR ALTER VERSIONED SCHEMA core;
GRANT USAGE ON SCHEMA core TO APPLICATION ROLE app_public;

-- 3. Create UDFs and Stored Procedures using the python code you wrote in src/module-add, as shown below.
CREATE OR REPLACE FUNCTION core.py_version()
  RETURNS STRING
  LANGUAGE PYTHON
  RUNTIME_VERSION=3.10
  PACKAGES=('snowflake-snowpark-python')
  IMPORTS=('/module-add/py_version.py')
  HANDLER='py_version.py_version_fn';

CREATE OR REPLACE FUNCTION core.generation(
      kunde_string STRING, 
      cloud_string STRING, 
      system_string STRING, 
      on_var BOOLEAN, 
      openai_api_key STRING, 
      url STRING, 
      port STRING
  )
  RETURNS STRING
  LANGUAGE PYTHON
  RUNTIME_VERSION=3.10
  PACKAGES=('snowflake-snowpark-python', 'pandas', 'langchain', 'langchain-community', 'langchain-core', 'openai')
  IMPORTS=('/module-add/generation.py')
  HANDLER='generation.generation_fn';

-- 4. Grant appropriate privileges over these objects to your application roles. 
GRANT USAGE ON FUNCTION core.py_version() TO APPLICATION ROLE app_public;
GRANT USAGE ON FUNCTION core.generation(STRING, STRING, STRING, BOOLEAN, STRING, STRING, STRING) TO APPLICATION ROLE app_public;

-- 5. Create a streamlit object using the code you wrote in you wrote in src/module-ui, as shown below. 
-- The `from` value is derived from the stage path described in snowflake.yml
CREATE OR REPLACE STREAMLIT core.ui
     FROM '/streamlit/'
     MAIN_FILE = 'ui.py';

-- 6. Grant appropriate privileges over these objects to your application roles. 
GRANT USAGE ON STREAMLIT core.ui TO APPLICATION ROLE app_public;

-- A detailed explanation can be found at https://docs.snowflake.com/en/developer-guide/native-apps/adding-streamlit 