def measurements(measurement_list):
    def area(a_list):
        return a_list[0] * a_list[1]

    def perimeter(a_list):
        return (a_list[0] * 2) + (a_list[1] * 2)

    output = "Perimeter = " + str(perimeter(measurement_list)) + " Area = " + str(area(measurement_list))
    return output


if __name__ == '__main__':
    print(measurements([2.1, 3.4]))
