from email import message
import smtplib

smtp_host = 'smtp.gmail.com'
smtp_port = 587

msg = message.EmailMessage()
msg.set_content("こんにちは **")
msg['Subject'] = "**"
msg['From'] = "**"
msg['To'] = "**"

# メールサーバーへアクセス
server = smtplib.SMTP(smtp_host, smtp_port)
# 暗号化の開始
server.ehlo()
server.starttls()
# TLS (Transport Layer Security) モードで SMTP 接続します。続く全てのSMTP コマンドは暗号化されます。
server.login("user", "password")
server.send_message(msg)
server.quit()
