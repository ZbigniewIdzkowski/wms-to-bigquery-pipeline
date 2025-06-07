from utils.logger import get_logger

logger = get_logger(__name__)

def simulate_upload_to_bigquery(data):
    if not data:
        logger.warning("No data to upload.")
        return False

    for row in data:
        logger.info(f"Uploading row to BigQuery: {row}")
        # Here you'd normally use the BigQuery client library

    logger.info(f"{len(data)} rows uploaded to BigQuery successfully.")
    return True
