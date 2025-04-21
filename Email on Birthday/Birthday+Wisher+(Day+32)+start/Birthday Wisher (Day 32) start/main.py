import smtplib

my_email = "webblip11@gmail.com"
password = "lwhlgmkzdtbpyflv"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="emmadojusrivani@gmail.com",msg="Hello")

