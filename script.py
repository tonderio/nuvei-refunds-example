import os
import requests
import hashlib
import uuid
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()


class NuveiSdk:
    def __init__(self):
        self.merchant_id = os.getenv("NUVEI_MERCHANT_ID")
        self.merchant_site_id = os.getenv("NUVEI_MERCHANT_SITE_ID")
        self.merchant_secret_id = os.getenv("NUVEI_MERCHANT_SECRET_ID")
        self.base_url = os.getenv("NUVEI_API_URL")
        self.headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
            }

    def generate_timestamp(self):
        return datetime.now().strftime("%Y%m%d%H%M%S")

    def get_client_request_id(self):
        client_request_id = str(uuid.uuid4()).replace('-', '')
        return client_request_id

    def calculate_checksum(
            self,
            timestamp,
            client_request_id,
            amount,
            currency):
        print('=====================================')
        print('Calculating checksum..')
        print('=====================================')

        concatenated_values = (
            f"{self.merchant_id}"
            f"{self.merchant_site_id}"
            f"{client_request_id}"
            f"{amount}"
            f"{currency}"
            f"{timestamp}"
            f"{self.merchant_secret_id}"
        )
        checksum = hashlib.sha256(concatenated_values.encode()).hexdigest()
        print('Checksum:', checksum)
        print('=====================================')
        return checksum

    def prepare_refund_data(self, vals):
        payment_transaction = vals.get("payment_transaction")
        amount = vals.get("amount")
        transaction_id = payment_transaction["response"]["transactionId"]
        currency = payment_transaction["currency"]["code"]
        timestamp = self.generate_timestamp()
        client_unique_id = payment_transaction["response"]["clientUniqueId"]
        client_request_id = self.get_client_request_id()
        checksum = self.calculate_checksum(
            timestamp, client_request_id, amount, currency
        )

        data = {
            "merchantId": self.merchant_id,
            "merchantSiteId": self.merchant_site_id,
            "clientUniqueId": client_unique_id,
            "amount": str(amount),
            "currency": currency,
            "relatedTransactionId": transaction_id,
            "timeStamp": timestamp,
            "checksum": checksum,
        }
        # print(data)

        return data

    def create_refund(self, payload):
        data = self.prepare_refund_data(payload)
        url = self.base_url + "refundTransaction.do"
        response = requests.post(url, data=data, headers=self.headers)
        return response.json()


def main(payload):
    nuvei_sdk = NuveiSdk()
    response = nuvei_sdk.create_refund(payload)
    print(response)


if __name__ == "__main__":
    payload = {
        "amount": 399,
        "payment_transaction": {
            "response": {
                "transactionId": "711000000031707391",
                "clientUniqueId": "12345",
            },
            "currency": {"code": "MXN"}
        },
    }
    main(payload)
