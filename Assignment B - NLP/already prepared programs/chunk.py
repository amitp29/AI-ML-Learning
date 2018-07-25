from nltk.chunk import ne_chunk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

chunk_sentence = ne_chunk(pos_tag(word_tokenize('My name is AnilKumar.')))
print (chunk_sentence)
chunk_sentence.draw()