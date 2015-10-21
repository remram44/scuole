# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models


class StaffStudentBase(models.Model):
    """
    An abstract model representing staff and student data commonly tracked
    across all entities in TEA data. Meant to be used with StatsBase by other
    apps for establishing their stats models.

    """

    # Student counts
    all_students_count = models.IntegerField(
        'Number of students', null=True, blank=True)
    african_american_count = models.IntegerField(
        'Number of African American students', null=True, blank=True)
    american_indian_count = models.IntegerField(
        'Number of American Indian students', null=True, blank=True)
    asian_count = models.IntegerField(
        'Number of Asian students', null=True, blank=True)
    hispanic_count = models.IntegerField(
        'Number of Hispanic students', null=True, blank=True)
    pacific_islander_count = models.IntegerField(
        'Number of Pacific Islander students', null=True, blank=True)
    two_or_more_races_count = models.IntegerField(
        'Number of Two or More Races students', null=True, blank=True)
    white_count = models.IntegerField(
        'Number of White students', null=True, blank=True)
    early_childhood_education_count = models.IntegerField(
        'Number of early childhood education students', null=True, blank=True)
    prek_count = models.IntegerField(
        'Number of pre-K students', null=True, blank=True)
    kindergarten_count = models.IntegerField(
        'Number of kindergarten students', null=True, blank=True)
    first_count = models.IntegerField(
        'Number of first grade students', null=True, blank=True)
    second_count = models.IntegerField(
        'Number of second grade students', null=True, blank=True)
    third_count = models.IntegerField(
        'Number of third grade students', null=True, blank=True)
    fourth_count = models.IntegerField(
        'Number of fourth grade students', null=True, blank=True)
    fifth_count = models.IntegerField(
        'Number of fifth grade students', null=True, blank=True)
    sixth_count = models.IntegerField(
        'Number of sixth grade students', null=True, blank=True)
    seventh_count = models.IntegerField(
        'Number of seventh grade students', null=True, blank=True)
    eighth_count = models.IntegerField(
        'Number of eigth grade students', null=True, blank=True)
    ninth_count = models.IntegerField(
        'Number of ninth grade students', null=True, blank=True)
    tenth_count = models.IntegerField(
        'Number of tenth grade students', null=True, blank=True)
    eleventh_count = models.IntegerField(
        'Number of eleventh grade students', null=True, blank=True)
    twelfth_count = models.IntegerField(
        'Number of twelfth grade students', null=True, blank=True)
    at_risk_count = models.IntegerField(
        'Number of at risk students', null=True, blank=True)

    # Student percents
    african_american_percent = models.FloatField(
        'Percent of African American students', null=True, blank=True)
    american_indian_percent = models.FloatField(
        'Percent of American Indian students', null=True, blank=True)
    asian_percent = models.FloatField(
        'Percent of Asian students', null=True, blank=True)
    hispanic_percent = models.FloatField(
        'Percent of Hispanic students', null=True, blank=True)
    pacific_islander_percent = models.FloatField(
        'Percent of Pacific Islander students', null=True, blank=True)
    two_or_more_races_percent = models.FloatField(
        'Percent of Two or More Races students', null=True, blank=True)
    white_percent = models.FloatField(
        'Percent of White students', null=True, blank=True)
    early_childhood_education_percent = models.FloatField(
        'Percent of early childhood education students', null=True, blank=True)
    prek_percent = models.FloatField(
        'Percent of pre-K students', null=True, blank=True)
    kindergarten_percent = models.FloatField(
        'Percent of kindergarten students', null=True, blank=True)
    first_percent = models.FloatField(
        'Percent of first grade students', null=True, blank=True)
    second_percent = models.FloatField(
        'Percent of second grade students', null=True, blank=True)
    third_percent = models.FloatField(
        'Percent of third grade students', null=True, blank=True)
    fourth_percent = models.FloatField(
        'Percent of fourth grade students', null=True, blank=True)
    fifth_percent = models.FloatField(
        'Percent of fifth grade students', null=True, blank=True)
    sixth_percent = models.FloatField(
        'Percent of sixth grade students', null=True, blank=True)
    seventh_percent = models.FloatField(
        'Percent of seventh grade students', null=True, blank=True)
    eighth_percent = models.FloatField(
        'Percent of eighth grade students', null=True, blank=True)
    ninth_percent = models.FloatField(
        'Percent of ninth grade students', null=True, blank=True)
    tenth_percent = models.FloatField(
        'Percent of tenth grade students', null=True, blank=True)
    eleventh_percent = models.FloatField(
        'Percent of eleventh grade students', null=True)
    twelfth_percent = models.FloatField(
        'Percent of twelfth grade students', null=True, blank=True)
    at_risk_percent = models.FloatField(
        'Percent of at risk students', null=True, blank=True)

    bilingual_esl_count = models.IntegerField(
        'Number of students enrolled in bilingual/ESL program',
        null=True, blank=True)
    career_technical_education_count = models.IntegerField(
        'Number of students enrolled in career and technical education program',
        null=True, blank=True)
    gifted_and_talented_count = models.IntegerField(
        'Number of students enrolled in gifted and talented program',
        null=True, blank=True)
    special_education_count = models.IntegerField(
        'Number of students enrolled in special education program',
        null=True, blank=True)

    bilingual_esl_percent = models.FloatField(
        'Percent of students enrolled in bilingual/ESL program',
        null=True, blank=True)
    career_technical_education_percent = models.FloatField(
        'Percent of students enrolled in career and technical education program',
        null=True, blank=True)
    gifted_and_talented_percent = models.FloatField(
        'Percent of students enrolled in gifted and talented program',
        null=True, blank=True)
    special_education_percent = models.FloatField(
        'Percent of students enrolled in special education program',
        null=True, blank=True)

    class_size_avg_kindergarten = models.FloatField(
        'Average kindergarten grade class size', null=True, blank=True)
    class_size_avg_first = models.FloatField(
        'Average first grade class size', null=True, blank=True)
    class_size_avg_second = models.FloatField(
        'Average second grade class size', null=True, blank=True)
    class_size_avg_third = models.FloatField(
        'Average third grade class size', null=True, blank=True)
    class_size_avg_fourth = models.FloatField(
        'Average fourth grade class size', null=True, blank=True)
    class_size_avg_fifth = models.FloatField(
        'Average fifth grade class size', null=True, blank=True)
    class_size_avg_sixth = models.FloatField(
        'Average sixth grade class size', null=True, blank=True)
    class_size_avg_mixed_elementary = models.FloatField(
        'Average mixed elementary class size', null=True, blank=True)
    class_size_avg_secondary_english = models.FloatField(
        'Average secondary English class size', null=True, blank=True)
    class_size_avg_secondary_foreign_language = models.FloatField(
        'Average secondary foreign language class size', null=True, blank=True)
    class_size_avg_secondary_math = models.FloatField(
        'Average secondary math class size', null=True, blank=True)
    class_size_avg_secondary_science = models.FloatField(
        'Average secondary science class size', null=True, blank=True)
    class_size_avg_secondary_social_studies = models.FloatField(
        'Average secondary social studies class size', null=True, blank=True)

    students_per_teacher = models.FloatField(
        'Number of students per teacher', null=True, blank=True)
    teacher_avg_tenure = models.FloatField(
        'Average tenure of teachers at entity', null=True, blank=True)
    teacher_avg_experience = models.FloatField(
        'Average years of experience at entity', null=True, blank=True)
    teacher_avg_base_salary = models.DecimalField(
        'Average teacher salary at entity', max_digits=10,
        decimal_places=2, null=True, blank=True)
    teacher_avg_beginning_salary = models.DecimalField(
        'Average teacher beginning salary at entity', max_digits=10,
        decimal_places=2, null=True, blank=True)
    teacher_avg_1_to_5_year_salary = models.DecimalField(
        'Average salary for teachers with 1-5 years experience',
        max_digits=10, decimal_places=2, null=True, blank=True)
    teacher_avg_6_to_10_year_salary = models.DecimalField(
        'Average salary for teachers with 6-10 years experience',
        max_digits=10, decimal_places=2, null=True, blank=True)
    teacher_avg_11_to_20_year_salary = models.DecimalField(
        'Average salary for teachers with 11-20 years experience',
        max_digits=10, decimal_places=2, null=True, blank=True)
    teacher_avg_20_plus_year_salary = models.DecimalField(
        'Average salary for teachers with over 20 years experience',
        max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        abstract = True
