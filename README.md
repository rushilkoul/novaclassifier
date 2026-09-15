## novaclassifier
tiny TF-IDF text classifier for the IEEESBJIIT Techblocks 2026 Agentic AI workshop.


start here:
```bash
# or however you setup your venv
uv venv
source .venv/bin/activate.fish

uv pip install -r requirements.txt
```

```bash
python classifier.py  # train the model
python main.py        # cli demo
```

---

### Notes for myself + those interested lol

my only two promising options were either a 1D CNN or a TF-IDF with logistic regression.

|  | TF-IDF + logreg| 1D CNN |
| :--- | :--- | :--- |
| **accuracy** | 90.9% | 72.7% |
| **training time** | 3.4 ms | 426 ms |
| **inference latency** | 0.26 ms | 0.04 ms |
| **params** | 615 | 2917 |

evidently, i ended up going for a TF-IDF instead. during testing, the inference time of the CNN was significantly faster (0.04ms vs 0.26) but the number of queries isnt really stacking up at the same rate for this difference to really mean anything.

ran 5 test runs, TFIDF remained baslically solid at ~90% accuracy, while the CNN accuracy swung a lot, lowest i got it was at 54% :p

CNNs are superior in theory, but we just dont have enough data (nor can i be bothered to generate the amount/kind it needs) yeah we have more params here but with such little data it is just more ways to overfit.

so yeah too much variance and not enough data for the CNN to realistically be usable for this workshop. cool stuff tho :)

