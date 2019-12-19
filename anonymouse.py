# coded by github.com/thelinuxchoice/anonymouse
#edited by Pratyaksha Beri(Shad0wMazt3r)
import requests

print("\nAnonymous Email by anonymouse.org")
print("coded by github.com/thelinuxchoice Edited by Pratyaksha Beri(Shad0wMazt3r)e\n")
to = input('to: ')
subject = input('subject: ')
message = input('body: ')
user_agent = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Go) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'
sess = requests.Session()
email_req = sess.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
	'Host': 'anonymouse.org',
	'User-Agent': user_agent,
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://anonymouse.org/anonemail.html',
        'Connection': 'close',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type':'application/x-www-form-urlencoded'
}, data={
	'to': to,
	'subject': subject,
	'text': message
})

if 'The e-mail has been sent' in email_req.text:
    print("[+] Email Sent!")
    print("[+] In order to increase your privacy, the anonymous e-mail will be randomly delayed up to 12 hours")


