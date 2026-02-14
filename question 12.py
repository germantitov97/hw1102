grades = [85, 90, 78, 92, 88]

_backup = grades.copy()

grades.clear()

print(grades)
print(_backup)

grades2 = [95 ,100]

gradesnew = _backup + grades2
print(gradesnew)

_backup.extend(grades2)
print(_backup)