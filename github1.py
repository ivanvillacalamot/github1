import spacy
pipelineCatala = spacy.load("ca_core_news_trf")
paraulesComuns=pipelineCatala.Defaults.stop_words
print(paraulesComuns)