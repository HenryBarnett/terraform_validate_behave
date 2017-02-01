from terraform_validate import Validator
import os
from unittest import TestCase


class TestValidatorFunctional(TestCase):

    def setUp(self):
        self.path = os.path.join(os.path.dirname(os.path.realpath(__file__)))

    def test_filter_type_by_id(self):
        validator = Validator(os.path.join(self.path, "test_scripts/filter_id"))
        validator.resources().types_by_id('some_id_2').is_size(2)

        # This fails
        with self.assertRaisesRegexp(AssertionError, "Type list 'some_id_2' should have size 3 but has size 2."):
            validator.resources().types_by_id('some_id_2').is_size(3)
