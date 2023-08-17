from django.shortcuts import render
from django.http import HttpResponse
import pymongo

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to Django & Mongodb connectivity</h1>")

client=pymongo.MongoClient('mongodb://localhost:27017/')
dbname=client['Djangodb'] #defining database name
collectionname=dbname['Books'] #defining collection name

Books={
    "book_name":"Django",
    "book_type":"ebook",
    "book_price":280
}

collectionname.insert_one(Books)

collectionname.update_one({"book_name": "Django"}, {"$set": {"book_type": "paper book"}})


books_details=collectionname.find({})

for b in books_details:
    print(b['book_name'])
    print(b['book_type'])
    print(b['book_price'])
    
    