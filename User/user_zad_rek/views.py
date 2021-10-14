from django.shortcuts import render
# Create your views here.
from .models import Website
from .filters import CategoryFilter
from django.http import  HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):

    page = request.GET.get('page')
    sort = request.GET.get("sort", None)
    filter = request.GET.get("category", None)

    if filter != None and sort !=None:
        try:
            website_list = CategoryFilter(request.GET, queryset=Website.filter(category=filter).values().order_by(sort)).qs
        except :
            website_list = CategoryFilter(request.GET, queryset=Website.objects.all()).qs
    elif filter != None and sort ==None:
        try:
            website_list = CategoryFilter(request.GET, queryset=Website.filter(category=filter).values()).qs
        except :
            website_list = CategoryFilter(request.GET, queryset=Website.objects.all()).qs
    elif filter == None and sort !=None:
        try:
            website_list = CategoryFilter(request.GET, queryset=Website.objects.all().order_by(sort)).qs
        except :
            website_list = CategoryFilter(request.GET, queryset=Website.objects.all()).qs
    else:
        website_list = CategoryFilter(request.GET, queryset=Website.objects.all()).qs


    paginator = Paginator(website_list, 25)
    try:
        websites = paginator.page(page)
    except PageNotAnInteger:
        websites = paginator.page(1)
    except EmptyPage:
        websites = paginator.page(paginator.num_pages)


    return render(request, 'website_list.html', { 'websites': websites })

# def index(request):
#     req = Website.objects.all()
#     return HttpResponse(req)
