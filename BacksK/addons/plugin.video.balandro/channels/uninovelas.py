# -*- coding: utf-8 -*-

import re

from platformcode import config, logger, platformtools
from core.item import Item
from core import httptools, scrapertools, servertools, tmdb


host = 'https://ennovelas.lat/'


def do_downloadpage(url, post=None, headers=None):
    # ~ por si viene de enlaces guardados
    ant_hosts = ['https://ennovelas.cc/']

    for ant in ant_hosts:
        url = url.replace(ant, host)

    resp = httptools.downloadpage(url, post=post, headers=headers)

    if resp.sucess: data = resp.data
    else: data = ''

    return data


def mainlist(item):
    return mainlist_series(item)


def mainlist_series(item):
    logger.info()
    itemlist = []

    itemlist.append(item.clone( title = 'Buscar serie ...', action = 'search', search_type = 'tvshow', text_color = 'hotpink' ))

    itemlist.append(item.clone( title = 'Catálogo', action = 'list_all', url = host + 'drama/', search_type = 'tvshow' ))

    itemlist.append(item.clone( title = 'Episodios', action = 'list_epis', url = host, search_type = 'tvshow' ))

    return itemlist


def list_all(item):
    logger.info()
    itemlist = []

    data = do_downloadpage(item.url)
    data = re.sub(r"\n|\r|\t|&nbsp;|<br>|<br/>", "", data)

    matches = re.compile('<li>(.*?)</li>').findall(data)

    for match in matches:
        url = scrapertools.find_single_match(match, '<a href="(.*?)"')

        title = scrapertools.find_single_match(match, 'title="(.*?)"').strip()

        if not url or not title: continue

        title = title.replace('&#8211;', '').strip()

        title = title.replace('Capitulo Completo', '').replace('Capitulos', '').replace('Completos', '').replace('Completo', '').strip()

        year = scrapertools.find_single_match(title, '(\d{4})')
        if not year: year = '-'
        else:
           title = title.replace('(' + year + ')', '').strip()

        url = host[:-1] + url

        SerieName = title

        if 'Temporada' in SerieName: SerieName = SerieName.split("Temporada")[0]
        if 'temporada' in SerieName: SerieName = SerieName.split("temporada")[0]

        if '(en Español)' in SerieName: SerieName = SerieName.split("(en Español)")[0]
        if 'En ESPAÑOL' in SerieName: SerieName = SerieName.split("En ESPAÑOL")[0]
        if 'En Español' in SerieName: SerieName = SerieName.split("En Español")[0]
        if 'en Español' in SerieName: SerieName = SerieName.split("en Español")[0]
        if 'en espnol' in SerieName: SerieName = SerieName.split("en espnol")[0]
        if 'español' in SerieName: SerieName = SerieName.split("español")[0]

        if 'onlline' in SerieName: SerieName = SerieName.split("onlline")[0]
        if 'online' in SerieName: SerieName = SerieName.split("online")[0]
        if 'ennovelas.ws' in SerieName: SerieName = SerieName.split("ennovelas.ws")[0]

        if 'HD' in SerieName: SerieName = SerieName.split("HD")[0]
        if 'Hd' in SerieName: SerieName = SerieName.split("Hd")[0]
        if 'hd' in SerieName: SerieName = SerieName.split("hd")[0]

        SerieName = SerieName.strip()

        title = title.replace('Temporada', '[COLOR goldenrod]Temp.[/COLOR]')

        itemlist.append(item.clone( action='temporadas', url = url, title = title,
                                    contentType = 'tvshow', contentSerieName = SerieName, infoLabels={'year': year} ))

    tmdb.set_infoLabels(itemlist)

    if itemlist:
        next_page = scrapertools.find_single_match(data, '<link rel="next".*?href="(.*?)"')

        if next_page:
            if '/page/' in next_page:
                itemlist.append(item.clone( title = 'Siguientes ...', url = next_page, action = 'list_all', text_color = 'coral' ))

    return itemlist


