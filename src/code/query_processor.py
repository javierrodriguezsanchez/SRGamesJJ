import nltk
import gensim
import json

class query_processor:
    def __init__(self, query):
        self.query = query
        self.tokenized_query = []
        self.vector_repr = []
        self.query_bow = []

    def tokenization_nltk(self):
        self.tokenized_query = nltk.tokenize.word_tokenize(self.query)

    def remove_noise_nltk(self):
        self.tokenized_query = [word.lower() for word in self.tokenized_query if word.isalpha()]

    def remove_stopwords(self):
        stop_words = set(nltk.corpus.stopwords.words('english'))
        self.tokenized_query = [word for word in self.tokenized_query if word not in stop_words]

    def morphological_reduction_nltk(self, use_lemmatization=True):
        if use_lemmatization:
            lemmatizer = nltk.stem.WordNetLemmatizer()
            self.tokenized_query = [lemmatizer.lemmatize(word) for word in self.tokenized_query]
                
        else:
            stemmer = nltk.stem.PorterStemmer()
            self.tokenized_query = [stemmer.stem(word) for word in self.tokenized_query]

    def filter_tokens_by_occurrence(self, no_below=5, no_above=0.5):
        tokenized_docs = []
        with open('../../data/tokenized_docs.json', 'r') as file:
            tokenized_docs = json.load(file)
        dictionary = gensim.corpora.Dictionary(tokenized_docs)
        dictionary.filter_extremes(no_below=no_below, no_above=no_above)

        filtered_words = [word for _, word in dictionary.iteritems()]
        self.tokenized_query = [word for word in self.tokenized_query if word in filtered_words]
        self.query_bow = dictionary.doc2bow(self.tokenized_query)

    def vector_representation(self, use_bow=True):
        corpus = []
        with open('../../data/corpus.json', 'r') as file:
            corpus = json.load(file)

        if use_bow:
            self.vector_repr = self.query_bow
        else:
            tfidf = gensim.models.TfidfModel(corpus)
            self.vector_repr = tfidf[self.query_bow]

    def matched_docs(self):
        doc_vector_repr = []
        with open('../../data/vector_repr.json', 'r') as file:
            doc_vector_repr = json.load(file)
        self.tokenization_nltk()
        self.remove_noise_nltk()
        self.remove_stopwords()
        self.morphological_reduction_nltk()
        self.filter_tokens_by_occurrence()
        self.vector_representation()

        index = gensim.similarities.MatrixSimilarity(doc_vector_repr)
                
        similarities = index[self.vector_repr]
        top_matches = sorted(enumerate(similarities), key=lambda x: -x[1])[:10]

        best_match_indices = [match[0] for match in top_matches]
        return best_match_indices
        