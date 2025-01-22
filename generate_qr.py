import qrcode

# URL de votre menu
url = "https://hazemch12.github.io/menu_skifa/"

# Générer le QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Créer l'image du QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Sauvegarder l'image
img.save("menu_skifa_qr_code.png")

print("QR Code généré et sauvegardé sous 'menu_skifa_qr_code.png'.")
