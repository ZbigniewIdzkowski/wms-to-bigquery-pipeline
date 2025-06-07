from datetime import datetime
from utils.logger import get_logger

logger = get_logger(__name__)

def clean_orders(data):
    cleaned = []
    for idx, record in enumerate(data):
        try:
            record["order_id"] = record["order_id"].strip()
            record["date"] = datetime.strptime(record["date"], "%Y-%m-%d").date().isoformat()
            record["qty"] = int(record["qty"])
            cleaned.append(record)
        except Exception as e:
            logger.error(f"Row {idx} failed to clean: {str(e)}")
            continue
    logger.info(f"{len(cleaned)} records cleaned successfully.")
    return cleaned
