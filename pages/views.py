from django.shortcuts import render

# Create your views here.
def page(request):
    return render(request, "pages/page.html", {
        "title": "Single page",
        "page": "Hello word from App Pages"
    })