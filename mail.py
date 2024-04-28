
import smtplib


Host= "smtp.gmail.com"
Port=587

FROM_EMAIL="medisys.pms@gmail.com"
TO_EMAIL="shaikharsheen13@gmail.com"
PASSWORD=input(str("Enter Password:"))

Message="""Subject: Demo MAIL
Hi Arsheen!
Mailed through Medisys Account

Thanks!
Medisys"""

mail=smtplib.SMTP(Host,Port)

mail.starttls()
print("TLS Connection started")

mail.login(FROM_EMAIL,PASSWORD)
print("Logging In Successful")


mail.sendmail(FROM_EMAIL,TO_EMAIL,Message)
print("Email Sent Successful")
mail.quit()