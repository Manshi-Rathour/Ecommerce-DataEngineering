import pandas as pd
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

# Load the product_category CSV file into a pandas DataFrame
try:
    product_category_df = pd.read_csv("data/product_category_name_translation.csv")
except FileNotFoundError:
    print("Error: 'product_category_name_translation.csv' not found.")
    exit()  # Exit the script if the file is not found


hostname = os.getenv("MongoDB_HOSTNAME")
database = os.getenv("MongoDB_DATABASE")
port = os.getenv("MongoDB_PORT")
username = os.getenv("MongoDB_USERNAME")
password = os.getenv("MongoDB_PASSWORD")

uri = "mongodb://" + username + ":" + password + "@" + hostname + ":" + port + "/" + database

try:
    # Establish a connection to MongoDB
    client = MongoClient(uri)
    db = client[database]

    collection = db["product_categories"]

    # Convert the DataFrame to a list of dictionaries for insertion into MongoDB
    data_to_insert = product_category_df.to_dict(orient="records")

    # Insert the data into the collection
    collection.insert_many(data_to_insert)

    print("Data uploaded to MongoDB successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the MongoDB connection
    if client:
        client.close()