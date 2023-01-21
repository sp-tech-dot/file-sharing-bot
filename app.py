import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'GreyMatters_Bot'

#Ex https://Greymattersbot:ghp_147bkkabcdefgh@github.com/Greymattersbot/Mogenius
os.system("git clone https://sp-tech-dot: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@github.com/sp-tech-dot/file_share okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 main.py &")
