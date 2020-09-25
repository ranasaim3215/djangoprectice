from django.urls import path
from .views import AboutpageView,RowPage
urlpatterns = [
    # path("", views.homepage, name="homepage"),
    path("", AboutpageView.as_view(),name='home'),
    path("about/", RowPage.as_view(),name='about')
]