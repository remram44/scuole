SCHEMA = {
    'staff-and-student-information': {
        'all_students_count': 'PETALLC',
        'african_american_count': 'PETBLAC',
        'african_american_percent': 'PETBLAP',
        'american_indian_count': '',
        'american_indian_percent': '',
        'asian_count': 'PETASIC',
        'asian_percent': 'PETASIP',
        'hispanic_count': 'PETHISC',
        'hispanic_percent': 'PETHISP',
        'pacific_islander_count': 'PETPCIC',
        'pacific_islander_percent': 'PETPCIP',
        'two_or_more_races_count': 'PETTWOC',
        'two_or_more_races_percent': 'PETTWOP',
        'white_count': 'PETWHIC',
        'white_percent': 'PETWHIP',
        'early_childhood_education_count': 'PETGEEC',
        'early_childhood_education_percent': 'CPETGEEP',
        'prek_count': 'PETGPKC',
        'prek_percent': 'PETGPKP',
        'kintergarten_count': 'CPETGKNC',
        'kindergarten_percent': 'CPETGKNP',
        'first_count': 'PETG01C',
        'first_percent': 'PETG01P',
        'second_count': 'PETG02C',
        'second_percent': 'PETG02P',
        'third_count': 'PETG03C',
        'third_percent': 'PETG03P',
        'fourth_count': 'PETG04C',
        'fourth_percent': 'PETG04P',
        'fifth_count': 'PETG05C',
        'fifth_percent': 'PETG05P',
        'sixth_count': 'PETG06C',
        'sixth_percent': 'PETG06P',
        'seventh_count': 'PETG07C',
        'seventh_percent': 'PETG07P',
        'eighth_count': 'PETG08C',
        'eighth_percent': 'PETG08P',
        'ninth_count': 'PETG09C',
        'ninth_percent': 'PETG09P',
        'tenth_count': 'PETG10C',
        'tenth_percent': 'PETG10P',
        'eleventh_count': 'PETG11C',
        'eleventh_percent': 'PETG11P',
        'twelfth_count': 'PETG12C',
        'twelfth_percent': 'PETG12P',
        'at_risk_count': 'PETRSKC',
        'at_risk_percent': 'PETRSKP',
    },
    # 'postsecondary-readiness-and-non-staar-performance-indicators': {
    #     'college_ready_graduates_english_13_african_american_count': '',
    #     'college_ready_graduates_english_13_african_american_percent': '',
    #     'college_ready_graduates_english_13_american_indian_count': '',
    #     'college_ready_graduates_english_13_american_indian_percent': '',
    #     'college_ready_graduates_english_13_asian_count': '',
    #     'college_ready_graduates_english_13_asian_percent': '',
    #     'college_ready_graduates_english_13_hispanic_count': '',
    #     'college_ready_graduates_english_13_hispanic_percent': '',
    #     'college_ready_graduates_english_13_pacific_islander_count': '',
    #     'college_ready_graduates_english_13_pacific_islander_percent': '',
    #     'college_ready_graduates_english_13_two_or_more_races_count': '',
    #     'college_ready_graduates_english_13_two_or_more_races_percent': '',
    #     'college_ready_graduates_english_13_white_count': '',
    #     'college_ready_graduates_english_13_white_percent': '',
    #     'college_ready_graduates_english_12_african_american_count': '',
    #     'college_ready_graduates_english_12_african_american_percent': '',
    #     'college_ready_graduates_english_12_american_indian_count': '',
    #     'college_ready_graduates_english_12_american_indian_percent': '',
    #     'college_ready_graduates_english_12_asian_count': '',
    #     'college_ready_graduates_english_12_asian_percent': '',
    #     'college_ready_graduates_english_12_hispanic_count': '',
    #     'college_ready_graduates_english_12_hispanic_percent': '',
    #     'college_ready_graduates_english_12_pacific_islander_count': '',
    #     'college_ready_graduates_english_12_pacific_islander_percent': '',
    #     'college_ready_graduates_english_12_two_or_more_races_count': '',
    #     'college_ready_graduates_english_12_two_or_more_races_percent': '',
    #     'college_ready_graduates_english_12_white_count': '',
    #     'college_ready_graduates_english_12_white_percent': '',
    #     'college_ready_graduates_math_13_african_american_count': '',
    #     'college_ready_graduates_math_13_african_american_percent': '',
    #     'college_ready_graduates_math_13_american_indian_count': '',
    #     'college_ready_graduates_math_13_american_indian_percent': '',
    #     'college_ready_graduates_math_13_asian_count': '',
    #     'college_ready_graduates_math_13_asian_percent': '',
    #     'college_ready_graduates_math_13_hispanic_count': '',
    #     'college_ready_graduates_math_13_hispanic_percent': '',
    #     'college_ready_graduates_math_13_pacific_islander_count': '',
    #     'college_ready_graduates_math_13_pacific_islander_percent': '',
    #     'college_ready_graduates_math_13_two_or_more_races_count': '',
    #     'college_ready_graduates_math_13_two_or_more_races_percent': '',
    #     'college_ready_graduates_math_13_white_count': '',
    #     'college_ready_graduates_math_13_white_percent': '',
    #     'college_ready_graduates_math_12_african_american_count': '',
    #     'college_ready_graduates_math_12_african_american_percent': '',
    #     'college_ready_graduates_math_12_american_indian_count': '',
    #     'college_ready_graduates_math_12_american_indian_percent': '',
    #     'college_ready_graduates_math_12_asian_count': '',
    #     'college_ready_graduates_math_12_asian_percent': '',
    #     'college_ready_graduates_math_12_hispanic_count': '',
    #     'college_ready_graduates_math_12_hispanic_percent': '',
    #     'college_ready_graduates_math_12_pacific_islander_count': '',
    #     'college_ready_graduates_math_12_pacific_islander_percent': '',
    #     'college_ready_graduates_math_12_two_or_more_races_count': '',
    #     'college_ready_graduates_math_12_two_or_more_races_percent': '',
    #     'college_ready_graduates_math_12_white_count': '',
    #     'college_ready_graduates_math_12_white_percent': '',
    #     'college_ready_graduates_both_13_african_american_count': '',
    #     'college_ready_graduates_both_13_african_american_percent': '',
    #     'college_ready_graduates_both_13_american_indian_count': '',
    #     'college_ready_graduates_both_13_american_indian_percent': '',
    #     'college_ready_graduates_both_13_asian_count': '',
    #     'college_ready_graduates_both_13_asian_percent': '',
    #     'college_ready_graduates_both_13_hispanic_count': '',
    #     'college_ready_graduates_both_13_hispanic_percent': '',
    #     'college_ready_graduates_both_13_pacific_islander_count': '',
    #     'college_ready_graduates_both_13_pacific_islander_percent': '',
    #     'college_ready_graduates_both_13_two_or_more_races_count': '',
    #     'college_ready_graduates_both_13_two_or_more_races_percent': '',
    #     'college_ready_graduates_both_13_white_count': '',
    #     'college_ready_graduates_both_13_white_percent': '',
    #     'college_ready_graduates_both_12_african_american_count': '',
    #     'college_ready_graduates_both_12_african_american_percent': '',
    #     'college_ready_graduates_both_12_american_indian_count': '',
    #     'college_ready_graduates_both_12_american_indian_percent': '',
    #     'college_ready_graduates_both_12_asian_count': '',
    #     'college_ready_graduates_both_12_asian_percent': '',
    #     'college_ready_graduates_both_12_hispanic_count': '',
    #     'college_ready_graduates_both_12_hispanic_percent': '',
    #     'college_ready_graduates_both_12_pacific_islander_count': '',
    #     'college_ready_graduates_both_12_pacific_islander_percent': '',
    #     'college_ready_graduates_both_12_two_or_more_races_count': '',
    #     'college_ready_graduates_both_12_two_or_more_races_percent': '',
    #     'college_ready_graduates_both_12_white_count': '',
    #     'college_ready_graduates_both_12_white_percent': '',

    # }
}
