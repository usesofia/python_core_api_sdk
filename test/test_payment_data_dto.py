# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.payment_data_dto import PaymentDataDto

class TestPaymentDataDto(unittest.TestCase):
    """PaymentDataDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentDataDto:
        """Test PaymentDataDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentDataDto`
        """
        model = PaymentDataDto()
        if include_optional:
            return PaymentDataDto(
                payer_name = '',
                payer_branch_number = '',
                payer_account_number = '',
                payer_routing_number = '',
                payer_routing_number_ispb = '',
                payer_document_number_type = '',
                payer_document_number_value = '',
                reason = '',
                receiver_name = '',
                receiver_branch_number = '',
                receiver_account_number = '',
                receiver_routing_number = '',
                receiver_routing_number_ispb = '',
                receiver_document_number_type = '',
                receiver_document_number_value = '',
                payment_method = '',
                reference_number = '',
                receiver_reference_id = ''
            )
        else:
            return PaymentDataDto(
        )
        """

    def testPaymentDataDto(self):
        """Test PaymentDataDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
