import asyncio
from random import randint
import aiohttp
from bs4 import BeautifulSoup
from lxml import html


async def ist(n):
    # n = randint(1, 617)
    async with aiohttp.ClientSession() as session:
        rec = await session.get(f'https://eku.ru/category/story/?page={str(n)}')
        soup = BeautifulSoup(await rec.text(), "html.parser")
    HtmlTree = html.fromstring(str(soup))
    async with aiohttp.ClientSession() as session:
        rec = await session.get('https://eku.ru' + HtmlTree.xpath(f"//div[@class='item-list humor-item']/h3/a/@href")[0])
        soup = BeautifulSoup(await rec.text(), "html.parser")
    HtmlTree = html.fromstring(str(soup))

    zag = HtmlTree.xpath(f"//div[@id='content']/h1/text()")
    # zag = [el.encode('ISO-8859-1').decode('UTF-8') for el in zag]
    txt = HtmlTree.xpath(f"//div[@class='text-content']/p/text()")
    # txt = [el.encode('ISO-8859-1').decode('UTF-8') + '\n' for el in txt]
    return ''.join(zag) + '\n' + '\n' + ''.join(txt)


# def anegdot():
#     vr = randint(0, 1)
#     if vr == 0:
#         num = randint(2, 194)
#         response = requests.get(f'https://anekdotov.net/anekdot/one/random{num}.html')
#         HtmlTree = html.fromstring(response.content)
#         el = HtmlTree.xpath(f"//a[@href='/anekdot/one/random{num - 1}.html']/text()")
#         return '\n'.join(el[:-2])
#     else:
#         num = randint(1, 100)
#         response = requests.get(f'https://anekdotbar.ru/top-100.html')
#         HtmlTree = html.fromstring(response.content)
#         el = HtmlTree.xpath(f"//div[@class ='tecst'][{num}]/text()")
#         return '\n'.join(el[:-1])


async def main():
    ls = [randint(1, 617) for _ in range(30)]
    ls_coroutines = [ist(n) for n in ls]
    for cor in asyncio.as_completed(ls_coroutines):
        cor_result = await cor
        print(cor_result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
