# AlpacaBot
This is an automatic stock trading bot that will obtain alerts from Tradingview or anywhere you would like alerts from, to Node on your PC which will then be read by your program that executes trades VIA AlpacaAPI Broker on your papertrading account

Personal Notification Server:

Uses Flask as the webhook
Uses ngrok as the public domain webhook link to flask server on pc.
Uses Trading View Alerts to execute trades

- Run Webserver by Running "python Webhookserver.py" in CMD (cd desktop, will make sure were in right directory if files are on desktop)
- Link ngrok to the webhook server tunnel which is coded to be (5000). Paste into cmd: "ngrok http 5000"
- Now ngrok will show your public URL: This changes every time, heres and example: https://bcdb-73-243-86-34.ngrok-free.app (this is what you set as yoru webhook for alerts on tradingview)
- View incoming Alerts on ngrok account: http://127.0.0.1:4040/inspect/http
