from seasons import get_minutes
from datetime import date , timedelta
import pytest 

def test_get_minutes():
    # Test with date 1 day ago = 1440 minutes
    yesterday = date.today() - timedelta(days=1)
    assert get_minutes(yesterday) == 1440

def test_future_date():
    tomorrow = date.today() + timedelta(days=1)
    with pytest.raises(ValueError):
        get_minutes(tomorrow)

def test_one_year():
    # Approx 365 days * 1440
    year_ago = date.today() - timedelta(days=365)
    minutes = get_minutes(year_ago)
    assert minutes == 365 * 1440