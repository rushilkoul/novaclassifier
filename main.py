from classifier import IntentClassifier

TOOLMAP = {
    "searchWeb": "Web Search",
    "searchYoutube": "YouTube Search",
    "searchWikipedia": "Wikipedia Search",
    "create_folder": "Create Folder",
    "create_file": "Create File",
    "read_file": "Read File",
    "get_weather": "Get Weather",
    "get_news": "Get News",
    "convert_currency": "Convert Currency",
}


def ask_gemini(query: str) -> str:
    return f"send to gemini: \"{query}\""


def handle_query(classifier: IntentClassifier, query: str) -> str:
    intent, confidence = classifier.predict(query)

    if intent is None:
        result = ask_gemini(query)
        return f"no clue\n{result}"

    if intent == "LLM":
        result = ask_gemini(query)
        return f"classified as gemini material: {confidence:.0%} confident\n{result}"

    return f"{intent}: {confidence:.0%} confident"


def main():
    classifier = IntentClassifier()
    print("classifier demo. type a query, or 'q' to exit.\n")
    while True:
        query = input("> ").strip()
        if query.lower() == 'q': break
        if not query:
            continue
        print(handle_query(classifier, query), '\n')


if __name__ == "__main__":
    main()
