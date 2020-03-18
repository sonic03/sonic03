import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

kimden=input("e posta adresiniz nedir :")
kime=input("Gönderielcek mail girin: ")
konu=input("konu girin")
detay=input("kısaca özetlermisiniz:")



mesaj=MIMEMultipart()
mesaj["From"]="reklamvereneleman@gmail.com"
mesaj["To"]="{}".format(kime)
mesaj["Subject"]="{}".format(konu)

yazi="""
{} adresinden gelen mail;
{}

""".format(kimden,detay)

mesaj_gövede=MIMEText(yazi,"plain")

mesaj.attach(mesaj_gövede)

try:
    mail=smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("reklamvereneleman@gmail.com","147852963Dark")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("gönderim başarılı")
    mail.close()
except:
    sys.stderr.write("bir sorun olutu")
    sys.stderr.flush()







