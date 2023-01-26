import qrcode

#Introduce el URL o Texto que deseas mostrar dentro de las ''
input = 'https://sites.google.com/view/vps-condiciones-de-servicio/inicio'

qr = qrcode. QRCode(version=1, box_size=10, border=5)

qr.add_data(input)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
#Nombre del archivo PNG que va a imprimir
img.save('qrtelecappurl.png')
