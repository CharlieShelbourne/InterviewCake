import unittest

class WordCloudData:
    def __init__(self, input):
        self.sentence = input
        self.puncuation = set(['!', '?', '.', ':', '(', ')', ','])
        self.words_to_counts = {}
        self.remove_punctuation()
        self.sentence = self.sentence.lower().split(" ")
        self.unique_words = set(self.sentence)
        self.count_unique_words()
        self.remove_hyphens()
        self.remove_empties()

    def remove_punctuation(self): 
        for punct in self.puncuation:
            if punct in set(list(self.sentence.strip())):
                self.sentence = self.sentence.replace(punct, ' ')
        
    def count_unique_words(self):
        for word in self.sentence:
            if word in self.unique_words:
                if word in self.words_to_counts:
                    self.words_to_counts[word] += 1
                else: 
                    self.words_to_counts[word] = 1
    
    def remove_hyphens(self):
        if "-" in self.words_to_counts:
            self.words_to_counts.pop("-")

    def remove_empties(self):
        if '' in self.words_to_counts:
            self.words_to_counts.pop('')
    
    def remove_quotes(self):
        if self.sentence[0] == '\"':
            self.sentence.remove('\"')
        elif self.sentence[0] == "\'":
            self.sentence = self.sentence[1:]
        elif self.sentence[-1] == "\'":
            self.sentence = self.sentence[:len(self.sentence)-1]

world_cloud = WordCloudData('\"We came, we saw, we conquered...then we ate Bill\'s (Mille-Feuille) cake.\"')
print(world_cloud.words_to_counts)


class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'i': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)
    
    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)
    
    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'strawberry': 1, 'short': 1, 'yum': 1}
        self.assertEqual(actual, expected)
        
    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"bakery": 1, "cakes": 1, "allie's": 1, "sasha's": 1}
        self.assertEqual(actual, expected)
   

unittest.main(verbosity=2)
