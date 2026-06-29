import re

SYNONYMS = {
    "covid": ["coronavirus", "sars cov 2", "viral infection"],
    "diabetes": ["type 1 diabetes", "type 2 diabetes", "insulin", "glucose"],
    "cancer": ["tumor", "carcinoma", "malignancy"],
    "heart": ["cardiac", "cardiovascular"],
    "blood": ["plasma", "serum"],
    "vaccine": ["immunization", "vaccination"],
}


def expand_query(query):
    words = re.findall(r"\w+", query.lower())
    expanded = words.copy()

    for word in words:
        if word in SYNONYMS:
            expanded.extend(SYNONYMS[word])

    return " ".join(expanded)