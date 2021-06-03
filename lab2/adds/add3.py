import re

def check_validity(regex, object ,string):
    if re.search(regex, object):
        print(f"Valid {string}")
    else:
        print(f"Invalid {string}")

def check_email():
    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    email = input("Enter email: ")
    check_validity(regex, email, "email")

def check_float():
    regex = "^[+-]?[0-9]+[.,][0-9]+$"
    number = input("Enter float number: ")
    check_validity(regex, number, "float number")

def url_parts(url):
    regex = re.compile(
        r"^"
        r"((?P<schema>.+?)://)?"
        r"(?P<host>.*?)"
        r"(:(?P<port>\d+?))?"
        r"(?P<path>/.*?)?"
        r"(?P<parameters>[?].*?)?"
        r"$"
    )

    for key, value in regex.match(url).groupdict().items():
        print(f"{key}: {value}")


check_email()
check_float()
url_parts("http://example.com:80/path/to/file.html?key1=value1&key2=value2")
    