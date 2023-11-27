from unittest.mock import Mock
from lib.cat_facts_API import *

def test_the_api():

    mock_repsponse = Mock()
    mock_request = Mock()

    mock_request.get.return_value = mock_repsponse

    mock_repsponse.json.return_value = {
        "fact":"The chlorine in fresh tap water irritates sensitive parts of the cat's nose. Let tap water sit for 24 hours before giving it to a cat."
    }

    fact = CatFacts(mock_request)
    result = fact.provide()
    assert result == "Cat fact: The chlorine in fresh tap water irritates sensitive parts of the cat's nose. Let tap water sit for 24 hours before giving it to a cat."
