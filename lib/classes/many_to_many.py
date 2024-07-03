class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.all.append(self)

    @property 
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if isinstance(title,str) and (5 <= len(title) <= 50):
            self._title = title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,author):
        if isinstance(Author,object):
            self._author = author
            Author.all.append(self)

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,magazine):
        if isinstance(Magazine,object):
            self._magazine = magazine
            Magazine.all.append(magazine)
    
class Author:

    all = []

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, '_name') or self._name is None:
            if isinstance(name, str) and (len(name) > 1):
                self._name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]
        pass

    def magazines(self):
        magazines = [article.magazine for article in Article.all if article.author == self]
        set_magazines = set(magazines)
        unique_magazines = (list(set_magazines))
        return unique_magazines
        pass

    def add_article(self, magazine, title):
        return Article(self,magazine,title)
        pass

    def topic_areas(self):
        topic_areas = [article.magazine.category for article in Article.all if article.author == self]
        set_topic_areas = set(topic_areas)
        unique_topic_areas = (list(set_topic_areas))
        if topic_areas == []:
                return None
        else:
            return unique_topic_areas

class Magazine:
    all=[]
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.all.append(self)
    
    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name,str) and (2 <= len(name) <= 16):
            self._name = name

    @property
    def category(self):
        return self._category
    
    @category.setter 
    def category(self,category):
        if isinstance(category,str) and (len(category) > 0):
            self._category = category

    def articles(self): 
        return [article for article in Article.all if article.magazine == self]
        pass

    def contributors(self):
        contributors = [article.author for article in Article.all if article.magazine == self]
        set_contributors = set(contributors)
        unique_contributors = list(set_contributors)
        return unique_contributors
        pass

    def article_titles(self):
        article_titles = [article.title for article in Article.all if article.magazine == self]
        if article_titles == []:
            return None
        else: 
            return article_titles

        pass

    def contributing_authors(self):
        contributing_authors = [article.author for article in Article.all if article.magazine == self]
        if len(contributing_authors) > 2:
            return contributing_authors
        else:
            return None
        pass

writer = Author("Jack")
print(writer.topic_areas())