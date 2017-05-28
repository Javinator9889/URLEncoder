# URL Encoder
Public lib for encoding text and URLs into valid ASCII charset for web-browsing

**Basically**: `España -> Espa%C3%B1a` 

*and also with URLs*: `http://google.es/search?q=España la vieja -> http://google.es/search?q=Espa%C3%B1a%20la%20vieja`


## Installation
* You can use `pip install URLEncoder` for easy installation
* Although, you can **download this git** and run __setup.py__ with `python setup.py install`

Go to the PyPi page: [URLEncoder on PyPi](https://pypi.python.org/pypi?name=URLEncoder&:action=display)

## Usage
When you have **downloaded** this library, for using it the easiest way is:

```javascript
import urlencode as ude

input_text = "WHAT_YOU_WANT_TO_ENCODE"
# You have to complete the filed 'text' with a simple text (for example: España) or with
# an URL (http://google.com/search?q=España suiza)

results = ude.urlencoder(text=input_text)

# The function returns a tuple, being the first value the encoded string and the second one, 
# info about web-page (if it is going to work, etc)

encoded_str = results[0]
info = results[1]

print("Encoded:", encoded_str, "\n\nINFO:", info)

# If text was: input_text = "España"
# encoded_str --> Espa%C3%B1a
# info --> Your word "España" was translated into "UTF-8 encoding for ASCII-URLs" correctly

# If text was: input_text = "http://google.com/search?q=España suiza"
# encoded_str --> http://google.com/search?q=Espa%C3%B1a%20suiza
# info --> Web-page is responding correctly.
#          It seems that it has a valid protocol for translating the UTF-8 corresponding ASCII-characters into a valid
#          URL-ASCII typography. You probably will not have problems when accessing to it
```
Nowadays, URLEncoder can transform every **single text** to a compatible **URL with ASCII values**. It also has a checker in order to know if the obtained URL *is going to work* as the original URL

## ¿Is public?

Of course, this took me a bit of my time 😉 but you can **completely use it for free** as well as all the main program such as the *dictionary of special characters*.

The **only requirement** is to mention me and *include a particular message in all distributions* (for more information, check **License** in the following lines)

## License
URLEncoder -- Public lib for encoding text and URLs into valid ASCII charset for web-browsing - Copyright (C) 2017 Javinator9889

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

For contacting, go to "https://github.com/Javinator9889/URLEncoder/issues" and type your message. Also you can go to my GitHub profile and send me direct message.
