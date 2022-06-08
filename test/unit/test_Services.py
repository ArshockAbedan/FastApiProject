'''
@File    :   test_Services.py   
@Contact :   arefabedjooy@gmail.com
@License :   (C)Copyright 2020-2022
 
@Modify Time      @Author          @Version    @Desciption
------------      ------------     --------    -----------
6/6/2022 12:06 PM   Aref Abedjooy       1.0         None
'''

import pytest

from app.Services import calc_expected_health_premium


@pytest.fixture()
def my_lead_id():
    return [
        {
            "lead_id": 9,
            "marketing_rank": 1,
            "gender": "F",
            "age": 5,
            "credit_score": 700,
            "urgency": "Within 2 Months"
        }]


def test_calc_expected_health_premium(my_lead_id):
    assert calc_expected_health_premium(my_lead_id) == "You are not in the accepted age range!"
