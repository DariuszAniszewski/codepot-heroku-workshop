import os
from time import sleep
import sys

from django.conf import settings
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


def save_file(request):
    file_name = "dummy-file.txt"
    file_path = os.path.join(settings.BASE_DIR, file_name)
    file_existed = os.path.exists(file_path)
    file_content = "Lorem ipsum"
    file = open(file_path, "w")
    file.write(file_content)
    file.close()
    file_exists_after = os.path.exists(file_path)

    data = {
        "file_existed": file_existed,
        "file_exists_after": file_exists_after,
        "file_path": file_path,
        "file_content": file_content,
    }
    return render(request, "save-file.html", data)


def read_file(request):
    file_name = "dummy-file.txt"
    file_path = os.path.join(settings.BASE_DIR, file_name)
    file_exists = os.path.exists(file_path)
    file_content = None
    if file_exists:
        file = open(file_path, "r")
        file_content = file.read()
        file.close()

    data = {
        "file_exists": file_exists,
        "file_path": file_path,
        "file_content": file_content,
    }
    return render(request, "read-file.html", data)


def python_version(request):
    data = {
        "version": sys.version.split(" ")[0]
    }
    return render(request, "version.html", data)


def memory(request, megs):
    print("Allocating {}MB of RAM".format(megs))
    dummy = ' ' * int(megs) * 1024 * 1014
    print("Waiting 15seconds so Heroku can notice this")
    sleep(15)
    data = {
        "megs": megs,
    }
    return render(request, "memory.html", data)


def slow_response(request, seconds):
    for i in range(1, int(seconds) + 1):
        sleep(1)
        print("{}s...".format(i))
    print("OK, enough")
    data = {
        "seconds": seconds,
    }
    return render(request, "slow-response.html", data)


def crash_me(request):
    error = 10 / 0
