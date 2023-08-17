# from django.shortcuts import render
# from django.http import HttpResponse
# from MongodbApp2.models import Book  # Import your Book model

# def add_book(request):
#     # Create a new book document
#     new_book = Book(
#         book_name="New Book",
#         book_type="paper book",
#         book_price=350
#     )
#     new_book.save()  # Save the new book to the database
    
#     return HttpResponse("New book added successfully.")  
                                                 # => to save data to mongodb


from django.shortcuts import render, redirect
from MongodbApp2.forms import BookForm
from MongodbApp2.models import Book  # Import your Book model

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book_data = form.cleaned_data
            new_book = Book(
                book_name=book_data['book_name'],
                book_type=book_data['book_type'],
                book_price=book_data['book_price']
            )
            new_book.save()
            return redirect('add_book')  # Redirect to the same page after successful submission
    else:
        form = BookForm()
    
    return render(request, 'm2/add_book.html', {'form': form})                                                 