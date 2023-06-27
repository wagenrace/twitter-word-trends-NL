from scrape_twitter.helpers import tokenize_tweet


def test_happy_flow():
    tweet = "mijn hond zweet"
    result = tokenize_tweet(tweet)
    assert result == ["mijn", "hond", "zweet"]


def test_remove_enters():
    tweet = """
    Dus wij sturen wapens en geld naar de Oekraïne zodat zij vervolgens de Northstream 2 op kunnen blazen?
    En hier in Nederland en de VS wisten ze dat van te voren?

    Ja echt? 

    Alle boosterspuiten nog aan toe zeg.
    """
    result = tokenize_tweet(tweet)
    assert result == [
        "dus",
        "wij",
        "sturen",
        "wapens",
        "en",
        "geld",
        "naar",
        "de",
        "oekraïne",
        "zodat",
        "zij",
        "vervolgens",
        "de",
        "northstream",
        "2",
        "op",
        "kunnen",
        "blazen",
        "en",
        "hier",
        "in",
        "nederland",
        "en",
        "de",
        "vs",
        "wisten",
        "ze",
        "dat",
        "van",
        "te",
        "voren",
        "ja",
        "echt",
        "alle",
        "boosterspuiten",
        "nog",
        "aan",
        "toe",
        "zeg",
    ]


def test_remove_emojis():
    tweet = '""Inhoudelijk profiel"" 🧐😂😂😂😂😂'
    result = tokenize_tweet(tweet)

    assert result == ["inhoudelijk", "profiel"]


def test_words_with_dashes():
    tweet = "Tijdelijke basisschool op voetbalcomplex Berkel-Enschot https://t.co/vu8Pl7RbWz https://t.co/8dm4gaOSwe"
    result = tokenize_tweet(tweet)

    assert result == [
        "tijdelijke",
        "basisschool",
        "op",
        "voetbalcomplex",
        "berkel-enschot",
    ]


def test_remove_links():
    tweet = "Gemeente onderzoekt handel in Joods vastgoed tijdens en na WOII https://t.co/awTQtZZRmh https://t.co/VxTa6ES2Rq"
    result = tokenize_tweet(tweet)

    assert result == [
        "gemeente",
        "onderzoekt",
        "handel",
        "in",
        "joods",
        "vastgoed",
        "tijdens",
        "en",
        "na",
        "woii",
    ]
