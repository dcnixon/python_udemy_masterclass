def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    word_search(doc_list, 'casino')
    [0]
    """
    #split the document into a list of words
    #check word in words == keyword

    match_list = []
    for doc in doc_list:
        stripped_string = doc.strip(".")
        words = stripped_string.split()

        for word in words:
            if word.lower() == keyword.lower():
                match_list.append(doc)
                break

    return [doc_list.index(match)for match in match_list]

docs_listed = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
print(word_search(docs_listed, "casino"))

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    keywords = ['casino', 'they']
    multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """

    return dict([(i, word_search(doc_list, i)) for i in keywords])


doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']
print(multi_word_search(doc_list, keywords))