# -*- coding: utf-8 -*-


from nose.tools import assert_equal, istest
from parameterized import parameterized


from ..utils.enumerators import ACCRUAL_PERIODICITY_DICT
from ..utils.datajsonar import translate_accrual_periodicity



@parameterized([
    ("quarterly", "R/P3M",),
    ("biannually", "R/P6M",),
    ("weekly", "R/P1W",),
    ("irregular", "eventual",),
    ("fortnightly", "R/P2W",),
    ("monthly", "R/P1M",),
    ("asNeeded", "eventual",),
    ("annually", "R/P1Y",),
    ("daily", "R/P1D",),
    ("notPlanned", "eventual",),
    ("continual", "R/PT1S",),
    ("unknown", "eventual",),
])
def test_translate_maintenance_frequency(value, expected):
    assert_equal(str(expected), translate_accrual_periodicity(value))
