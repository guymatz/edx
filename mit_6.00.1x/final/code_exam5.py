#!/usr/bin/python


class courseInfo(object):

    def __init__(self, courseName):
        self.courseName = courseName
        self.psetsDone = []
        self.grade = "No Grade"
        
    def setPset(self, pset, score):
        self.psetsDone.append((pset, score))
        
    def getPset(self, pset):
        for (p, score) in self.psetsDone:
            if p == pset:
                return score

    def setGrade(self, grade):
        if self.grade == "No Grade":
            self.grade = grade

    def getGrade(self):
        return self.grade



class edx(object):
    def __init__(self, courses):
        self.myCourses = []
        for course in courses:
            self.myCourses.append(courseInfo(course))

    def _get_courseID_by_name(self, course_name):
        for c in range(len(self.myCourses)):
            if self.myCourses[c].courseName == course_name:
                return c
        return None

    def setGrade(self, grade, course="6.01x"):
        """
        grade: integer greater than or equal to 0 and less than or equal to 100
        course: string 

        This method sets the grade in the courseInfo object named by `course`.   

        If `course` was not part of the initialization, then no grade is set, and no
        error is thrown.

        The method does not return a value.
        """
        #   fill in code to set the grade
        #edX.setGrade(100)
        if self._get_courseID_by_name(course) is not None:
            self.myCourses[self._get_courseID_by_name(course)].setGrade(grade)

    def getGrade(self, course="6.02x"):
        """
        course: string 

        This method gets the grade in the the courseInfo object named by `course`.

        returns: the integer grade for `course`.  
        If `course` was not part of the initialization, returns -1.
        """
        #   fill in code to get the grade
        if self._get_courseID_by_name(course) is not None:
            return self.myCourses[self._get_courseID_by_name(course)].getGrade()
        else:
            return -1

    def setPset(self, pset, score, course="6.00x"):
        """
        pset: a string or a number
        score: an integer between 0 and 100
        course: string

        The `score` of the specified `pset` is set for the
        given `course` using the courseInfo object.

        If `course` is not part of the initialization, then no pset score is set,
        and no error is thrown.
        """
        #   fill in code to set the pset
        if self._get_courseID_by_name(course) is not None:
            self.myCourses[self._get_courseID_by_name(course)].setPset(pset, score)

    def getPset(self, pset, course="6.00x"):
        """
        pset: a string or a number
        course: string        

        returns: The score of the specified `pset` of the given
        `course` using the courseInfo object.
        If `course` was not part of the initialization, returns -1.
        """
        #   fill in code to get the pset
        if self._get_courseID_by_name(course) is not None:
            return self.myCourses[self._get_courseID_by_name(course)].getPset(pset)
        else:
            return -1


edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setPset(1,100)
edX.setPset(2,100,"6.00x")
edX.setPset(2,90,"6.00x")

edX.setGrade(100)

for c in ["6.00x","6.01x","6.02x", "qwert"]:
    edX.setGrade(90,c)

for c in ["6.00x","6.01x","6.02x", "qwert"]:
    print edX.getGrade(c)


edX = edx( ["6.00x","6.01x","6.02x"] )
edX.setPset(2, 100,"6.02x")
edX.setPset(2, 100,"2.01x")
print edX.getPset(2, "6.02x")
#100
print edX.getPset(3, "6.02x")
#None
print edX.getPset(2, "2.01x")
#-1
