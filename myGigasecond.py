from datetime import timedelta
from datetime import date


def add_gigasecond(dt):
    """Calculate the date that someone will celebrate their 1Gsanniversary."""
    return dt + timedelta(seconds=10**9)

print(add_gigasecond(date(1974, 1, 8)))
