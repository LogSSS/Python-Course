import Parser as p

# 1
parser = p.Parser("KN-4.csv")

# 2
print('-' * 30)
print(parser)

# 3
print('-' * 30)
print(parser.table_size())

# 4
print('-' * 30)
print(parser.column_names_and_types())

# 5
print('-' * 30)
print(parser.students_who_passed_all())

# 6
print('-' * 30)
print(parser.get_passed_students_surnames())

# 7
print('-' * 30)
parser.fill_nan_with_zeros()
print(parser)

# 8
print('-' * 30)
print(parser.students_with_test_score_over_30())

# 9
print('-' * 30)
parser.convert_test_scores()
print(parser)

# 10
print('-' * 30)
parser.add_lab_bonus()
print(parser)

# 11
print('-' * 30)
parser.create_lab('Lab7', "1")
parser.create_lab('Lab7', "2")
print(parser)

# 12
print('-' * 30)
parser.change_to_numeric('Lab71')
parser.change_to_numeric('Lab72')

# 13
print('-' * 30)
parser.add_lab_column('Lab3', 2)
parser.change_to_numeric('Lab3')
print(parser)

# 14
print('-' * 30)
parser.calculate_zalik(['Lab1', 'Lab2', 'Lab3', 'Lab71', 'Lab72', 'Test', 'KR1'])
print(parser)

# 15
print('-' * 30)
parser.rename_columns(['Lab71', 'Lab72'], ['Lab8', 'Lab9'])
print(parser)

# 16
print('-' * 30)
parser.delete_column('Lab3')
print(parser)

# 17
print('-' * 30)
print(parser.max_zalik())

# 18
print('-' * 30)
print(parser.max_zalik_by_index())

# 19
print('-' * 30)
print(parser.max_zalik_student_info())

# 20
print('-' * 30)
print(parser.max_zalik_student_surname())

# 21
print('-' * 30)
print(parser.who_have_zalik())

# 22
print('-' * 30)
print(parser.count_who_have_zalik())

# 23
print('-' * 30)
parser.sort_by_zalik()
print(parser)

# 24
print('-' * 30)
print(parser.find_students_lab1_score())

# 25
print('-' * 30)
print(parser.surnames_with_zalik())

print('-' * 30)
