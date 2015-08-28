#!/usr/bin/env python
import os
import sys
from time import sleep

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codepot_app.settings")

    from django.core.management import execute_from_command_line

    print("Waiting 80 seconds to boot for some reason")
    for i in range(1, 80):
        sleep(1)
        print("{}s...".format(i))
        if i == 54:
            print("It will crash soon :(")

    execute_from_command_line(sys.argv)