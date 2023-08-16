from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Movieapp, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movieapp.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movieapp.objects.all()
    return render(request, 'home.html',	{'searchTerm':searchTerm, 'movies': movies})

def about(request):
    return HttpResponse('<h1>Welcome to about the Page</h1>')

def signup(request):
    email = request.GET.get("email")
    return render(request, "signup.html", {"email":email})


def detail(request, movieapp_id): 
    movieapp = get_object_or_404(Movieapp,pk=movieapp_id)
    reviews = Review.objects.filter(movieapp = movieapp)
    return render(request, 
                  'detail.html', {'movieapp':movieapp, 'reviews':reviews})
    
@login_required
def createreview(request, movieapp_id):   
    movieapp = get_object_or_404(Movieapp,pk=movieapp_id) 
    if request.method == 'GET':
        return render(request, 'createreview.html', 
                      {'form':ReviewForm(), 'movieapp': movieapp})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movieapp = movieapp
            newReview.save()
            return redirect('detail', newReview.movieapp.id)
        except ValueError:
            return render(request, 'createreview.html', 
              {'form':ReviewForm(),'error':'bad data passed in'})

@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review,pk=review_id,user=request.user)
    if request.method == 'GET':
        forms = ReviewForm(instance=review)
        return render(request, 'updatereview.html', 
                      {'review': review,'forms':forms})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('detail', review.movieapp.id)
        except ValueError:
            return render(request, 'updatereview.html',
             {'review': review,'form':form,'error':'Bad data in form'})
            
@login_required        
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('detail', review.movieapp.id)
