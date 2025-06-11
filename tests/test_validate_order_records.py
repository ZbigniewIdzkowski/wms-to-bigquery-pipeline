from validate_order_records import validate_records

def test_validate_records():
    sample_data = [
        {"order_id": "A123", "date": "2024-10-01", "qty": 10},
        {"order_id": "A124", "date": "2024-10-02", "qty": -5}, 
        {"order_id": "", "date": "2024-10-03", "qty": 7},       
    ]

    is_valid, errors = validate_records(sample_data)

    assert not is_valid
    assert any("Invalid quantity" in e for e in errors)
    assert any("Missing order ID" in e for e in errors)
