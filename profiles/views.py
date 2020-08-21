from django.shortcuts import render


def profile(request):
    template = "profiles/profile.html"
    context = {}

    return(request, template, context)