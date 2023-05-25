from django.urls import path
from app import views


app_name='app'
urlpatterns=[
    path('',views.IndexView.as_view(),name='home'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('portfolio/',views.PortfolioView.as_view(),name='portfolio'),
    path('portfolio/<slug:slug>',views.PortfolioDetailView.as_view(),name='portfoliodetail'),
    path('blog/',views.BlogView.as_view(),name='blog'),
    path('blog/<slug:slug>',views.BlogDetailView.as_view(),name='blogdetail'),







]

