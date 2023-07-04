from scrape_twitter.helpers import count_words


def test_happy_flow():
    tweets = [
        "Het zijn GEEN vaccins!!!",
        "Mijn hond is geen kat",
        "De Honden zijn op de TAFEL",
    ]
    result = count_words(tweets)
    assert result == {"vaccin": 1, "hond": 2, "kat": 1, "tafel": 1}


def test_add_counts():
    current_count = {"hond": 102}
    tweets = ["Mijn hond is geen kat", "De Honden zijn op de TAFEL", "koets"]
    count_words(tweets, current_count)
    assert current_count == {"hond": 104, "kat": 1, "tafel": 1, "koets": 1}
