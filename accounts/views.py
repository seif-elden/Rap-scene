from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth import login as auth_login
from .forms import SignUpForm , f_community_post , f_comments
from .models import community_post , comments
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView , CreateView
from django.urls import reverse_lazy
# Create your views here.

class signup_CLASSBASED(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('rapper:home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            auth_login(self.request, user)
        return super(signup_CLASSBASED ,self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('rapper:home')
        return super(signup_CLASSBASED ,self).get(*args, **kwargs)


# def signup_FUNCTIONBASED(request):
#     # MAKE SURE THAT LOGED IN USERS CANNOT SIGN UP AGAIN
#     if  request.user.is_authenticated:
#         return redirect("rapper:home")
#     # IF USER NOT authenticated
#     else :
#         form = SignUpForm()
#         if request.method =='POST':
#             form = SignUpForm(request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 auth_login(request,user)

#                 return redirect('rapper:home')

#         return render(request,'signup.html',{'form':form})


class community_CLASSBASED(CreateView):
    form_class = f_community_post
    template_name = 'community.html'
    success_url = reverse_lazy('accounts:community')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.created_by = self.request.user
        return super(community_CLASSBASED, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(community_CLASSBASED,self).get_context_data(**kwargs)
        context['posts'] = community_post.objects.filter(visable=True).order_by("-created_dt")
        return context


# def community_FUNCTIONBASED(request):

#     if request.method == "POST" and request.user.is_authenticated :
#         form = f_community_post(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.created_by = request.user
#             post.save()

#     form = f_community_post()
#     posts = community_post.objects.filter(visable=True).order_by("-created_dt")
            
#     return render(request,"community.html",{"form":form,"posts":posts})








@login_required
def s_post(request,pk):
    post = get_object_or_404(community_post,pk=pk,visable=True)
    if request.method =='POST' :
        if "del-com" in request.POST:
            x = get_object_or_404(comments,pk=request.POST["del-com"])
            if request.user == x.created_by :
                x.delete()
        elif "del-post" in request.POST:
            x = get_object_or_404(community_post,pk=request.POST["del-post"])
            if request.user == x.created_by :
                x.delete()
                return redirect("accounts:community")
        else :
            form=f_comments(request.POST)
            if form.is_valid():
                comment = form.save(commit=False) 
                comment.created_by = request.user
                comment.community_post = post
                comment.save()
    comment = comments.objects.filter(community_post=post)
    form = f_comments()
    
    return render(request,"s_post.html",{"post":post,"comment":comment,"form":form})