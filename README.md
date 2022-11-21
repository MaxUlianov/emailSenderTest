# emailSenderTest

Email sender app with following functions:
1. html-email sending to subscribers from subscriber database (django db sqlite)
2. Delayed emails (scheduled emails with celery, in this example – email every 120 seconds)
3. Custom emails (name, second name of subscriber in html letter)
4. Email opening tracker with tracking pixel (set up for local network in this example)