def list_epis(item):
    logger.info()
    itemlist = []

    data = do_downloadpage(item.url)
    data = re.sub(r"\n|\r|\t|&nbsp;|<br>|<br/>", "", data)

    title_ser = item.contentSerieName.replace("’s", 's').replace("'t", 't').replace(':', '').replace("'t", 't').replace('ñ', 'n')

    title_ser = title_ser.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
    title_ser = title_ser.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace(' ', '-').lower()

    title_ser = title_ser.replace('(', '').replace(')', '').strip()

    title_ser = title_ser.replace('&#8217;', '').replace('&#8220;', '').replace('&#8221;', '').replace('&amp;', '').replace('amp;', '').replace('quot;', '').strip()

    matches = re.compile('<li class="SUB">(.*?)</li>').findall(data)

    for match in matches:
        url = scrapertools.find_single_match(match, '<a href="(.*?)"')

        title = scrapertools.find_single_match(match, 'title="(.*?)"').strip()

        if not url or not title: continue

        title = title.replace('&#8211;', '').strip()

        title = title.replace('Capitulo Completo', '').replace('Capitulos', '').replace('Completos', '').replace('Completo', '').replace('HD', '').strip()

        year = scrapertools.find_single_match(title, '(\d{4})')
        if not year: year = '-'
        else:
           title = title.replace('(' + year + ')', '').strip()

        SerieName = title

        if 'Sub Español' in SerieName: SerieName = SerieName.split("Sub Español")[0]

        if 'Capitulo' in SerieName: SerieName = SerieName.split("Capitulo")[0]
        if 'Capítulo' in SerieName: SerieName = SerieName.split("Capítulo")[0]
        if 'capitulo' in SerieName: SerieName = SerieName.split("capitulo")[0]
        if 'capítulo' in SerieName: SerieName = SerieName.split("capítulo")[0]

        if 'Temporada' in SerieName: SerieName = SerieName.split("Temporada")[0]
        if 'temporada' in SerieName: SerieName = SerieName.split("temporada")[0]

        if '(en Español)' in SerieName: SerieName = SerieName.split("(en Español)")[0]
        if 'En ESPAÑOL' in SerieName: SerieName = SerieName.split("En ESPAÑOL")[0]
        if 'En Español' in SerieName: SerieName = SerieName.split("En Español")[0]
        if 'en Español' in SerieName: SerieName = SerieName.split("en Español")[0]
        if 'en espnol' in SerieName: SerieName = SerieName.split("en espnol")[0]
        if 'español' in SerieName: SerieName = SerieName.split("español")[0]

        if 'onlline' in SerieName: SerieName = SerieName.split("onlline")[0]
        if 'online' in SerieName: SerieName = SerieName.split("online")[0]
        if 'ennovelas.ws' in SerieName: SerieName = SerieName.split("ennovelas.ws")[0]

        if 'HD' in SerieName: SerieName = SerieName.split("HD")[0]
        if 'Hd' in SerieName: SerieName = SerieName.split("Hd")[0]
        if 'hd' in SerieName: SerieName = SerieName.split("hd")[0]

        SerieName = SerieName.strip()

        thumb = scrapertools.find_single_match(match, ' src="(.*?)"')

        title = title.replace('Temporada', '[COLOR tan]Temp.[/COLOR]')

        title = title.replace('Capitulo', '[COLOR goldenrod]Epis.[/COLOR]').replace('Capítulo', '[COLOR goldenrod]Epis.[/COLOR]')

        url = host[:-1] + url

        itemlist.append(item.clone( action='temporadas', url=url, title=title, thumbnail=thumb,
                                    contentType = 'tvshow', contentSerieName = SerieName, infoLabels={'year': year} ))

    tmdb.set_infoLabels(itemlist)

    if itemlist:
        next_page = scrapertools.find_single_match(data, '<link rel="next".*?href="(.*?)"')

        if next_page:
            if '/page/' in next_page:
                itemlist.append(item.clone( title = 'Siguientes ...', url = next_page, action = 'list_epis', text_color = 'coral' ))

    return itemlist


