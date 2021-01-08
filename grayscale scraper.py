import cloudscraper
from bs4 import BeautifulSoup as BS
import csv

#urls for all grayscale assets
#XRP was removed from grayscale on December 2020 so it will not be included here

urls = [
    ["BTC", "https://grayscale.co/bitcoin-trust/"],
    ["BCH","https://grayscale.co/bitcoin-cash-trust/"],
    ["ETH","https://grayscale.co/ethereum-trust/"],
    ["ETC","https://grayscale.co/ethereum-classic-trust/"],
    ["LTC","https://grayscale.co/litecoin-trust/"],
    ["XLM","https://grayscale.co/stellar-lumens-trust/"],
    ["ZEC","https://grayscale.co/zcash-trust/"],
    ["ZEN","https://grayscale.co/horizen-trust/"]
]


#initiate cloudscraper
scraper = cloudscraper.create_scraper()
print("-------------")
with open('grayscale_scraping.csv', mode='w', newline='') as output_file:
    file_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow(['asset_name', 'aum', 'shares','asset_per_share','holdings_per_share','market_per_share'])    
        
    for asset in urls:
        
        print(asset[0])
        response = scraper.get(asset[1]).text
        table = BS(response, "html.parser")
        overviewdata = table.find("table", {"class":"overview-data"})
        
        if (asset[0] == "ETC") :
           #AUM
            aum = overviewdata.findAll("tr")[9]
            aum = aum.findAll("td")[1].text
            aum = aum.replace("*","")
            aum = aum.replace("‡","")
            print("AUM: "+aum)

            #sharesoutstanding
            shares = overviewdata.findAll("tr")[10]
            shares = shares.findAll("td")[1].text
            shares = shares.replace("*","")
            shares = shares.replace("‡","")
            print("Shares: " + shares)
            #asset per share
            assetpershare = overviewdata.findAll("tr")[11]
            assetpershare = assetpershare.findAll("td")[1].text
            assetpershare = assetpershare.replace("*","")
            assetpershare = assetpershare.replace("‡","")
            
            print("Asset per share: " + assetpershare)



            
        elif asset[0] == "XLM" or asset[0] == "ZEC" or asset[0] == "ZEN":
             #AUM
            aum = overviewdata.findAll("tr")[7]
            aum = aum.findAll("td")[1].text
            aum = aum.replace("*","")
            aum = aum.replace("‡","")
            print("AUM: "+aum)


            #sharesoutstanding
            shares = overviewdata.findAll("tr")[8]
            shares = shares.findAll("td")[1].text
            shares = shares.replace("*","")
            shares = shares.replace("‡","")
            print("Shares: " + shares)

            #asset per share
            assetpershare = overviewdata.findAll("tr")[9]
            assetpershare = assetpershare.findAll("td")[1].text
            assetpershare = assetpershare.replace("*","")
            assetpershare = assetpershare.replace("‡","")
            print("Asset per share: " + assetpershare)



            
            
        else:
            #AUM
            aum = overviewdata.findAll("tr")[8]
            aum = aum.findAll("td")[1].text
            aum = aum.replace("*","")
            aum = aum.replace("‡","")
            print("AUM: "+aum)


            #sharesoutstanding
            shares = overviewdata.findAll("tr")[9]
            shares = shares.findAll("td")[1].text
            shares = shares.replace("*","")
            shares = shares.replace("‡","")
            print("Shares: " + shares)

            #asset per share
            assetpershare = overviewdata.findAll("tr")[10]
            assetpershare = assetpershare.findAll("td")[1].text
            assetpershare = assetpershare.replace("*","")
            assetpershare = assetpershare.replace("‡","")
            print("Asset per share: " + assetpershare)
            
        #holdings per share and market price per share
        holdingspershare = table.findAll("div","price")[0].text
        print("Holdings per share: ", holdingspershare)

        #market price per share only available for following assets
        if asset[0] == "BTC" or asset[0] == "ETH" or asset[0] == "LTC" or asset[0] == "BCH" or asset[0] == "ETC":
            marketpershare = table.findAll("div","price")[1].text
            print("Market per share: ", marketpershare)


                                         
        file_writer.writerow([asset[0],aum,shares,assetpershare,holdingspershare,marketpershare])
        print("-------------")
