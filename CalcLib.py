class CalcLib(object):

    def __init__(self):
        self.grade_total = 0
        self.pass_total = 0

    def grade_calc(self, grades_array):
        total = 0

        for grade in grades_array:
            print (grade)
            grade_value = int(grade)

            if grade_value == 100:
                total = total + 60
            elif grade_value >= 97:
                total = total + 40
            elif grade_value >= 90:
                total = total + 30

            self.grade_total = total
        return total

    def advisory_calc(self,pass_bool):
        total = 0
        if pass_bool:
            print ("Advisory: " + str(pass_bool))
            total = 4

        self.pass_total = total
        return total

    def get_grades(self):
        return self.grade_total + self.pass_total


            # todo:Advsiory pays 4 dollars