def temporadas(item):
    logger.info()
    itemlist = []

    if config.get_setting('channels_seasons', default=True):
        platformtools.dialog_notification(item.contentSerieName.replace('&#038;', '&').replace('&#8217;', "'"),'[COLOR tan]Sin temporadas[/COLOR]')

    item.contentType = 'season'

    season = 1
    if '-temporada-' in item.url:
        season = scrapertools.find_single_match(item.url, '-temporada-(.*?)-')
        if not season: season = scrapertools.find_single_match(item.url, '-temporada-(.*?)/')

    item.contentSeason = season
    item.page = 0

    title_ser = item.contentSerieName.replace("’s", 's').replace("'t", 't').replace(':', '').replace("'t", 't').replace('ñ', 'n')

    title_ser = title_ser.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
    title_ser = title_ser.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace(' ', '-').lower()

    title_ser = title_ser.replace('(', '').replace(')', '').strip()

    title_ser = title_ser.replace('&#8217;', '').replace('&#8220;', '').replace('&#8221;', '').replace('&amp;', '').replace('amp;', '').replace('quot;', '').strip()

    if '-temporada-' in item.url: 
        temporada = scrapertools.find_single_match(item.url, '-temporada-(.*?)-')
        if temporada:
            title_ser = title_ser + '-temporada-' + temporada

    url = host + title_ser + '/'

    SerieName = title_ser.replace('-', ' ').capitalize()

    itemlist.append(item.clone( action='episodios', url=url, title='[COLOR hotpink]Serie[/COLOR] ' + title_ser.replace('-', ' ').capitalize(),
                                        serie = True, page = 0,
                                        contentType = 'tvshow', contentSerieName = SerieName, contentSeason = season ))

    itemlist2 = episodios(item)

    itemlist = itemlist + itemlist2

    return itemlist


