from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
root=Path(__file__).resolve().parents[1]/'web/dist';base='/misa-python-workshop/'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set()
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  if tag=='a' and 'href' in a:self.links.append(a['href'])
cache={}
for file in root.rglob('*.html'):
 page=Page();page.feed(file.read_text());cache[file.resolve()]=page
from urllib.parse import urljoin
errors=[];checked=0
for file,page in cache.items():
 url='http://localhost'+base+str(file.relative_to(root.resolve())).removesuffix('index.html')
 for href in page.links:
  target=urlsplit(urljoin(url,href))
  if target.netloc!='localhost':continue
  if not target.path.startswith(base):errors.append((str(file),href,'outside base'));continue
  local=root/unquote(target.path[len(base):]);local=local/'index.html' if local.is_dir() else local
  if not local.exists():errors.append((str(file),href,'missing'));continue
  if target.fragment and local.resolve() in cache and unquote(target.fragment) not in cache[local.resolve()].ids:errors.append((str(file),href,'missing anchor'))
  checked+=1
print('Checked',checked,'internal links and anchors across',len(cache),'pages')
for err in errors:print(err)
assert not errors
