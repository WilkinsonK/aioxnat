from aioxnat.protocols import isvalidator


class TestObjectUtilities:

    def test_isvalidator(self, validator_callable):
        assert isvalidator(validator_callable),\
            "Validator object should return True."

    def test_not_isvalidator(self, generic_callable):
        assert not isvalidator(generic_callable),\
            "Callables not marked as validator should not return True."
