import Lab2.bmi
import Lab2.bmi as bmi
print("Test_bmi.py")
def test_bmi_normal_weight():
    result = Lab2.bmi.calculate_bmi(1.73,60)
    assert(result==0)
def test_bmi_over_weight():
    result = Lab2.bmi.calculate_bmi(1.73,78)
    assert(result==1)
def test_bmi_under_weight():
    result = Lab2.bmi.calculate_bmi(1.73,48)
    assert(result==-1)
