from clean_and_format_orders import clean_orders

def test_clean_orders():
    raw_data = [
        {"order_id": " A123 ", "date": "2024-10-01", "qty": "10"},
        {"order_id": "A124", "date": "invalid-date", "qty": "5"},  # should fail
        {"order_id": "A125", "date": "2024-10-03", "qty": "7"}
    ]

    cleaned = clean_orders(raw_data)

    assert len(cleaned) == 2  # One should be skipped
    assert cleaned[0]["order_id"] == "A123"
    assert cleaned[0]["date"] == "2024-10-01"
    assert isinstance(cleaned[0]["qty"], int)

