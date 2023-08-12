from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.views.generic import View

class FeedbackView(View):
    def post(self, request):
        if request.method == "POST":
            form = FeedbackForm(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = FeedbackForm()
        return redirect("/")