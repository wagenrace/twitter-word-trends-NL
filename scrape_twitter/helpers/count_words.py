from .tokenize_tweet import tokenize_tweet
import spacy

model_name = "nl_core_news_lg"
try:
    NLP = spacy.load(model_name)
except OSError:
    print(f"downloading the model {model_name}")
    spacy.cli.download(model_name)
    NLP = spacy.load(model_name)


def count_words(tweets: list[str], all_words: dict = {}):
    for tweet in tweets:
        words = tokenize_tweet(tweet)
        doc = NLP(" ".join(words))

        for token in doc:
            # Skip hashtags
            if token.text.startswith("#"):
                continue

            # Skip stop words
            if token.is_stop:
                continue

            # Skip numbers
            if token.pos_ == "NUM":
                continue

            lemma = token.lemma_.lower()

            # Skip empty strings
            if lemma in ["", " "]:
                continue

            all_words[lemma] = all_words.get(lemma, 0) + 1

    return all_words
