class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property 
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if isinstance(title,str) and (5 <= len(title) <= 50):
            self._title = title
            
        
class Author:
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
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
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
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

author = Author("Cary")
author.name = "Jack"
print(author.name)
