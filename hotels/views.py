from django.shortcuts import render
from .models import Hotel, Review
from django.core.paginator import Paginator

def see_hotels(request):    
    all_items = Hotel.objects.all().order_by('id')
    items_per_page = 4
    paginator = Paginator(all_items, items_per_page)
    page_number = request.GET.get('page')
    hotels = paginator.get_page(page_number)
    return render(request, 'hotel.html', {'hotels': hotels})

def  hotel_detail(request, hotel_slug, hotel_id):
    
    single_hotel = Hotel.objects.get(slug=hotel_slug, id=hotel_id)
    if request.user.is_authenticated:
        user_reviews = Review.objects.filter(hotel=single_hotel, user=request.user)
        
        has_reviewed = user_reviews.exists()
        if has_reviewed:
            review = Review.objects.get(hotel=single_hotel, user=request.user)
            return render(request, 'hotel_details.html', {'hotels' : single_hotel , 'review': review, 'has_reviewed': has_reviewed})

    
        return render(request, 'hotel_details.html', {'hotels' : single_hotel , 'has_reviewed': has_reviewed})
    return render(request, 'hotel_details.html', {'hotels' : single_hotel ,})

def hotel_search(request):
    hotels = Hotel.objects.all()

    query = request.GET.get('search')
    if query:
        hotels = hotels.filter(address__icontains=query)

    return render(request, 'hotel_search.html', {'hotels': hotels})