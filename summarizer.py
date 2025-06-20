import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import string
nltk.download('punkt')
nltk.download('stopwords')
def summarize_text(text, max_sentences=3):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    freq_table = defaultdict(int)
    for word in words:
        if word not in stop_words and word not in string.punctuation:
            freq_table[word] += 1
    sentences = sent_tokenize(text)
    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_table:
                sentence_scores[sentence] += freq_table[word]
    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = ' '.join(ranked_sentences[:max_sentences])
    return summary
