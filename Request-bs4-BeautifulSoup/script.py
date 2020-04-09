import requests  # python library for http request
from bs4 import BeautifulSoup  # this help us to pull out individiual item from website
import smtplib # enables us to send email in pyhton no need to instll
import time

URL ='https://www.amazon.in/Beats-MNEN2ZM-Wireless-Headphones-Gloss/dp/B01LVVF7LA/ref=br_msw_pdt-6?_encoding=UTF8&smid=A14CZOWI0VEHLG&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=H8MAZZQSBVVPK6DJSF7W&pf_rd_t=36701&pf_rd_p=2b9bb3c1-71bb-48bb-8476-31c6e37895b1&pf_rd_i=desktop'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

#response = requests.get(URL) 

#print(response.status_code) 200 ok 404 notfoudn
#print(response.content)  // gets all content from website 
#print(response.headers)  // content-type etc etc

def find_price():
    page = requests.get(URL,headers=headers)         

    soup = BeautifulSoup(page.content, "html.parser")

    title  = soup.find(id='priceblock_dealprice').getText()
    title = [title[x:x+1] for x in range(2,8)]
    title.remove(',')
    price =''
    for i in range(len(title)):
        price+=title[i]
    price = float(price)
    price  = price + 1000
    if(price > 17000.0):
        print(price)
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() #The client sends this command to the SMTP server to identify itself and initiate the SMTP conversation.
    server.starttls() #encrypts are connection
    server.ehlo()

    server.login('sam9111doshi@gmail.com','9111204454')

    subject = 'price went up'
    body = 'checkout link https://www.amazon.in/Beats-MNEN2ZM-Wireless-Headphones-Gloss/dp/B01LVVF7LA/ref=br_msw_pdt-6?_encoding=UTF8&smid=A14CZOWI0VEHLG&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=H8MAZZQSBVVPK6DJSF7W&pf_rd_t=36701&pf_rd_p=2b9bb3c1-71bb-48bb-8476-31c6e37895b1&pf_rd_i=desktop'

    msg = f"Subject: {subject}\n\n{body}" #new f-string way to format in python like we use ``  and ${} in js
    
    server.sendmail(
        'sam9111doshi@gmail.com', #from
        'sam9111doshi@gmail.com', #to
        msg
    )
    print('mail sent!')
    server.quit()

find_price()

while(True):
    send_mail()
    time.sleep(60*60*12)