from bs4 import BeautifulSoup
from requests import get
from posel import Posel

# dostęp do danych posłów mamy przez ten link:
# https://sejm.gov.pl/Sejm9.nsf/posel.xsp?id=XXX
# gdzie XXX to numer od 001
# zwróć uwagę, że są z zerami przewodnimi
# max id wyszedł mi 473
# ale z pętli trzeba jakoś pewnie wyjść

url = 'https://sejm.gov.pl/Sejm9.nsf/posel.xsp?id='
i = 1
# while True:
str_id = str(i)
while len(str_id) < 3:
    str_id = '0' + str_id
strona = url + str_id

req = get(strona)
soup = BeautifulSoup(req.text, "html.parser")
# zakładamy, że nie ma posła o danym id
# jeśli nie ma nazwy
nazwa = soup.find(id="title_content").h1.get_text()
#if not nazwa:
#    break
partia = soup.find(id="lblLista").find_next_sibling().get_text()
wyksz = soup.find(id="lblWyksztalcenie").find_next_sibling().get_text()
szkola = soup.find(id="lblSzkola").find_next_sibling().get_text()
zawod = soup.find(id="lblZawod").find_next_sibling().get_text()
posel = Posel(nazwa, partia, wyksz, szkola, zawod)
i += 1
