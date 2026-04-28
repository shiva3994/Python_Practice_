import qrcode

#Taking UPI ID as a input
upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&apn=Name&am=Amount&cu=CURRENCY&th=MESSAGE

#Defining the paymnet url based on upi id and the payment app
#You can modify the urls based on the payment apps you want to support
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR code for each paymnet app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Save the qr code to image (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('phonepe_qr.png')

#Display the qr code and for that you may need to install pillow library
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

