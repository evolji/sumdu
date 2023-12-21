import nltk
nltk.download('punkt')
from nltk.corpus import gutenberg
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string

nltk.download('gutenberg')
nltk.download('stopwords')
text = gutenberg.raw('edgeworth-parents.txt')

words = nltk.word_tokenize(text)
num_words = len(words)
print(f"Кількість слів у тексті: {num_words}")

fdist = FreqDist(words)
top_words = fdist.most_common(10)
print(f"10 найбільш вживаних слів: {top_words}")

words, counts = zip(*top_words)
plt.bar(words, counts)
plt.title('10 найбільш вживаних слів (з урахуванням стоп-слів та пунктуації)')
plt.xlabel('Слова')
plt.ylabel('Частота вживання')
plt.show()

stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word not in string.punctuation]

fdist_filtered = FreqDist(filtered_words)
top_words_filtered = fdist_filtered.most_common(10)
print(f"10 найбільш вживаних слів (після видалення стоп-слів та пунктуації): {top_words_filtered}")

words_filtered, counts_filtered = zip(*top_words_filtered)
plt.bar(words_filtered, counts_filtered)
plt.title('10 найбільш вживаних слів (після видалення стоп-слів та пунктуації)')
plt.xlabel('Слова')
plt.ylabel('Частота вживання')
plt.show()




from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

nltk.download('punkt')
nltk.download('stopwords')

input_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

with open('input_text.txt', 'w', encoding='utf-8') as file:
    file.write(input_text)

tokens = word_tokenize(input_text)

lemmatizer = WordNetLemmatizer()
porter_stemmer = PorterStemmer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
stemmed_tokens = [porter_stemmer.stem(token) for token in tokens]

stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in lemmatized_tokens if token.lower() not in stop_words]

filtered_tokens = [token for token in filtered_tokens if token not in string.punctuation]
processed_text = ' '.join(filtered_tokens)
with open('processed_text.txt', 'w', encoding='utf-8') as file:
    file.write(processed_text)
