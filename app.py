from flask import Flask, render_template, request, flash
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'mon_secret_flask'

EMAIL_ADDRESS = 'alecalec252@gmail.com'
EMAIL_PASSWORD = 'hbialsvscqfsfplj'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        destinataire = request.form['destinataire']
        sujet = request.form['sujet']
        message = request.form['message']

        msg = EmailMessage()
        msg['Subject'] = sujet
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = destinataire
        msg.set_content(message)

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            flash('✉️ Message envoyé avec succès !', 'success')
        except Exception as e:
            flash(f'❌ Erreur lors de l’envoi : {e}', 'error')

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
