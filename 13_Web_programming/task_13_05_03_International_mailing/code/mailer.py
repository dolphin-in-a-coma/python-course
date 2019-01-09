import json
import os.path
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate
import requests

SMTP_TLS = True


class Mailer:
    def __init__(self, my_email, my_passwd):
        self.it_email = my_email
        self.it_email_password = my_passwd
        self.it_email_smtp_server = 'smtp.gmail.com'
        self.it_email_smtp_port = 587
        self.log_filename = os.path.abspath('log.txt')
        self.msg = MIMEText('', 'plain', 'utf-8')
        self._settings = None
        self._options_file_name = 'options.json'
        self._read_config(self._options_file_name)
        self._template_file_name = 'template.txt'
        f = open(self._template_file_name, 'r', encoding='utf8')
        self._template_msg = ''.join(f.readlines())
        f.close()

    def send_mail(self, text, target_email):
        encoding = 'utf-8'
        session = None
        self.msg = MIMEText(str(text), 'plain', encoding)
        self.msg['Subject'] = Header('Поторопитесь!',
                                     encoding)
        self.msg['From'] = Header('Русские Матрешки', encoding)
        self.msg['To'] = target_email
        self.msg['Date'] = formatdate()
        try:
            session = smtplib.SMTP(self.it_email_smtp_server,
                                   str(self.it_email_smtp_port))
            if SMTP_TLS:
                session.ehlo()
                session.starttls()
                session.ehlo()
                session.login(self.it_email,
                              self.it_email_password)
            session.sendmail(self.it_email, target_email,
                             self.msg.as_string())
        except Exception as e:
            raise e
        finally:
            if session:
                session.quit()

    def _read_config(self, file_name):
        f = open(file_name, 'r', encoding='utf-8')
        raw_json = ''.join(f.readlines()).replace('\n', '').replace('\t', '')
        f.close()
        self._settings = json.loads(raw_json)

    def run(self):
        for row in self._settings['clients']:
            msg = self._create_msg(self._template_msg, row)
            self.send_mail(msg, row['email'])

    def _create_msg(self, template, client):
        lang = client['language']
        if lang == 'ru':
            return template
        url = "https://translate.yandex.net/api/v1.5/tr.json/translate?"
        answer = requests.post(url,
                               {'lang': 'ru-{}'.format(lang),
                                "key": self._settings['yandex']['api_key'],
                                "text": template})
        body = answer.content.decode(encoding='utf8')
        translate_msg = json.loads(body)['text'][0]
        return translate_msg
        
mail = Mailer(mail, password)
mail.run()
