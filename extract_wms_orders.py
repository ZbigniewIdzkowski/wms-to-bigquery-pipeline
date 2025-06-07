import csv
from utils.logger import get_logger

logger = get_logger(__name__)

def extract_orders_from_csv(file_path):
    orders = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row["qty"] = int(row["qty"])  # Convert quantity to integer
                orders.append(row)
        logger.info(f"Extracted {len(orders)} orders from {file_path}")
        return orders
    except Exception as e:
        logger.error(f"Failed to extract orders: {str(e)}")
        raise
