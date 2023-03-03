from datetime import date


def calc(parcel: float, interest_rate: float, early_days: int):
    rate_per_day = interest_rate / 30
    return round(parcel - parcel * rate_per_day * early_days, 2)
