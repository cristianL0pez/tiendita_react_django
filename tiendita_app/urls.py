from django.urls import path
from django.views import generic

urlpatterns = [
    path('' ,generic.TemplateView.as_view(template_name='view1.html')),
    path('view2/', generic.TemplateView.as_view(template_name='view2.html')),
    path('view3/', generic.TemplateView.as_view(template_name='view3.html')),
    path('login/',generic.TemplateView.as_view(template_name='view2.html')),
    
]