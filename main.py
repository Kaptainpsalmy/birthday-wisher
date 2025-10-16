import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# === Your email details ===
sender = "kaptainpsalmy@gmail.com"
receiver = "roseline1122333@gmail.com"   # Replace with her real email
password = "wxbx wvof lqia dbrf"            # Use Gmail app password (not normal password)

# === Email setup ===
msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = "🎂 A Birthday Surprise for You, Ameenah! ❤️"

# === Email body ===
body = """
Hi Ameenah 💖,

I made something special for your birthday — just for you.

Please open the attached file to see it 🎉

Wishing you all the happiness in the world!

– Samuel
"""
msg.attach(MIMEText(body, "plain"))

# === Attach the HTML file ===
filename = "greetings.html"  # The file you made
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename= {filename}")
msg.attach(part)

# === Send email ===
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.send_message(msg)

print("🎉 Email sent successfully to Ameenah!")