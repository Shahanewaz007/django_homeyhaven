from django.urls import path
from . import views
urlpatterns = [
    path('review/<int:hotel_id>', views.give_rating, name='rating'),
    path('updatereview/<int:hotel_id>', views.update_review, name='update_rating'),
    path('deletereview/<int:review_id>', views.remove_review, name='delete_rating'),
]