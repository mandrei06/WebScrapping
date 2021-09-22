import requests
from bs4 import BeautifulSoup
contorp=0
r=requests.get('https://www.flanco.ro/')
soup= BeautifulSoup(r.text,'html.parser')
PCategory=soup.find_all('a',attrs={'class':''})
for i in range (0,283):
    print("Categorie: ",PCategory[i].text,"link: ")
    link01=PCategory[i]['href']
    print(link01)
    r=requests.get(link01)
    soup = BeautifulSoup(r.text, 'html.parser')
    PPages=soup.find_all('a',attrs={'class':'jumps-last'})
    link02=link01
    try:
        link02=PPages[0]['href']
        pagini=link02[-6]
    except:
        pagini=1
        pass
    print(pagini)
    for j in range(1,int(pagini)+1):
        if int(pagini)>1:
            link02=link02.replace(link02[-6],str(j))
            link03=link02
        else:
            link03=link02
        r=requests.get(link03)
        PPrices = soup.find_all('span', attrs={'itemprop': 'price'})
        for i in range(0, len(PPrices)):
            first_result = PPrices[i]
            first_result = first_result.find('span')
            first_result = first_result.contents
            first_result = first_result[0]
            PPrices[i] = first_result

        ###Obtinerea numelor produselor de pe site
        PName = soup.find_all('a', attrs={'class': 'product-new-link'})
        new_list = PName[1:70:2]
        PName = new_list
        for i in range(0, len(PName)):
            first_result = PName[i]
            first_result = first_result.text
            PName[i] = first_result


        ###Crearea unei clase care contine pretul si numele produsului
        class NameAndPrice:
            def __init__(self, Name, Price):
                self.Name = Name
                self.Price = Price


        produse = {}
        for i in range(0, min(len(PName), len(PPrices))):
            produse[i] = NameAndPrice(PName[i], PPrices[i])
        for item in produse:
            print(contorp, '.', produse[item].Name," pret: ", produse[item].Price)
            contorp = contorp + 1

r=requests.get('https://mediagalaxy.ro/home/')
link1='https://mediagalaxy.ro'
soup= BeautifulSoup(r.text,'html.parser')
MGCategory=soup.find_all('a',attrs={'class':'ProductsMenu-trigger'})
for i in range (0,len(MGCategory)):
    first_result=MGCategory[i]
    print("Categoria:",first_result.text,"cu linkul:")
    link2=link1+first_result['href']
    print(link2)
    r=requests.get(link2)
    soup = BeautifulSoup(r.text, 'html.parser')
    MGSubCategory = soup.find_all('a', attrs={'class': 'Product u-display-block u-text-align-center u-text-linkInherit u-color-black u-text-no-decoration u-text-hover-underline'})
    for j in range(0,len(MGSubCategory)):
        first_result=MGSubCategory[j]
        print("     ~Subcategoria:",first_result.text," cu linkul:")
        link3=MGSubCategory[j]['href']
        print("     ",link3)
        r=requests.get(link3)
        soup=BeautifulSoup(r.text,'html.parser')
        MGPages = soup.find_all('select', attrs={'class': 'js-trigger-catalog-toolbar-apply-filters'})
        try:
            k=MGPages[3].text[4]
        except:
            k=1
            pass
        for l in range(1,int(k)+1):
                print("          ~pagina: ",l," cu linkul:")
                link4=link3+"/filtru/p/"+str(l)+"/"
                print(link4)
                r = requests.get(link4)
                soup = BeautifulSoup(r.text, 'html.parser')
                ###Obtinerea preturilor de pe site
                MGPrices = soup.find_all('span', attrs={'class': 'Price-int'})
                ###print(len(MGPrices))
                for ii in range(0, len(MGPrices)):
                    first_result = MGPrices[ii]
                    first_result = first_result.contents
                    MGPrices[ii] = first_result
                    ###print(i," ",first_result)
                jj = 0
                for ii in range(0, len(MGPrices)):
                    for jj in range(0, len(MGPrices[ii])):
                        MGPrices[ii][jj] = float(MGPrices[ii][jj])
                ###print (MGPrices)
                ###Obtinerea numelor produselor de pe site
                MGNames = soup.find_all('a', attrs={'class': 'Product-name'})
                ###print(len(MGNames))
                for i in range(0, len(MGNames)):
                    first_result = MGNames[i]
                    first_result = first_result.text
                    MGNames[i] = first_result
                new_list = MGNames[::2]
                MGNames = new_list


                ###Crearea unei clase care contine pretul si numele produsului
                class NameAndPrice:
                    def __init__(self, Name, Price):
                        self.Name = Name
                        self.Price = Price


                produse = {}
                for i in range(0, len(MGNames)):
                    produse[i] = NameAndPrice(MGNames[i], MGPrices[i])
                j = 0
                for item in produse:
                    print(contorp, '.', produse[item].Name," pret: ",produse[item].Price)
                    contorp=contorp+1
                    j = j + 1
