
from classifier import IntentClassifier
from tools import TOOLMAP

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

    tool_fn = TOOLMAP[intent]
    result = tool_fn(query)
    return f"{intent}: {confidence:.0%} confident\n{result}"


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
