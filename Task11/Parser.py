import pandas as pd


class Parser:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path, delimiter=';', na_values=[''])

    def __str__(self):
        return str(self.data)

    def table_size(self):
        return f"Number of rows: {len(self.data)}\nNumber of columns: {len(self.data.columns)}"

    def column_names_and_types(self):
        return self.data.dtypes

    def students_who_passed_all(self):
        return self.data.dropna()

    def get_passed_students_surnames(self):
        passed_all = self.students_who_passed_all()
        surnames = passed_all['Student'].tolist()
        return str(surnames) + f"\nNumber of students who passed all: {len(surnames)}"

    def fill_nan_with_zeros(self):
        return self.data.fillna(0, inplace=True)

    def students_with_test_score_over_30(self):
        mask = self.data['Test'] > 30
        return self.data[mask]

    def convert_test_scores(self):
        self.data['Test'] = (self.data['Test'] * 12) / 100

    def add_lab_bonus(self):
        self.data['Lab1'] = self.data['Lab1'].apply(lambda x: 2 if x == '+' else 1 if x == '/' else 0)
        self.data['Lab2'] = self.data['Lab2'].apply(lambda x: 2 if x == '+' else 1 if x == '/' else 0)

    def create_lab(self, lab_name, lab_number):
        self.data[lab_name + lab_number] = self.data[lab_name]
        marks = self.data[lab_name].str.split('/', expand=True)
        if lab_number == "1":
            self.data[lab_name + lab_number] = marks[0]
        else:
            self.data[lab_name + lab_number] = marks[1]

    def change_to_numeric(self, column_name):
        self.data[column_name] = pd.to_numeric(self.data[column_name])

    def add_lab_column(self, lab_name, value):
        self.data[lab_name] = value

    def calculate_zalik(self, columns_to_sum):
        self.data['Zalik'] = self.data[columns_to_sum].sum(axis=1)

    def rename_columns(self, old_names, new_names):
        self.data.rename(columns=dict(zip(old_names, new_names)), inplace=True)

    def delete_column(self, column_name):
        self.data.drop(column_name, axis=1, inplace=True)

    def max_zalik(self):
        return self.data['Zalik'].max()

    def max_zalik_by_index(self):
        return self.data['Zalik'].idxmax()

    def max_zalik_student_info(self):
        return self.data.loc[self.max_zalik_by_index()]

    def max_zalik_student_surname(self):
        return self.max_zalik_student_info()['Student']

    def who_have_zalik(self):
        return self.data[self.data['Zalik'] >= 50]

    def count_who_have_zalik(self):
        return len(self.who_have_zalik())

    def sort_by_zalik(self):
        self.data = self.data.sort_values(by=['Zalik'], ascending=False)

    def find_students_lab1_score(self):
        mask = (self.data['Lab1'] == 1) | (self.data['Lab1'] == 0)
        return self.data[mask]['Student']

    def surnames_with_zalik(self):
        return self.data[['Student', 'Zalik']]
