Inside the root folder of the project, run the following commands to install the required packages:

$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

Add a .env file in the root folder of the project with the following content:
NUVEI_MERCHANT_ID=
NUVEI_MERCHANT_SITE_ID=
NUVEI_MERCHANT_SECRET_ID=
NUVEI_API_URL=

Run the following command to test a refund with Nuvei
$ python script.py

Output:
=====================================
Calculating checksum..
=====================================
Checksum: cabb84cf2cf85b5cb4db5c8abae79d901e74255a0b5162af2a0785bbb6519679
=====================================
{'status': 'ERROR', 'errCode': 1019, 'reason': 'We are experiencing technical difficulties. Please, try again later!', 'version': '1.0'}
