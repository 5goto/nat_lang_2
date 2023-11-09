import string
import nltk

nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


def generate_summary(text, num_sentences=3):
    # Приведение текста к нижнему регистру
    text = text.lower()

    # Токенизация текста
    tokens = word_tokenize(text)

    # Удаление пунктуации
    table = str.maketrans('', '', string.punctuation)
    tokens = [word.translate(table) for word in tokens]

    # Подсчет частоты встречаемости слов
    fdist = FreqDist(tokens)

    # Выбор наиболее часто встречающихся слов
    top_words = fdist.most_common(10)

    # Формирование реферата из предложений, содержащих наиболее часто встречающиеся слова
    sentences = text.split('.')
    summary = []
    for sentence in sentences:
        for word, _ in top_words:
            if word in sentence:
                summary.append(sentence)
                break
        if len(summary) >= num_sentences:
            break

    return '. '.join(summary) + '.'


if __name__ == '__main__':
    print(generate_summary(''))
