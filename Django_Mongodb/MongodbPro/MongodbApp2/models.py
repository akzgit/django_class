from django.db import models

from mongoengine import Document, StringField, FloatField

class Book(Document):
    book_name = StringField(required=True)
    book_type = StringField()
    book_price = FloatField()