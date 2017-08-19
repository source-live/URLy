from lavla import *
from shutil import *

shorten = lavla("redirect","redirect","Redirect")

class URLy:
  def __init__(url="",id=""):
    shorten.local("/temp/index",[url])
    shutil.copy2('/temp/index.html', ''.join(['/',id]))
    shorten.local(''.join(['/',id,'index']))
    print('URL:' + url + ' redirected to /' + id + '/ in your website\'s root directory.')
