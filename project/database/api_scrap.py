from bs4 import BeautifulSoup
import requests
import prettify
import datetime

class Scrap_info:
    def __init__(self):
        self.matchs = []
        self.url = 'https://www.footao.tv/programmefoot.php?mois=mars&ms=03&an=2021'
        self.response = requests.get(self.url)
        self.content = BeautifulSoup(self.response.content, 'html.parser')
        

    def finder(self):
        element = self.content.select('article>section')
        for ii, i in enumerate(element):
            dates = element[ii]['id']
            if dates=="pjr":
                dates = datetime.date.today()
                j = str(dates.day)
                m = list(str(dates.month))
                if len(m) == 1:
                    m.insert(0, "0")
                    m = "".join(m)
                else:
                    m = "".join(m)
                yyyy = list(str(dates.year))
                yy = "".join(yyyy[2:])
                date_num = j+m+yy
            else:
                date_nums = list(dates)
                del date_nums[0]
                date_num = "".join(date_nums)
            date_s = element[ii].select("h2>a")
            date_text = date_s[0].get_text()
            divs = element[ii].select("div")
            for yy, y in enumerate(divs):
                time_s = divs[yy].select('time')
                time = time_s[0].get_text()
                chaine_s = divs[yy].select('a')
                chaine_o = list(chaine_s[0].find('img')['alt'])
                if 'm' in chaine_o:
                    chaine = ''.join(chaine_o[:chaine_o.index('m') - 1])
                else:
                    chaine = "???"
                match_s = divs[yy].select("a[class=rc]")
                match = match_s[0].get_text()
                match_l = list(match)
                if '·' in match_l:
                    eq1 = ''.join(match_l[:match_l.index('·')-1])
                    eq2 = ''.join(match_l[match_l.index('·')+2:])
                else:
                    eq1 = match
                    eq2 = match
                compet_s = divs[yy].select("span[class=ap]")
                if len(compet_s) > 0:
                    compet = compet_s[0].get_text()
                    if compet == "\xa0 \xa0»\xa0":
                        compet = "Ligue Europa"
                    dict_match = {"Nom":match, "Date_text":date_text, "Time":time, "Equipe1":eq1, "Equipe2":eq2, "Competition":compet, "Chaine":chaine, "Date_num": date_num}
                else :
                    compet = "match finie"
                    dict_match = {"Nom":match, "Date_text":date_text, "Time":time, "Equipe1":eq1, "Equipe2":eq2, "Competition":compet, "Chaine":chaine, "Date_num": date_num}
                self.matchs.append(dict_match)
