import requests
from random import randint
from lxml import html


def ist():
    n = randint(1, 617)
    rec = requests.get(f'https://eku.ru/category/story/?page={str(n)}')
    HtmlTree = html.fromstring(rec.content)
    rec = requests.get('https://eku.ru' + HtmlTree.xpath(f"//div[@class='item-list humor-item']/h3/a/@href")[0])
    HtmlTree = html.fromstring(rec.content)

    zag = HtmlTree.xpath(f"//div[@id='content']/h1/text()")
    zag = [el.encode('ISO-8859-1').decode('UTF-8') for el in zag]
    txt = HtmlTree.xpath(f"//div[@class='text-content']/p/text()")
    txt = [el.encode('ISO-8859-1').decode('UTF-8') + '\n' for el in txt]
    return ''.join(zag) + '\n' + '\n' + ''.join(txt)


def anegdot():
    vr = randint(0, 2)
    if vr == 0:
        num = randint(1, 24)
        response = requests.get(f'https://anekdotov.net/anekdot/index-page-{num}.html')
        HtmlTree = html.fromstring(response.content)
        ls_blocks = HtmlTree.xpath(f"//div[@class ='anekdot']")
        num = randint(0, len(ls_blocks) - 1)
        el = ls_blocks[num].xpath(f"./text()")
        return '\n'.join(el)
    elif vr == 1:
        num = randint(1, 100)
        response = requests.get(f'https://anekdotbar.ru/top-100.html')
        HtmlTree = html.fromstring(response.content)
        el = HtmlTree.xpath(f"//div[@class ='tecst'][{num}]/text()")
        return '\n'.join(el[:-1])
    elif vr == 2:
        response = requests.get(f'https://vse-shutochki.ru/anekdoty-mesaca.php')
        HtmlTree = html.fromstring(response.content)
        ls_blocks = HtmlTree.xpath(f"//div[@class ='post']")
        ls_blocks = ls_blocks[1:-5]
        num = randint(0, len(ls_blocks) - 1)
        el = ls_blocks[num].xpath(f"./text()")
        return '\n'.join(el[:-2])


if __name__ == '__main__':
    print(anegdot())
