from django.shortcuts import render
from .models import PatentDatabase

def base(request):
    
    return render(request, 'index.html',{'title':'Home Page'})

def patent_list(request):
    patents = PatentDatabase.objects.all()
    context = {}
    context['title']= 'All Patents'
    context['data'] = patents
    return render(request, 'patent_list.html', context)

def get_patents_queryset(query=None):
    queryset = []
    print(query)
    post = PatentDatabase.objects.filter(Title_of_Invention__icontains=query).distinct()
    print('hello')
    #A set for application number to avoid duplicate entries
    ap_no = set()
    res=[]
    for i in post:
        if i.Application_Number not in ap_no:
            ap_no.add(i.Application_Number)
            res.append(i)
    print(set(res))
    return res

def search(request):
    context = {}
    res=[]
    context['title'] = 'Search Results'
    query = request.GET.get('query')
    context['q'] = query
    if query:
        res = get_patents_queryset(query)
    else:
        queryset = []
    context['queryset'] = res
    return render(request, 'search_res.html', context)