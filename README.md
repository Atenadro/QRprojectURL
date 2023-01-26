# QRprojectURL - QR Code Generator
Este código utiliza la librería qrcode para generar códigos QR a partir de una URL o texto específico.

Uso
Importe la librería qrcode al inicio de su archivo.
Introduzca el URL o texto que desea mostrar dentro de las '' en la variable input.
Ejecute el código. Esto generará un archivo PNG con el nombre 'qrtelecappurl.png' en su directorio actual.

Personalización
Puede cambiar el tamaño de la caja y el borde del código QR mediante los parámetros box_size y border en la línea qr = qrcode. QRCode(version=1, box_size=10, border=5).
Puede cambiar el color de relleno y el color de fondo del código QR utilizando los parámetros fill y back_color en la línea img = qr.make_image(fill='black', back_color='white').
Puede cambiar el nombre del archivo PNG generado mediante el parámetro save en la línea img.save('qrtelecappurl.png').

Requisitos
Python 3.x
qrcode library

Instalacion de qrcode
pip install qrcode
