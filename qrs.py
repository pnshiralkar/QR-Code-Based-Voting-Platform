# Config

np = 301 # Number of photos
ns = 301 # Number of sketches


# Actual Code
import requests
import json

s = "{:04d}"

for i in range(1,np):
	print("Generating QR Code for P" + s.format(i), flush=True)
	r = requests.post('https://qr-generator.qrcode.studio/qr/custom', json={"data":"P" + s.format(i) ,"config":{"body":"square","eye":"frame1","eyeBall":"ball0","erf1":["fh"],"erf2":[],"erf3":["fh","fv"],"brf1":[],"brf2":[],"brf3":[],"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":"#000000","eye2Color":"#000000","eye3Color":"#000000","eyeBall1Color":"#000000","eyeBall2Color":"#000000","eyeBall3Color":"#000000","gradientColor1":"","gradientColor2":"","gradientType":"linear","gradientOnEyes":"true","logo":"b16b7f94376a16f93a1f8f2398f06ea98efca44c.png","logoMode":"clean"},"size":1500,"download":"imageUrl","file":"png"})

	fn = json.loads(r.text)
	#print(fn)

	print("Downlodading generated QR for P" + s.format(i))

	f = open('P' + s.format(i) + '.png', 'wb')
	f.write(requests.get('https:' + fn['imageUrl']).content)
	f.close()

	print("Downloaded P" + s.format(i), flush=True, end="\n\n")


for i in range(1,ns):
	print("Generating QR Code for S" + s.format(i), flush=True)
	r = requests.post('https://qr-generator.qrcode.studio/qr/custom', json={"data":"S" + s.format(i) ,"config":{"body":"square","eye":"frame1","eyeBall":"ball0","erf1":["fh"],"erf2":[],"erf3":["fh","fv"],"brf1":[],"brf2":[],"brf3":[],"bodyColor":"#000000","bgColor":"#FFFFFF","eye1Color":"#000000","eye2Color":"#000000","eye3Color":"#000000","eyeBall1Color":"#000000","eyeBall2Color":"#000000","eyeBall3Color":"#000000","gradientColor1":"","gradientColor2":"","gradientType":"linear","gradientOnEyes":"true","logo":"b16b7f94376a16f93a1f8f2398f06ea98efca44c.png","logoMode":"clean"},"size":1500,"download":"imageUrl","file":"png"})

	fn = json.loads(r.text)
	#print(fn)

	print("Downlodading generated QR for S" + s.format(i))

	f = open('S' + s.format(i) + '.png', 'wb')
	f.write(requests.get('https:' + fn['imageUrl']).content)
	f.close()

	print("Downloaded S" + s.format(i), flush=True, end="\n\n")
