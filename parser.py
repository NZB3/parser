import requests
from bs4 import BeautifulSoup

URL = 'https://www.avito.ru/moskva/odezhda_obuv_aksessuary/obuv-muzhskaya/43-ASgBAQICAkTeAtgL4ALiCwFAxAEUxAU?cd=1&f=ASgBAQICAkTeAtgL4ALiCwJAxAEUxAXivA0U8NE0&q=%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0', 'accept': '*/*'}
TAIL = 'https://www.avito.ru'

def get_html(url, params=None):
	r = requests.get(url, headers=HEADERS, params=params)
	return r


def get_content(html):
	soup = BeautifulSoup(html, 'html.parser')
	items = soup.find_all('div', class_ = 'iva-item-root-Nj_hb photo-slider-slider-_PvpN iva-item-list-H_dpX iva-item-redesign-nV4C4 iva-item-responsive-gIKjW iva-item-xl-Fkrdv items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')

	content = []
	for item in items:
		content.append({
			'link':TAIL + item.find('a', class_ = 'link-link-MbQDP link-design-default-_nSbv title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes').get('href'),
			'title':item.find('h3', class_ = 'title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes text-text-LurtD text-size-s-BxGpL text-bold-SinUO').get_text(strip = True),
			'cost':item.find('span', class_ = 'price-text-E1Y7h text-text-LurtD text-size-s-BxGpL').get_text(strip = True),
			'station':item.find('div', class_ = 'geo-georeferences-Yd_m5 text-text-LurtD text-size-s-BxGpL').get_text(strip = True)
			})
	return content


def parser():
	html = get_html(URL)
	print(html.status_code)
	print(str(get_content(html.text))+'\n\n')


parser()