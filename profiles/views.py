from django.http import Http404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib import messages
# from books.forms import ProfileForm
from .models import Profile
from .models import User
from django.urls import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def profile_page(request):
    profile_form =ProfileForm(request.POST or None, request.FILES or None)
    context = { "form": profile_form}
    if profile_form.is_valid():
        #store_image = profile_form.cleaned_data["image"]
        store_name = profile_form.cleaned_data.get("name")
        store_home_addr = profile_form.cleaned_data.get("home_addr")
        store_nick_name = profile_form.cleaned_data.get("nick_name")
        new_profile = Profile(name=store_name, home_addr=store_home_addr, nick_name=store_nick_name)
        new_profile.save()
        np_was_set = True

        if np_was_set is not None:
        #if User.profile.nick_name is not None:
            # Redirect to a success page.
            return redirect("{{ Profile.slug }}")
        else:
            # Return an 'invalid' error message.
            print("Error")

    return render(request, "profiles/create.html", context)

# @login_required
# def CreateProfile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.Post, instance= request.user.profile)
#         if form.is_valid():
#             form.save()
#             context = {'Your profile was successfully updated!'}
#             return render(request, "profiles/view.html", context)
#         else:
#             context = {'Please correct the error below.'}
#             return render(request, "profiles/view.html", context)
#     else:
#         try:
#             form = ProfileForm(instance=request.user.profile)
#             args = {}
#             args.update(request)
#
#             args['form'] = form
#         except ObjectDoesNotExist:
#             True
#
#     return render_to_response('profiles/view.html')

class ProfileDetailSlugView(DetailView):
    queryset = Profile.profile_obj.all()
    template_name = "profiles/view.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug= self.kwargs.get('slug')

        try:
            instance = Profile.profile_obj.get(slug=slug)
        except Profile.DoesNotExist:
            raise Http404("Not found ...")
        except Profile.MultipleObjectsReturned:
            qs = Profile.profile_obj.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Something unexpected happened :(")
        return instance

class ProfileDetailView(DetailView):
    template_name = "profiles/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk= self.kwargs.get('pk')
        instance = Profile.profile_obj.get_by_id(pk)
        if instance is None:
            raise Http404("Profile does not exist")
        return instance

def profile_detail_view(request, pk=None, *args, **kwargs):

	instance = Profile.profile_obj.get_by_id(pk)
	if instance is None:
		raise Http404("Profile does not exist")

	context = {
		'object': instance
	}
	return render(request, "profiles/view.html", context)

# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             context = {'Your profile was successfully updated!'}
#             return render(request, "profiles/view.html", context)
#
#         else:
#             context = {'Please correct the error below.'}
#             return render(request, "profiles/view.html", context)
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/view.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })
