from requests import get,post

r = get('http://repubblica.it')
#print(r.text)
text = r.text.splitlines()
for i,l in enumerate(text):
    l = l.strip()
    if l == '<h2 class="entry__title">':
        title = text[i+2].strip()
        if len(title) > 0:
            print(title)