def episodios(item):
    logger.info()
    itemlist = []

    matches = []

    if not item.page: item.page = 0
    if not item.perpage: item.perpage = 50

    data = do_downloadpage(item.url)
    data = re.sub(r"\n|\r|\t|&nbsp;|<br>|<br/>", "", data)

    if not data: return itemlist

    hay_match = False

    match = scrapertools.find_single_match(data, '<link rel="canonical" href="(.*?)"')

    if item.serie:
        match = ''

        bloque = scrapertools.find_single_match(data, '>Show All Episodes<(.*?)</ul>')

        matches = re.compile('<li(.*?)</li>', re.DOTALL).findall(bloque)

    if match:
        if '-capitulo-' in match:
            hay_match = True

            epis = scrapertools.find_single_match(match, '-capitulo-(.*?)-')
            if not epis: epis = 1

            itemlist.append(item.clone( action='findvideos', url = match, title = item.title,
                                        contentType = 'episode', contentSeason = 1, contentEpisodeNumber=epis ))

    else:
        if not matches:
            bloque = scrapertools.find_single_match(data, '>Show All Episodes<(.*?)</ul>')

            matches = re.compile('<li(.*?)</li>', re.DOTALL).findall(bloque)

        if not matches:
            season = item.contentSeason
            if '-temporada-' in item.url: season = scrapertools.find_single_match(item.url, '-temporada-(.*?)/')

            epis = scrapertools.find_single_match(item.url, '-capitulo-(.*?)/')
            if not epis: epis = scrapertools.find_single_match(item.url, '-capitulo-(.*?)-')

            if not epis: epis = 1

            itemlist.append(item.clone( action='findvideos', url=item.url, title=item.title,
                                        contentType = 'episode', contentSeason = season, contentEpisodeNumber=epis ))

            tmdb.set_infoLabels(itemlist)

            return itemlist

    if item.page == 0 and item.perpage == 50:
        sum_parts = len(matches)

        try:
            tvdb_id = scrapertools.find_single_match(str(item), "'tvdb_id': '(.*?)'")
            if not tvdb_id: tvdb_id = scrapertools.find_single_match(str(item), "'tmdb_id': '(.*?)'")
        except: tvdb_id = ''

        if config.get_setting('channels_charges', default=True):
            item.perpage = sum_parts
            if sum_parts >= 100:
                platformtools.dialog_notification('UniNovelas', '[COLOR cyan]Cargando ' + str(sum_parts) + ' elementos[/COLOR]')
        elif tvdb_id:
            if sum_parts > 50:
                platformtools.dialog_notification('UniNovelas', '[COLOR cyan]Cargando Todos los elementos[/COLOR]')
                item.perpage = sum_parts
        else:
            if sum_parts >= 1000:
                if platformtools.dialog_yesno(item.contentSerieName.replace('&#038;', '&').replace('&#8217;', "'"), '¿ Hay [COLOR yellow][B]' + str(sum_parts) + '[/B][/COLOR] elementos disponibles, desea cargarlos en bloques de [COLOR cyan][B]500[/B][/COLOR] elementos ?'):
                    platformtools.dialog_notification('UniNovelas', '[COLOR cyan]Cargando 500 elementos[/COLOR]')
                    item.perpage = 500

            elif sum_parts >= 500:
                if platformtools.dialog_yesno(item.contentSerieName.replace('&#038;', '&').replace('&#8217;', "'"), '¿ Hay [COLOR yellow][B]' + str(sum_parts) + '[/B][/COLOR] elementos disponibles, desea cargarlos en bloques de [COLOR cyan][B]250[/B][/COLOR] elementos ?'):
                    platformtools.dialog_notification('UniNovelas', '[COLOR cyan]Cargando 250 elementos[/COLOR]')
                    item.perpage = 250

            elif sum_parts > 250:
                if platformtools.dialog_yesno(item.contentSerieName.replace('&#038;', '&').replace('&#8217;', "'"), '¿ Hay [COLOR yellow][B]' + str(sum_parts) + '[/B][/COLOR] elementos disponibles, desea cargarlos en bloques de [COLOR cyan][B]250[/B][/COLOR] elementos?'):
                    platformtools.dialog_notification('UniNovelas', '[COLOR cyan]Cargando elementos[/COLOR]')
                    item.perpage = 250

            elif sum_parts >= 125:
                if platformtools.dialog_yesno(item.contentSerieName.replace('&#038;', '&').replace('&#8217;', "'"), '¿ Hay [COLOR yellow][B]' + str(sum_parts) + '[/B][/COLOR] elementos disponibles, desea cargarlos en bloques de [COLOR cyan][B]75[/B][/COLOR] elementos ?'):
                    platformtools.dialog_notification('UniNovelas', '[COLOR cyan]Cargando 75 elementos[/COLOR]')
                    item.perpage = 75

            elif sum_parts > 50:
                if platformtools.dialog_yesno(item.contentSerieName.replace('&#038;', '&').replace('&#8217;', "'"), '¿ Hay [COLOR yellow][B]' + str(sum_parts) + '[/B][/COLOR] elementos disponibles, desea cargarlos [COLOR cyan][B]Todos[/B][/COLOR] de una sola vez ?'):
                    platformtools.dialog_notification('UniNovelas', '[COLOR cyan]Cargando ' + str(sum_parts) + ' elementos[/COLOR]')
                    item.perpage = sum_parts
                else: item.perpage = 50

    title_ser = item.contentSerieName.replace("’s", 's').replace("'t", 't').replace(':', '').replace("'t", 't').replace('ñ', 'n')

    title_ser = title_ser.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
    title_ser = title_ser.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace(' ', '-').lower()

    title_ser = title_ser.replace('(', '').replace(')', '').strip()

    title_ser = title_ser.replace('&#8217;', '').replace('&#8220;', '').replace('&#8221;', '').replace('&amp;', '').replace('amp;', '').replace('quot;', '').strip()

    for match in matches[item.page * item.perpage:]:
        url = scrapertools.find_single_match(match, '<a href="(.*?)"')

        if not title_ser in url: continue

        title = scrapertools.find_single_match(match, 'title="(.*?)"')

        title = title.replace('&#8211;', '').strip()

        title = title.replace('Capitulo Completo', '').replace('Completo', '').replace('HD', '').strip()

        thumb = scrapertools.find_single_match(match, 'src="(.*?)"')

        epis = scrapertools.find_single_match(url, '-capitulo-(.*?)-')
        if not epis: epis = scrapertools.find_single_match(url, '-capitulo-(.*?)/')

        if not epis: epis = 1

        titulo = title

        if not titulo: titulo = title_ser.replace('-', ' ').capitalize()

        url = host[:-1] + url

        if not 'capitulo' in titulo.lower():
            titulo = str(item.contentSeason) + 'x' + str(epis) + ' ' + titulo

        itemlist.append(item.clone( action='findvideos', url = url, title = titulo, thumbnail = thumb,
                                    contentType = 'episode', contentSeason = item.contentSeason, contentEpisodeNumber=epis ))

        if not hay_match:
            if len(itemlist) >= item.perpage:
                break
        else:
            if len(itemlist) >= (item.perpage + 1):
               break

    tmdb.set_infoLabels(itemlist)

    if itemlist:
        if len(matches) > ((item.page + 1) * item.perpage):
            itemlist.append(item.clone( title="Siguientes ...", action="episodios", page= item.page + 1, perpage = item.perpage, text_color = 'coral' ))
        else:
            next_page = scrapertools.find_single_match(data, '<div class="pagination">.*?<span class="current">.*?<a href="(.*?)"')

            if next_page:
                if '/page/'in next_page:
                    itemlist.append(item.clone( title = 'Siguientes ...', url = next_page, action = 'episodios', page = 0, text_color = 'coral' ))

    return itemlist


