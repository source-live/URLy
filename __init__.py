import os




__version__ = "0.01-dev"
#
source = ""
f = ""

c_WEB_NAME = ""
c_PAGE_NAME = ""
c_PAGE_ALIAS = ""

ext = open(".ext","r")


class lavla:
  _web_name = c_WEB_NAME
  _page_name = c_PAGE_NAME
  _page_alias = c_PAGE_ALIAS
  _vers = __version__
  
  def __init__(_n,_pn,_pa)
    c_WEB_NAME = _n
    _web_name = c_WEB_NAME
    
    c_PAGE_NAME = _pn
    _page_name = c_PAGE_NAME
    
    c_PAGE_ALIAS = _pa
    _page_alias = c_PAGE_ALIAS
  
  def local(name,pre):
    name = "".join([name,ext])
    
    for n = pre:
      n = n.format(nm=_webname)
    
    f = open(path,"a")
    if f == None:
      print("Please add source.")
      
    f.write(f.format(*pre))
    
    def new(name,path,pre):
    name = "".join([name,ext])
    
    for n = pre:
      n = n.format(nm=_webname)
    
    path = "/".join(path)
    path = os.path.join(path,name)
    if not os.path.exists(path):
      os.makedirs(path)
    f = open(path,"a")
    if f == None:
      if source == None:
        print("Please add source.")
      else:
        f.write(source)
      
    f.write(f.format(*pre))
      
  def source(data)
    source = data
  
  def setup(_n,_pn,_pa)
    c_PAGE_NAME = _pn
    _page_name = c_PAGE_NAME
    
    c_PAGE_ALIAS = _pa
    _page_alias = c_PAGE_ALIAS
