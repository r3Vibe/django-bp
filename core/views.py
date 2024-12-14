from django.utils.safestring import SafeString
from django.shortcuts import render


def dashboard_callback(request, context):
    labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
    data = [65, 59, 80, 81, 56, 55]
    context.update({"data": SafeString(data), "labels": SafeString(labels)})

    return context


def home(request):
    return render(request, "core/home.html")
