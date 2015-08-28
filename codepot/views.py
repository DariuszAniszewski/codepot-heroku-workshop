from time import sleep
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


def timeout(request):
    print("Starting timeout request")
    for i in range(1, 10):
        sleep(1)
        print("{}s...".format(i))
    sleep(1)
    print("10 seconds already, and waiting")
    for i in range(11, 20):
        sleep(1)
        print("{}s...".format(i))
    sleep(1)
    print("20 seconds...")
    for i in range(21, 28):
        sleep(1)
        print("{}s...".format(i))
    sleep(1)
    print("28 seconds...")
    print("Heroku will raise H12 error soon")
    for i in range(29, 40):
        sleep(1)
        print("{}s...".format(i))
    print("Heroku timeouted a while ago...")
    for i in range(41, 62):
        sleep(1)
        print("{}s...".format(i))
    print("WOW, Heroku returned H12 error like 30 seconds ago, but I'm still alive")
    return render(request, "timeout.html")