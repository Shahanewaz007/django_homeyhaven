from django.shortcuts import render, redirect
from .forms import RatingForm  
from hotels.models import Hotel, Review

def give_rating(request, hotel_id):
    hotel = Hotel.objects.get(id = hotel_id)
    
        
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = Review(
                hotel = hotel,
                user = request.user,
                rating = form.cleaned_data['rating'],
                comment = form.cleaned_data['comment']
            )
            rating.save()
            return redirect('hotel_details', hotel.slug, hotel.id)

    else:
        form = RatingForm()

    return render(request, 'review.html', {'form': form,})

def update_review(request, hotel_id):
    hotel = Hotel.objects.get(id=hotel_id)
    review = Review.objects.get(hotel = hotel, user=request.user)
    
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            review.rating = form.cleaned_data['rating']
            review.comment = form.cleaned_data['comment']
            review.save()
            return redirect('hotel_details', hotel.slug, hotel.id)
            
    else:
        form = RatingForm()

    return render(request, 'update_review.html', {'form': form,})