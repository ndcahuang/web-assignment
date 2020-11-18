import urllib.request

def is_destination_reachable():
    try:
        urllib.request.urlopen("http://127.0.0.1:5000/login", timeout=2)
        return True
    except:
        return False
