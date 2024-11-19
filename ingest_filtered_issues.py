import os
import json
from astrapy import DataAPIClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# Initialize Astra DB Collection
def initialize_astra_collection():
    """
    Connect to Astra DB and return the collection object.
    """
    token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
    endpoint = os.getenv("ASTRA_DB_API_ENDPOINT")
    collection_name = os.getenv("ASTRA_COLLECTION_NAME")

    if not all([token, endpoint, collection_name]):
        raise ValueError("Missing one or more required environment variables: "
                         "ASTRA_DB_APPLICATION_TOKEN, ASTRA_DB_API_ENDPOINT, ASTRA_COLLECTION_NAME")

    client = DataAPIClient(token)
    db = client.get_database_by_api_endpoint(endpoint)
    collection = db.get_collection(collection_name)
    return collection


def ingest_files_to_astra(folder_path):
    """
    Read JSON files from a folder and ingest them into Astra DB.

    Args:
        folder_path (str): Path to the folder containing JSON files.
    """
    try:
        collection = initialize_astra_collection()
        print("Connected to Astra DB.")

        # Iterate over all JSON files in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith("_filtered.json"):
                file_path = os.path.join(folder_path, filename)
                with open(file_path, 'r') as f:
                    issue_data = json.load(f)

                # Extract the `id` from the JSON file to use as the document ID
                json_id = issue_data.get("id")
                if not json_id:
                    print(f"Skipping {filename}: No 'id' field found in JSON.")
                    continue

                # Prepare the document for insertion
                document = {
                    "_id": json_id,  # Use `id` from JSON as the document ID
                    "content": json.dumps(issue_data),  # Store entire JSON data as a string
                    "$vectorize": json.dumps(issue_data),  # Store vectorizable data
                    "metadata": issue_data  # Store the JSON data as-is under "metadata"
                }

                # Insert the document into Astra DB
                collection.insert_one(document)
                print(f"Successfully ingested {filename} into Astra DB with id '{json_id}'.")

    except Exception as e:
        print(f"Error during ingestion: {e}")


if __name__ == "__main__":
    # Path to the folder containing the filtered JSON files
    folder_path = "./filtered_issue_data"

    # Run the ingestion process
    ingest_files_to_astra(folder_path)
