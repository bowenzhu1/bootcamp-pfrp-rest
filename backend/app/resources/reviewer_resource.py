class ReviewerResource(object):
    def __init__(self, name, description=None, rating=None):
        self.name = name
        self.description = description
        self.rating = int(rating) if rating is not None else rating
    