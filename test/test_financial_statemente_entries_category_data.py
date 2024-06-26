# coding: utf-8

"""
    Sofia Api

    Api principal do sistema Sofia.

    The version of the OpenAPI document: 0.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.financial_statemente_entries_category_data import FinancialStatementeEntriesCategoryData

class TestFinancialStatementeEntriesCategoryData(unittest.TestCase):
    """FinancialStatementeEntriesCategoryData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FinancialStatementeEntriesCategoryData:
        """Test FinancialStatementeEntriesCategoryData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FinancialStatementeEntriesCategoryData`
        """
        model = FinancialStatementeEntriesCategoryData()
        if include_optional:
            return FinancialStatementeEntriesCategoryData(
                category_id = '',
                category_name = '',
                outcome = 1.337,
                subcategories = [
                    openapi_client.models.financial_statemente_entries_subcategory_data.FinancialStatementeEntriesSubcategoryData(
                        subcategory_id = '', 
                        subcategory_name = '', 
                        outcome = 1.337, )
                    ]
            )
        else:
            return FinancialStatementeEntriesCategoryData(
                category_id = '',
                category_name = '',
                outcome = 1.337,
                subcategories = [
                    openapi_client.models.financial_statemente_entries_subcategory_data.FinancialStatementeEntriesSubcategoryData(
                        subcategory_id = '', 
                        subcategory_name = '', 
                        outcome = 1.337, )
                    ],
        )
        """

    def testFinancialStatementeEntriesCategoryData(self):
        """Test FinancialStatementeEntriesCategoryData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
