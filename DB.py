import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","DNbookproject.settings")
import django
django.setup()
from bookmap.models import BookStore, Crawling

if __name__ == '__main__':
    name=[]
    addr=[]
    insta=[]
    site=[]
    email=[]
    phone_number=[]
    openhour=[]
    saup=[]
    img=[]

    with open('bookDB.txt',"r",encoding='UTF8') as f:
        while True:
            line=f.readline()
            if not line : break
            line=line[:-1]
            a=line.split('\t')
            name.append(a[0])
            addr.append(a[1])
            insta.append(a[2])
            site.append(a[3])
            email.append(a[4])
            phone_number.append(a[5])
            a[6]=a[6].replace(';','\n')
            openhour.append(a[6])
            saup.append(a[7])
            img.append(a[8])

    for i in range(len(name)):
        BookStore.objects.create(
        name=name[i],
        addr=addr[i],
        insta=insta[i],
        site=site[i],
        email=email[i],
        phone_number=phone_number[i],
        openhour=openhour[i],
        saup=saup[i],)
        img='store/' + img[i])
        
    store = []
    title = []
    content = []
    link = []

    with open('crawling.txt',"r",encoding='UTF8') as f:
        while True:
            line=f.readline()
            if not line : break
            line=line[:-1]
            a = line.split('\t')
            store.append(a[0])
            title.append(a[1])
            content.append(a[2])
            link.append(a[3])

    for i in range(len(link)):
        s = BookStore.objects.get(name=store[i])
        Crawling.objects.create(
            store=s,
            title=title[i],
            content=content[i],
            link=link[i]
        )