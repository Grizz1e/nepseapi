def extract_date(date_str: str):
    if len(date_str) != 8:
        return False
    
    try:
        int(date_str)
    except Exception as e:
        return False
    year = date_str[:4]
    month = date_str[4:6]
    date = date_str[6:]
    return {
        "year": year,
        "month": month,
        "date": date
    }
