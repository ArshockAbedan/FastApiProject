'''
@File    :   Services.py   
@Contact :   arefabedjooy@gmail.com
@License :   (C)Copyright 2020-2022
 
@Modify Time      @Author          @Version    @Desciption
------------      ------------     --------    -----------
6/6/2022 11:16 AM   Aref Abedjooy       1.0         None
'''
import math

import numpy as np


def calc_expected_health_premium(input_data):
    """
     This function calculates the expected health premium
    :param input_data: A dictionary containing details of rach person
    :return: the expected health premium
    """
    if 'credit_score' in input_data:
        credit_score = float(input_data["credit_score"])
    else:
        credit_score = float(0)

    if 'age' in input_data:
        age = float(input_data["age"])
    else:
        return "You are not in the accepted age range!"

    # check for to be in range
    if float(18) > age or age > float(90):
        return "You are not in the accepted age range!"

    if 'marketing_rank' in input_data:
        marketing_rank = float(input_data["marketing_rank"])
    else:
        marketing_rank = float(1)  # best

    if 'gender' in input_data:
        gender = str(input_data["gender"]).lower()
    else:
        gender = "m"

    if 'urgency' in input_data:
        urgency = str(input_data["urgency"]).lower()
    else:
        urgency = "not sure"

    # Determining value of gender_male
    if gender == "m" or gender == "male":
        gender_male = float(1)
    else:
        gender_male = float(0)

    # Determining values of  urgency_immediately, urgency_within_2_months, urgency_not_sure
    if urgency == "immediately":
        urgency_immediately = float(1)
        urgency_within_2_months = float(0)
        urgency_not_sure = float(0)
    elif urgency == "within 2 months":
        urgency_immediately = float(0)
        urgency_within_2_months = float(1)
        urgency_not_sure = float(0)
    elif urgency == "not sure":
        urgency_immediately = float(0)
        urgency_within_2_months = float(0)
        urgency_not_sure = float(1)
    else:
        urgency_immediately = float(0)
        urgency_within_2_months = float(0)
        urgency_not_sure = float(1)

    expected_health_premium = (0.001222 * credit_score) + \
                              (0.00927 * age) - (0.03404 * marketing_rank) \
                              + (0.031735 * urgency_immediately) \
                              + (0.07091 * urgency_within_2_months) \
                              + (0.0233 * urgency_not_sure) + (0.0509 * gender_male) \
                              + 3.622

    return np.exp(expected_health_premium)
