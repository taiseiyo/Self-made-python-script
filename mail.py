from email import message
import smtplib

smtp_host='smtp.gmail.com'
smtp_port=587

msg = message.EmailMessage()
msg.set_content("こんにちは、Taiseiです。体調不良の為、本日のイベントを欠席させて頂きます。") 
msg['Subject'] = "欠席連絡"
msg['From'] = "taiseiyo11@gmail.com"
msg['To'] = "drn29309@kwansei.ac.jp"
 
# メールサーバーへアクセス
server = smtplib.SMTP(smtp_host, smtp_port)
#暗号化の開始
server.ehlo()
server.starttls()
#TLS (Transport Layer Security) モードで SMTP 接続します。続く全てのSMTP コマンドは暗号化されます。
server.login("taiseiyo11@gmail.com","taiseiyo11")
server.send_message(msg)
server.quit()
