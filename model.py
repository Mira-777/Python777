import pickle
import os.path

class Article:
    def __init__(self, title, genre, director, year, duration, atelier, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.atelier = atelier
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.genre})"

class ArticleModel:
    def __init__(self):
        self.db_name = 'bd.txt'
        self.articles = self.load_data() #{}

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_single_arcticle(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            "название": article.title,
            "жанр": article.genre,
            "режиссера": article.director,
            "год выпуска": article.year,
            "длительность": article.duration,
            "студию": article.atelier,
            "актеров": article.actors
        }

        return dict_article
    def remove_article(self, user_title):
        return self.articles.pop(user_title)


    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)

        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.articles, f)




