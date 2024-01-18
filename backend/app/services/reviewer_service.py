from ..models.reviewer import Reviewer
from ..models import db

def get_reviewers():
    return [result.to_dict() for result in Reviewer.query.all()]

def get_reviewer(id):
    # get queries by the primary key, which is id for the Restaurant table
    reviewer = Reviewer.query.get(id)
    if reviewer is None:
        return reviewer
    return reviewer.to_dict()

def delete_review(id):
    deleted = Reviewer.query.filter_by(id=id).delete()
    db.session.commit()

    if deleted == 1:
        return id
    return None

def update_reviewer(id, reviewer_data):
    reviewer = Reviewer.query.get(id)
    if reviewer is None:
        return None  # Reviewer not found

    for key, value in reviewer_data.items():
        setattr(reviewer, key, value)

    db.session.commit()

    return reviewer.to_dict()

def create_reviewer(reviewer_data):
    new_reviewer = Reviewer(**reviewer_data)
    db.session.add(new_reviewer)
    db.session.commit()

    return new_reviewer.to_dict()