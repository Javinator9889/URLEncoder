import pip


def install(package):
    pip.main(['install', package])


try:
    import re
except (ImportError, ModuleNotFoundError):
    print("\"re\" module not found. Try to update Python to Python 3.6.1")

try:
    import ujson as json
except (ImportError, ModuleNotFoundError):
    print("\"ujson\" module not found. Trying installation with pip")
    install('ujson')

try:
    from urllib.parse import urlparse
except (ImportError, ModuleNotFoundError):
    print("\"urllib.parse\" module not found. Try to update Python to Python 3.6.1")

try:
    import os.path as path
except (ImportError, ModuleNotFoundError):
    print("\"os & os.path\" modules not found. Try to update Python to Python 3.6.1")

try:
    from urlencode import create_JSON_dict as jsonDict
except (ImportError, ModuleNotFoundError):
    print("Requiered packages (create_JSON_dict.py) were not found. Please, go to main GitHub project and download them\
    \nhttps://github.com/Javinator9889/URLEncoder")

try:
    import requests as rq
except (ImportError, ModuleNotFoundError):
    print("\"requests\" module not found. Trying installation with pip")
    install('requests')


def urlencoder(**kwargs):
    try:
        text = kwargs.get('text')
    except TypeError:
        print("\"text\" requiered. Use \"urlencoder(text=\"something\")\"")
    else:
        try:
            query = re.search("(?P<url>https?://[^\s]+)", text).group("url")
            isurl = True
        except AttributeError:
            try:
                query = re.search("(?P<url>http?://[^\s]+)", text).group("url")
                isurl = True
            except AttributeError:
                try:
                    query = re.search("(?P<url>www?.[^\s]+)", text).group("url")
                    isurl = True
                except AttributeError:
                    query = text
                    isurl = False

    if not path.exists("Encoded-values.json"):
        jsonDict
    dict_encoded = open("Encoded-values.json", 'rb')
    json_data = json.load(dict_encoded)

    if isurl:
        parse_url = urlparse(query)
        if parse_url.scheme is not '':
            first_part = parse_url.scheme + "://" + parse_url.netloc
        else:
            first_part = parse_url.netloc
        putted = False
        rest = parse_url.path
        if parse_url.params is not '':
            rest = rest + ";" + parse_url.params
        if parse_url.query is not '':
            rest = rest + "?" + parse_url.query
        if parse_url.fragment is not '':
            rest = rest + "#" + parse_url.fragment
        characters = list(rest)
        for a in range(0, len(characters)):
            try:
                value = json_data[characters[a]]
            except KeyError:
                value = characters[a]
            if not putted:
                result = first_part + value
                putted = True
            else:
                result = result + value
        r = rq.get(result)
        if result == query:
            info = "Your final encoded-URL was already encoded. No changes has been done"
        elif r.status_code == rq.codes.ok:
            info = "Web-page is responding correctly.\nIt seems that it has a valid protocol for translating the\
 UTF-8 corresponding ASCII-characters into a valid URL-ASCII typography. You probably will not \
 have problems when accessing to it"
        else:
            info = "Web-page returned status \""+str(r.status_code)+"\" so probably it has not a valid protocol for translating\
 UTF-8 corresponding ASCII-characters into valid URL-ASCII typography. Contact the web-page-administrator to inform\
 about this issue"
    else:
        characters = list(query)

        for a in range(0, len(characters)):
            try:
                value = json_data[characters[a]]
            except KeyError:
                value = characters[a]
            if a == 0:
                result = value
            else:
                result = result + value
        info = "Your word \""+query+"\" was translated into \"UTF-8 encoding for ASCII-URLs\" correctly"

    return result, info
