from zipfile import ZipFile

with ZipFile("C:/Users/User/Nika/course_work_proj/operations.zip", "r") as myzip:
    content = myzip.extract("operations.json")
