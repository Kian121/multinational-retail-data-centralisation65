from data_extraction import DataExtractor
from data_cleaning import DataCleaning
from database_utils import DatabaseConnector

print("Initialising database connectors")
rds_connector = DatabaseConnector('/Users/kiansemnani/Documents/GitHub/multinational-retail-data-centralisation65/db_creds.yaml')
local_connector = DatabaseConnector('/Users/kiansemnani/Documents/GitHub/multinational-retail-data-centralisation65/pgdb_creds.yaml')

print("Initialising data extraction and cleaning modules")
data_extractor = DataExtractor()
data_cleaner = DataCleaning()

print("Extracting data from the source database")
raw_data = data_extractor.read_rds_table(rds_connector, "legacy_users")

print("Cleaning data...")
clean_data = data_cleaner.clean_user_data(raw_data)

print("Uploading cleaned data to the destination database")
local_connector.upload_to_db(clean_data, 'dim_users')
print("Data upload complete.")