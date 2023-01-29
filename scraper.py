from bs4 import BeautifulSoup
from requests import get
from posel import Posel
from dbhelper import insert_posel_into_db, create_db

def _none_or_text(_soup, _id):
    if _soup.find(id=_id):
        return _soup.find(id=_id).find_next_sibling().get_text()
    else:
        return None

# dostęp do danych posłów mamy przez ten link:
# https://sejm.gov.pl/Sejm9.nsf/posel.xsp?id=XXX
# gdzie XXX to numer od 001
# zwróć uwagę, że są z zerami przewodnimi

def get_poslowie():
    url = 'https://sejm.gov.pl/Sejm9.nsf/posel.xsp?id='
    i = 1
    create_db()
    while True:
        str_id = str(i)
        while len(str_id) < 3:
            str_id = '0' + str_id
        print('\rPoseł nr',str_id, end='')
        strona = url + str_id

        req = get(strona)
        soup = BeautifulSoup(req.text, "html.parser")
        # zakładamy, że nie ma posła o danym id
        # jeśli nie ma nazwy
        nazwa = soup.find(id="title_content").h1.get_text()
        if not nazwa:
            break
        partia = _none_or_text(soup, 'lblLista')
        wyksz = _none_or_text(soup, 'lblWyksztalcenie')
        szkola = _none_or_text(soup, 'lblSzkola')
        zawod = _none_or_text(soup, 'lblZawod')
        posel = Posel(i, nazwa, partia, wyksz, szkola, zawod)
        insert_posel_into_db(posel)
        i += 1

def get_przemowienia():
    # TODO
    url = 'https://sejm.gov.pl/Sejm9.nsf/wypowiedzi.xsp?type=P&symbol=WYPOWIEDZI_POSLA&id='
    i = 1
