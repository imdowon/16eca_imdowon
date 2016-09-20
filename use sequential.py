# -*- coding: utf8 -*-
# [학번] [이름]
"""
1변수 방정식의 근을 찾는 방법 중 sequential method 를 사용하여
어떤 함수 f(x)의 근을 찾고자 함
"""

#
import root_finding

print dir(root_finding)


def func(x):
    """
    근을 구하고자 하는 함수
    이 경우
    :param x:
    :return:
    """
    #
    return 1.0 * x * x - 3.0


# end of func()
#

# func() 의 근을 찾기 위해 root_finding 모듈의 sequential() 함수를 사용
print  root_finding.sequential(func, 0.01)

# bisection method 로 구하는 법은?

# Newton Raphson method 로 구하는 법은?
