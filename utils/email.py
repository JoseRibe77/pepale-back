import smtplib
from email.mime.text import MIMEText

def enviar_correo_admin(producto, comprador_email):
    msg = MIMEText(f"Se vendió: {producto} a {comprador_email}")
    msg["Subject"] = "Nueva venta"
    msg["From"] = "tu_correo@gmail.com"
    msg["To"] = "ribej881@gmail.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("tu_correo@gmail.com", "tu_contraseña")
        server.send_message(msg)
