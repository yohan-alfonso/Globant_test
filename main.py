# Flask 2.2.3

from flask import Flask, request, jsonify
from google.cloud import bigquery

app = Flask(__name__)

# Initialize the BigQuery client
bigquery_client = bigquery.Client()

# Data dictionary rules for each table
data_dictionary_rules = {
    "employees": ["id", "name", "datetime", "department_id", "job_id"],
    "departments": ["id", "department"],
    "jobs": ["id", "job"],
}

@app.route('/api/<table_name>', methods=['POST'])
def insert_data(table_name):
    if table_name not in data_dictionary_rules:
        return jsonify({"error": "Invalid table name"}), 400

    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        if isinstance(data, dict):  # Single transaction
            data = [data]
        elif isinstance(data, list):  # Batch transactions (1 to 1000 rows)
            if len(data) > 1000:
                return jsonify({"error": "Batch size exceeds the limit of 1000 rows"}), 400
        else:
            return jsonify({"error": "Invalid data format"}), 400

        # Validate data against the data dictionary rules
        for transaction in data:
            for field in data_dictionary_rules[table_name]:
                if field not in transaction:
                    return jsonify({"error": f"Field '{field}' is missing"}), 400

        # Insert the data into BigQuery table
        dataset_id = 'globant-test-yah.test'  # Replace with your BigQuery dataset ID
        table_id = f"{dataset_id}.{table_name}"

        errors = bigquery_client.insert_rows_json(table_id, data)

        if errors:
            return jsonify({"error": "Failed to insert data into BigQuery"}), 500

        return jsonify({"message": "Data inserted successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
