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
