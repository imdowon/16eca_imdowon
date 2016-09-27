# -*- coding: utf8 -*-
"""
 수치 적분 응용 예제
 단면의 도심 구하기
"""
# 수학 기능을 담고 있는 math 모듈을 불러 들임
import math

import pylab

import num_int

#
help(num_int.rect0)


def main():
    #
    y_min = 0.0
    y_max = 0.12
    #
    n = 120

    #

    #
    area = num_int.trapezoid1(f, y_min, y_max, n)
    #
    moment_first = num_int.trapezoid1(g, y_min, y_max, n)

    #
    centroid = moment_first / area

    # 도심 계산 끝

    # 결과 값 표시
    print "area =", area
    print "moment =", moment_first
    print("centroid = %g" % centroid)

    # 그림 준비 시작
    y_list = pylab.arange(y_min, y_max, 1e-6)
    w_list = [f(y) for y in y_list]

    # 단면 표시
    pylab.fill_between(y_list, w_list)
    # 도심 위치에 수직선 표시
    pylab.axvline(x=centroid, c='r')

    #
    pylab.axis('equal')
    #
    pylab.grid()
    #

    #
    pylab.show()


def f(y):
    """



    :param y:
    :return:
    """
    if 0.0 <= y <0.02:
        r = 0.01
        result = 0.04 + math.sqrt(r * r - (y - r) ** 2)
        #
    elif 0.02 <= y < 0.10:
        result = 0.02
    elif 0.10 <= y <= 0.12:
        result = 0.06
    else:
        result = 0.0

    return result


def g(y):
    result = y * f(y)
    return result


if "__main__" == __name__:
    main()