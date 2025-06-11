from utils.logger import get_logger

logger = get_logger(__name__)

def validate_records(data):
    errors = []
    for idx, record in enumerate(data):
        if record["qty"] < 0:
            errors.append(f"Record {idx} - Invalid quantity '{record['qty']}'")
        if not record["order_id"]:
            errors.append(f"Record {idx} - Missing order ID")
        
    if errors:
        logger.error(f"Validation failed: {errors}")
        return False, errors
    logger.info("Validation successful")
    return True, []
