from django.shortcuts import render
from django.db.models import Q
from .models import Team_Member , rapper  , article 
from .forms import f_ad


from django.views.generic import DetailView ,ListView , FormView
from django.urls import reverse_lazy

import smtplib
# Create your views here.

#help function that alert admin if some one send ad 
def mail():
    fromaddr = 'your-email@gmail.com'
    toaddrs  = 'admin-email@gmail.com'
    msg = "some one send you ad message "
    username = 'your-email@gmail.com'
    password = 'your password'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()



class home_CLASSBASED(FormView):
    form_class = f_ad 
    template_name = 'home.html'
    success_url = reverse_lazy('rapper:home')

    def form_valid(self, form):
        form.save()
        mail()
        return super(home_CLASSBASED , self).form_valid(form)


# def home_FUNCTIONBASED(request):
#     if request.method == "POST" :
#         form = f_ad(request.POST)
#         if form.is_valid():
#             print("mail sent")
#             form.save()
#             mail()

#     form = f_ad()
#     return render(request,"home.html",{"form":form})




class meet_CLASSBASED(ListView):
    model = Team_Member
    template_name = 'meet.html'
    context_object_name = 'our_team'

# def meet_FUNCTIONBASED(request):
#     our_team = Team_Member.objects.all()
#     return render(request,"meet.html",{"our_team":our_team})
 



class search_CLASSBASED(ListView):
    model = rapper
    template_name = 'search.html'
    context_object_name = 'result'

    def get_queryset(self):
        q = self.request.GET["query"]
        result = None
        if q:
            result = self.model.objects.filter(Q(name__contains=q) |Q(about_him__contains =q)|Q(nickname__contains =q))
        return result



# def search_FUNCTIONBASED(request):    
#     result = None
#     try :
#         q = request.GET["query"]
#         if q :
#             result = rapper.objects.filter(Q(name__contains=q) |Q(about_him__contains =q)|Q(nickname__contains =q))
#     except :
#         pass

#     return render(request,"search.html",{"result":result})

  



class v_rapper_CLASSBASED(DetailView):
    model = rapper
    template_name = "v_rapper.html"
    context_object_name = 'result' 


    def get_context_data(self, **kwargs):
        context = super(v_rapper_CLASSBASED,self).get_context_data(**kwargs)
        context['result_articals'] = article.objects.filter(rapper=self.kwargs["pk"])
        return context


# def v_rapper_FUNCTIONBASED(request,pk):
#     result = rapper.objects.get(pk=pk)
#     result_articals = article.objects.filter(rapper=pk)
#     return render(request,"v_rapper.html",{"result":result,"result_articals":result_articals})





class v_article_CLASSBASED(DetailView):
    model = article
    template_name = "v_article.html"
    context_object_name = 'result_articals' 


# def v_article_FUNCTIONBASED(request,pk):
#     result_articals = article.objects.get(pk=pk)
#     return render(request,"v_article.html",{"result_articals":result_articals})
