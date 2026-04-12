from textblob import TextBlob
import re


# ─── Text Preprocessing ───────────────────────────────────────────────────────

def preprocess_text(text):
    """Clean and normalize text before analysis."""
    text = text.lower()                        # Lowercase
    text = re.sub(r'http\S+|www\S+', '', text) # Remove URLs
    text = re.sub(r'@\w+|#\w+', '', text)      # Remove mentions & hashtags
    text = re.sub(r'[^a-zA-Z\s!?.,]', '', text) # Keep letters + basic punctuation
    text = re.sub(r'\s+', ' ', text).strip()   # Remove extra spaces
    return text


# ─── Sentiment Analysis ───────────────────────────────────────────────────────

def analyze_sentiment(text):
    """
    Analyze sentiment of given text using TextBlob.

    Returns:
        dict with keys: original, cleaned, polarity, subjectivity, label, confidence
    """
    cleaned = preprocess_text(text)
    blob = TextBlob(cleaned)

    polarity    = round(blob.sentiment.polarity, 4)     # -1 (negative) to +1 (positive)
    subjectivity = round(blob.sentiment.subjectivity, 4) # 0 (objective) to 1 (subjective)

    # Classify label
    if polarity > 0.1:
        label = "Positive"
        emoji = ":)"
    elif polarity < -0.1:
        label = "Negative"
        emoji = ":("
    else:
        label = "Neutral"
        emoji = ":|"

    # Confidence: how far from 0 (neutral)
    confidence = round(abs(polarity) * 100, 1)

    return {
        "original":     text,
        "cleaned":      cleaned,
        "polarity":     polarity,
        "subjectivity": subjectivity,
        "label":        label,
        "emoji":        emoji,
        "confidence":   f"{confidence}%"
    }


# ─── Batch Analysis ───────────────────────────────────────────────────────────

def analyze_multiple(texts):
    """Analyze a list of texts and return results."""
    results = []
    for text in texts:
        result = analyze_sentiment(text)
        results.append(result)
    return results


def print_result(result):
    """Pretty-print a single sentiment result."""
    print(f"\n{'─'*60}")
    print(f"  Text     : {result['original'][:70]}")
    print(f"  Cleaned  : {result['cleaned'][:70]}")
    print(f"  Sentiment: {result['label']} {result['emoji']}")
    print(f"  Polarity : {result['polarity']:+.4f}  (-1=very negative, +1=very positive)")
    print(f"  Subjectiv: {result['subjectivity']:.4f}  (0=objective, 1=subjective)")
    print(f"  Confidence: {result['confidence']}")


# ─── Main Demo ────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    print("=" * 60)
    print("       NLP TASK: SENTIMENT ANALYSIS")
    print("       Using TextBlob | BS Artificial Intelligence")
    print("=" * 60)
    print("\nEnter any sentence and I will analyze its sentiment.")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("Enter text: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break
        if not user_input:
            print("Please enter some text.")
            continue
        result = analyze_sentiment(user_input)
        print_result(result)
        print()