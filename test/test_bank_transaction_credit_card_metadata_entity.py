# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.bank_transaction_credit_card_metadata_entity import BankTransactionCreditCardMetadataEntity

class TestBankTransactionCreditCardMetadataEntity(unittest.TestCase):
    """BankTransactionCreditCardMetadataEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankTransactionCreditCardMetadataEntity:
        """Test BankTransactionCreditCardMetadataEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BankTransactionCreditCardMetadataEntity`
        """
        model = BankTransactionCreditCardMetadataEntity()
        if include_optional:
            return BankTransactionCreditCardMetadataEntity(
                id = '',
                transaction_id = '',
                installment_number = 1.337,
                total_installments = 1.337,
                total_amount = 1.337,
                payee_mcc = 1.337,
                card_number = '',
                bill_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return BankTransactionCreditCardMetadataEntity(
                id = '',
                transaction_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testBankTransactionCreditCardMetadataEntity(self):
        """Test BankTransactionCreditCardMetadataEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