def findvideos(item):
    logger.info()
    itemlist = []

    data = do_downloadpage(item.url)
    data = re.sub(r"\n|\r|\t|&nbsp;|<br>|<br/>", "", data)

    ses = 0

    matches1 = scrapertools.find_multiple_matches(data, '<iframe.*?src="(.*?)"')
    matches2 = scrapertools.find_multiple_matches(data, '<IFRAME.*?SRC="(.*?)"')

    matches3 = scrapertools.find_multiple_matches(data, "<iframe.*?src='(.*?)'")
    matches4 = scrapertools.find_multiple_matches(data, "<IFRAME.*?SRC='(.*?)'")

    matches5 = scrapertools.find_multiple_matches(data, 'videoIframe.src = "(.*?)"')

    matches = matches1 + matches2 + matches3 + matches4 + matches5

    for url in matches:
        if not url: continue

        if url.endswith('.jpg'): continue

        elif 'data:image' in url: continue
        elif '/avatar/' in url: continue

        ses += 1

        if url.startswith("https://sb"): continue

        elif '/argtesa.' in url: continue

        elif 'fembed' in url or  'streamsb' in url or 'playersb' in url or 'fcom' in url: continue
        elif '.lvturbo.' in url: continue

        if url.startswith("//"): url = 'https:' + url

        if '/videoembed//' in url: url = url.replace('/videoembed//', '/videoembed/')

        elif 'api.mycdn.moe/uqlink.php?id=' in url: url = url.replace('api.mycdn.moe/uqlink.php?id=', 'uqload.com/embed-')

        elif 'api.mycdn.moe/dourl.php?id=' in url: url = url.replace('api.mycdn.moe/dourl.php?id=', 'dood.to/e/')

        elif 'api.mycdn.moe/dl/?uptobox=' in url: url = url.replace('api.mycdn.moe/dl/?uptobox=', 'uptobox.com/')

        elif url.startswith('http://vidmoly/'): url = url.replace('http://vidmoly/w/', 'https://vidmoly/embed-').replace('http://vidmoly/', 'https://vidmoly/')

        elif url.startswith('https://sr.ennovelas.net/'): url = url.replace('/sr.ennovelas.net/', '/waaw.to/')
        elif url.startswith('https://video.ennovelas.net/'): url = url.replace('/video.ennovelas.net/', '/waaw.to/')
        elif url.startswith('https://reproductor.telenovelas-turcas.com.es/'): url = url.replace('/reproductor.telenovelas-turcas.com.es/', '/waaw.to/')
        elif url.startswith('https://novelas360.cyou/player/'): url = url.replace('/novelas360.cyou/player/', '/waaw.to/')
        elif url.startswith('https://novelas360.cyou/'): url = url.replace('/novelas360.cyou/', '/waaw.to/')

        url = url.replace('/7/', '/e/').replace('&#038;', '&')

        servidor = servertools.get_server_from_url(url)
        servidor = servertools.corregir_servidor(servidor)

        url = servertools.normalize_url(servidor, url)

        other = ''
        if servidor == 'various': other = servertools.corregir_other(url)

        itemlist.append(Item( channel = item.channel, action = 'play', server = servidor, title = '', url = url, language = 'Lat', other = other ))

    if not itemlist:
        if not ses == 0:
            platformtools.dialog_notification(config.__addon_name, '[COLOR tan][B]Sin enlaces Soportados[/B][/COLOR]')
            return

    return itemlist


def search(item, texto):
    logger.info()
    try:
        item.url = host + '?s=' + texto.replace(" ", "+")
        return list_all(item)
    except:
        import sys
        for line in sys.exc_info():
            logger.error("%s" % line)
        return []
