from upload_to_bigquery import simulate_upload_to_bigquery

def test_upload_to_bigquery():
    data = [
        {"order_id": "A123", "date": "2024-10-01", "qty": 10},
        {"order_id": "A124", "date": "2024-10-02", "qty": 5}
    ]
    success = simulate_upload_to_bigquery(data)
    assert success is True

def test_upload_empty_data():
    empty_data = []
    success = simulate_upload_to_bigquery(empty_data)
    assert success is False

