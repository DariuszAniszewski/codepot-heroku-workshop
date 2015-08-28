from django.shortcuts import render


def home(request):
    data = {

    }
    return render(request, "index.html", data)


def log(request):
    for i in range(2000):
        print("Dummy log line #{}".format(i))
        if i == 200:
            print("WOW THIS IS SUPER IMPORTANT LINE WITH ERROR")
    return render(request, "logs.html")