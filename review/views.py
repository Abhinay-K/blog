from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import review,novels
from django.views.generic import ListView, DetailView
from .forms import reviewForm

# Create your views here.
#def home(request):
#    all_reviews= review.objects.all()


#    return render(request,'home.html',{'allreview':all_reviews})
class HomeView(ListView):
    #model= review
    queryset = review.objects.order_by('-pk')
    template_name='home.html'

class NovelReviewView(DetailView):
    model= review
    template_name='novel_review.html'

def write_a_review(request):
    form=reviewForm
    if request.method =='POST':
        if request.user.is_authenticated:
            form=reviewForm(request.POST)
            if form.is_valid():
                form.save()
            
            # name= request.POST['name']
            # chapter_no= request.POST['chapter_no']
            # date= request.POST['date']
            # description= request.POST['description']
            # r= review(name=name,chapter_no=chapter_no,date=date,description=description)
            # r.save()
            return redirect('/')
        else:
            return redirect('accounts/login')
    context={'forms':form}
    
    return render(request,'post_review.html',context)