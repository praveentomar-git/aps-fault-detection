# DUMP DATA INSIDE MONGODB

# IMPORT REQUIRED LIBRARIES
import pymongo
import pandas as pd
import json 

# PROVIDE THE MONGODB LOCAL HOST URL TO CONNECT PYTHON TO MONGODB
client=pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"rows and columns : {df.shape}")

# CONVERT DATAFRAME TO JSON SO THAT WE CAN DUMP THESE RECORD IN MONGODB
df.reset_index(drop=True, inplace=True)
json_record = list(json.loads(df.T.to_json()).values())
print (json_record[0])

# INSERT CONVERTED RECORD TO MONGODB
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
