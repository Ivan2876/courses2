import pytest

from homework2_utils import is_password_strong


class TestIsPasswordStrong:
    @pytest.mark.parametrize(
        'password,expected',
        [
            ('fejh3jh4k3h4hh34h', True),
            ('7347ghfhfgfr', True),
            ('grrgrgr355532', True),
            ('ghrigehhgekhjgrh266', True),
            ('fewfefe23232', True),
            ('dwwdwd', False),
            ('fghfehfhjkfhekfhhdhfhfhekfg', False),
            ('236468628646286458462', False),
            ('c2c22c', False),
            ('2gh3g32 gh3gh2ggh2332', False),

        ]
    )
    def test_is_password_strong(self, password: str, expected: bool):
        actual = is_password_strong(password)
        assert expected is actual


@pytest.mark.skip(reason="Test is not ready yet")
def test_is_password_strong():
    password = 'fjejwfwkkhwfh6468346'
    actual = is_password_strong(password)
    assert actual is True

