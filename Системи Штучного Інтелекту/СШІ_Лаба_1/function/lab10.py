from lab10.ant import Ant


def write_stats_to_file(file_name, statistics, field_name):
    statistics_list = sorted(statistics.keys(), key=lambda x: (statistics[x]['distance']))

    file = open(file_name, 'w')
    var = True
    our_max = 0
    empty_ways = ''
    for st in statistics_list:
        item = statistics[st]
        if var:
            our_max = item['distance']
            var = False

        if our_max == item['distance']:
            line = f"{st}\nКількість мурах, які пройшли цим маршрутом: {item[field_name]}\n" \
                   f"Відстань: {item['distance']}\n\n"
            if item[field_name] != 0:
                file.write(line)
            else:
                empty_ways += line
        else:
            break
    if empty_ways != '':
        file.write(empty_ways)
    file.close()


items1 = {
    1: 'Вінниця',
    2: 'Дніпропетровськ',
    3: 'Донецьк',
    4: 'Житомир',
    5: 'Запоріжжя',
}
combinations1 = [
    {
        'id': 1,
        'connections': [
            {
                'id': 2,
                'distance': 645
            },
            {
                'id': 3,
                'distance': 868
            },
            {
                'id': 4,
                'distance': 125
            },
            {
                'id': 5,
                'distance': 748
            },
        ]
    },
    {
        'id': 2,
        'connections': [
            {
                'id': 1,
                'distance': 645
            },
            {
                'id': 3,
                'distance': 252
            },
            {
                'id': 4,
                'distance': 664
            },
            {
                'id': 5,
                'distance': 81
            },
        ]
    },
    {
        'id': 3,
        'connections': [
            {
                'id': 1,
                'distance': 868
            },
            {
                'id': 2,
                'distance': 252
            },
            {
                'id': 4,
                'distance': 858
            },
            {
                'id': 5,
                'distance': 217
            },
        ]
    },
    {
        'id': 4,
        'connections': [
            {
                'id': 1,
                'distance': 125
            },
            {
                'id': 2,
                'distance': 664
            },
            {
                'id': 3,
                'distance': 858
            },
            {
                'id': 5,
                'distance': 738
            },
        ]
    },
    {
        'id': 5,
        'connections': [
            {
                'id': 1,
                'distance': 748
            },
            {
                'id': 2,
                'distance': 81
            },
            {
                'id': 3,
                'distance': 217
            },
            {
                'id': 4,
                'distance': 738
            },
        ]
    },
]

items2 = {
    1: 'Вінниця',
    2: 'Дніпропетровськ',
    3: 'Донецьк',
    4: 'Житомир',
    5: 'Запоріжжя',
    6: 'Ів-Франківськ',
    7: 'Київ',
    8: 'Кіровоград',
    9: 'Луганськ',
    10: 'Луцьк',
}
combinations2 = [
    {
        'id': 1,
        'connections': [
            {
                'id': 2,
                'distance': 645
            },
            {
                'id': 3,
                'distance': 868
            },
            {
                'id': 4,
                'distance': 125
            },
            {
                'id': 5,
                'distance': 748
            },
            {
                'id': 6,
                'distance': 366
            },
            {
                'id': 7,
                'distance': 256
            },
            {
                'id': 8,
                'distance': 316
            },
            {
                'id': 9,
                'distance': 1057
            },
            {
                'id': 10,
                'distance': 382
            },
        ]
    },
    {
        'id': 2,
        'connections': [
            {
                'id': 1,
                'distance': 645
            },
            {
                'id': 3,
                'distance': 252
            },
            {
                'id': 4,
                'distance': 664
            },
            {
                'id': 5,
                'distance': 81
            },
            {
                'id': 6,
                'distance': 901
            },
            {
                'id': 7,
                'distance': 533
            },
            {
                'id': 8,
                'distance': 294
            },
            {
                'id': 9,
                'distance': 394
            },
            {
                'id': 10,
                'distance': 805
            },
        ]
    },
    {
        'id': 3,
        'connections': [
            {
                'id': 1,
                'distance': 868
            },
            {
                'id': 2,
                'distance': 252
            },
            {
                'id': 4,
                'distance': 858
            },
            {
                'id': 5,
                'distance': 217
            },
            {
                'id': 6,
                'distance': 1171
            },
            {
                'id': 7,
                'distance': 727
            },
            {
                'id': 8,
                'distance': 520
            },
            {
                'id': 9,
                'distance': 148
            },
            {
                'id': 10,
                'distance': 1111
            },
        ]
    },
    {
        'id': 4,
        'connections': [
            {
                'id': 1,
                'distance': 125
            },
            {
                'id': 2,
                'distance': 664
            },
            {
                'id': 3,
                'distance': 858
            },
            {
                'id': 5,
                'distance': 738
            },
            {
                'id': 6,
                'distance': 431
            },
            {
                'id': 7,
                'distance': 131
            },
            {
                'id': 8,
                'distance': 407
            },
            {
                'id': 9,
                'distance': 1182
            },
            {
                'id': 10,
                'distance': 257
            },
        ]
    },
    {
        'id': 5,
        'connections': [
            {
                'id': 1,
                'distance': 748
            },
            {
                'id': 2,
                'distance': 81
            },
            {
                'id': 3,
                'distance': 217
            },
            {
                'id': 4,
                'distance': 738
            },
            {
                'id': 6,
                'distance': 1119
            },
            {
                'id': 7,
                'distance': 607
            },
            {
                'id': 8,
                'distance': 303
            },
            {
                'id': 9,
                'distance': 365
            },
            {
                'id': 10,
                'distance': 681
            },
        ]
    },
    {
        'id': 6,
        'connections': [
            {
                'id': 1,
                'distance': 366
            },
            {
                'id': 2,
                'distance': 901
            },
            {
                'id': 3,
                'distance': 1171
            },
            {
                'id': 4,
                'distance': 431
            },
            {
                'id': 5,
                'distance': 1119
            },
            {
                'id': 7,
                'distance': 561
            },
            {
                'id': 8,
                'distance': 618
            },
            {
                'id': 9,
                'distance': 1402
            },
            {
                'id': 10,
                'distance': 328
            },
        ]
    },
    {
        'id': 7,
        'connections': [
            {
                'id': 1,
                'distance': 256
            },
            {
                'id': 2,
                'distance': 533
            },
            {
                'id': 3,
                'distance': 727
            },
            {
                'id': 4,
                'distance': 131
            },
            {
                'id': 5,
                'distance': 607
            },
            {
                'id': 6,
                'distance': 561
            },
            {
                'id': 8,
                'distance': 298
            },
            {
                'id': 9,
                'distance': 811
            },
            {
                'id': 10,
                'distance': 388
            },
        ]
    },
    {
        'id': 8,
        'connections': [
            {
                'id': 1,
                'distance': 316
            },
            {
                'id': 2,
                'distance': 294
            },
            {
                'id': 3,
                'distance': 520
            },
            {
                'id': 4,
                'distance': 407
            },
            {
                'id': 5,
                'distance': 303
            },
            {
                'id': 6,
                'distance': 618
            },
            {
                'id': 7,
                'distance': 298
            },
            {
                'id': 9,
                'distance': 668
            },
            {
                'id': 10,
                'distance': 664
            },
        ]
    },
    {
        'id': 9,
        'connections': [
            {
                'id': 1,
                'distance': 1057
            },
            {
                'id': 2,
                'distance': 394
            },
            {
                'id': 3,
                'distance': 148
            },
            {
                'id': 4,
                'distance': 1182
            },
            {
                'id': 5,
                'distance': 365
            },
            {
                'id': 6,
                'distance': 1402
            },
            {
                'id': 7,
                'distance': 811
            },
            {
                'id': 8,
                'distance': 668
            },
            {
                'id': 10,
                'distance': 1199
            },
        ]
    },
    {
        'id': 10,
        'connections': [
            {
                'id': 1,
                'distance': 382
            },
            {
                'id': 2,
                'distance': 805
            },
            {
                'id': 3,
                'distance': 1111
            },
            {
                'id': 4,
                'distance': 257
            },
            {
                'id': 5,
                'distance': 681
            },
            {
                'id': 6,
                'distance': 328
            },
            {
                'id': 7,
                'distance': 388
            },
            {
                'id': 8,
                'distance': 664
            },
            {
                'id': 9,
                'distance': 1199
            },
        ]
    },
]

items3 = {
    1: 'Вінниця',
    2: 'Дніпропетровськ',
    3: 'Донецьк',
    4: 'Житомир',
    5: 'Запоріжжя',
    6: 'Ів-Франківськ',
    7: 'Київ',
    8: 'Кіровоград',
    9: 'Луганськ',
    10: 'Луцьк',
    11: 'Львів',
    12: 'Миколаїв',
    13: 'Одеса',
    14: 'Полтава',
    15: 'Рівне',
    16: 'Сімферополь',
    17: 'Суми',
    18: 'Тернопіль',
    19: 'Ужгород',
    20: 'Харків',
    21: 'Херсон',
    22: 'Хмельницький',
    23: 'Черкаси',
    24: 'Чернівці',
    25: 'Чернігів',
}
combinations3 = [
    {
        'id': 1,
        'connections': [
            {
                'id': 2,
                'distance': 645
            },
            {
                'id': 3,
                'distance': 868
            },
            {
                'id': 4,
                'distance': 125
            },
            {
                'id': 5,
                'distance': 748
            },
            {
                'id': 6,
                'distance': 366
            },
            {
                'id': 7,
                'distance': 256
            },
            {
                'id': 8,
                'distance': 316
            },
            {
                'id': 9,
                'distance': 1057
            },
            {
                'id': 10,
                'distance': 382
            },
            {
                'id': 11,
                'distance': 360
            },
            {
                'id': 12,
                'distance': 471
            },
            {
                'id': 13,
                'distance': 428
            },
            {
                'id': 14,
                'distance': 593
            },
            {
                'id': 15,
                'distance': 311
            },
            {
                'id': 16,
                'distance': 844
            },
            {
                'id': 17,
                'distance': 602
            },
            {
                'id': 18,
                'distance': 232
            },
            {
                'id': 19,
                'distance': 575
            },
            {
                'id': 20,
                'distance': 734
            },
            {
                'id': 21,
                'distance': 521
            },
            {
                'id': 22,
                'distance': 120
            },
            {
                'id': 23,
                'distance': 343
            },
            {
                'id': 24,
                'distance': 312
            },
            {
                'id': 25,
                'distance': 396
            },
        ]
    },
    {
        'id': 2,
        'connections': [
            {
                'id': 1,
                'distance': 645
            },
            {
                'id': 3,
                'distance': 252
            },
            {
                'id': 4,
                'distance': 664
            },
            {
                'id': 5,
                'distance': 81
            },
            {
                'id': 6,
                'distance': 901
            },
            {
                'id': 7,
                'distance': 533
            },
            {
                'id': 8,
                'distance': 294
            },
            {
                'id': 9,
                'distance': 394
            },
            {
                'id': 10,
                'distance': 805
            },
            {
                'id': 11,
                'distance': 975
            },
            {
                'id': 12,
                'distance': 343
            },
            {
                'id': 13,
                'distance': 468
            },
            {
                'id': 14,
                'distance': 196
            },
            {
                'id': 15,
                'distance': 957
            },
            {
                'id': 16,
                'distance': 446
            },
            {
                'id': 17,
                'distance': 430
            },
            {
                'id': 18,
                'distance': 877
            },
            {
                'id': 19,
                'distance': 1130
            },
            {
                'id': 20,
                'distance': 213
            },
            {
                'id': 21,
                'distance': 376
            },
            {
                'id': 22,
                'distance': 765
            },
            {
                'id': 23,
                'distance': 324
            },
            {
                'id': 24,
                'distance': 891
            },
            {
                'id': 25,
                'distance': 672
            },
        ]
    },
    {
        'id': 3,
        'connections': [
            {
                'id': 1,
                'distance': 868
            },
            {
                'id': 2,
                'distance': 252
            },
            {
                'id': 4,
                'distance': 858
            },
            {
                'id': 5,
                'distance': 217
            },
            {
                'id': 6,
                'distance': 1171
            },
            {
                'id': 7,
                'distance': 727
            },
            {
                'id': 8,
                'distance': 520
            },
            {
                'id': 9,
                'distance': 148
            },
            {
                'id': 10,
                'distance': 1111
            },
            {
                'id': 11,
                'distance': 1221
            },
            {
                'id': 12,
                'distance': 611
            },
            {
                'id': 13,
                'distance': 731
            },
            {
                'id': 14,
                'distance': 390
            },
            {
                'id': 15,
                'distance': 1045
            },
            {
                'id': 16,
                'distance': 591
            },
            {
                'id': 17,
                'distance': 706
            },
            {
                'id': 18,
                'distance': 1100
            },
            {
                'id': 19,
                'distance': 1391
            },
            {
                'id': 20,
                'distance': 335
            },
            {
                'id': 21,
                'distance': 560
            },
            {
                'id': 22,
                'distance': 988
            },
            {
                'id': 23,
                'distance': 547
            },
            {
                'id': 24,
                'distance': 1141
            },
            {
                'id': 25,
                'distance': 867
            },
        ]
    },
    {
        'id': 4,
        'connections': [
            {
                'id': 1,
                'distance': 125
            },
            {
                'id': 2,
                'distance': 664
            },
            {
                'id': 3,
                'distance': 858
            },
            {
                'id': 5,
                'distance': 738
            },
            {
                'id': 6,
                'distance': 431
            },
            {
                'id': 7,
                'distance': 131
            },
            {
                'id': 8,
                'distance': 407
            },
            {
                'id': 9,
                'distance': 1182
            },
            {
                'id': 10,
                'distance': 257
            },
            {
                'id': 11,
                'distance': 423
            },
            {
                'id': 12,
                'distance': 677
            },
            {
                'id': 13,
                'distance': 557
            },
            {
                'id': 14,
                'distance': 468
            },
            {
                'id': 15,
                'distance': 187
            },
            {
                'id': 16,
                'distance': 803
            },
            {
                'id': 17,
                'distance': 477
            },
            {
                'id': 18,
                'distance': 298
            },
            {
                'id': 19,
                'distance': 671
            },
            {
                'id': 20,
                'distance': 690
            },
            {
                'id': 21,
                'distance': 624
            },
            {
                'id': 22,
                'distance': 185
            },
            {
                'id': 23,
                'distance': 321
            },
            {
                'id': 24,
                'distance': 389
            },
            {
                'id': 25,
                'distance': 271
            },
        ]
    },
    {
        'id': 5,
        'connections': [
            {
                'id': 1,
                'distance': 748
            },
            {
                'id': 2,
                'distance': 81
            },
            {
                'id': 3,
                'distance': 217
            },
            {
                'id': 4,
                'distance': 738
            },
            {
                'id': 6,
                'distance': 1119
            },
            {
                'id': 7,
                'distance': 607
            },
            {
                'id': 8,
                'distance': 303
            },
            {
                'id': 9,
                'distance': 365
            },
            {
                'id': 10,
                'distance': 681
            },
            {
                'id': 11,
                'distance': 833
            },
            {
                'id': 12,
                'distance': 377
            },
            {
                'id': 13,
                'distance': 497
            },
            {
                'id': 14,
                'distance': 270
            },
            {
                'id': 15,
                'distance': 925
            },
            {
                'id': 16,
                'distance': 365
            },
            {
                'id': 17,
                'distance': 477
            },
            {
                'id': 18,
                'distance': 977
            },
            {
                'id': 19,
                'distance': 1488
            },
            {
                'id': 20,
                'distance': 287
            },
            {
                'id': 21,
                'distance': 297
            },
            {
                'id': 22,
                'distance': 875
            },
            {
                'id': 23,
                'distance': 405
            },
            {
                'id': 24,
                'distance': 957
            },
            {
                'id': 25,
                'distance': 747
            },
        ]
    },
    {
        'id': 6,
        'connections': [
            {
                'id': 1,
                'distance': 366
            },
            {
                'id': 2,
                'distance': 901
            },
            {
                'id': 3,
                'distance': 1171
            },
            {
                'id': 4,
                'distance': 431
            },
            {
                'id': 5,
                'distance': 1119
            },
            {
                'id': 7,
                'distance': 561
            },
            {
                'id': 8,
                'distance': 618
            },
            {
                'id': 9,
                'distance': 1402
            },
            {
                'id': 10,
                'distance': 328
            },
            {
                'id': 11,
                'distance': 135
            },
            {
                'id': 12,
                'distance': 747
            },
            {
                'id': 13,
                'distance': 627
            },
            {
                'id': 14,
                'distance': 898
            },
            {
                'id': 15,
                'distance': 296
            },
            {
                'id': 16,
                'distance': 1070
            },
            {
                'id': 17,
                'distance': 908
            },
            {
                'id': 18,
                'distance': 134
            },
            {
                'id': 19,
                'distance': 280
            },
            {
                'id': 20,
                'distance': 1040
            },
            {
                'id': 21,
                'distance': 798
            },
            {
                'id': 22,
                'distance': 246
            },
            {
                'id': 23,
                'distance': 709
            },
            {
                'id': 24,
                'distance': 143
            },
            {
                'id': 25,
                'distance': 701
            },
        ]
    },
    {
        'id': 7,
        'connections': [
            {
                'id': 1,
                'distance': 256
            },
            {
                'id': 2,
                'distance': 533
            },
            {
                'id': 3,
                'distance': 727
            },
            {
                'id': 4,
                'distance': 131
            },
            {
                'id': 5,
                'distance': 607
            },
            {
                'id': 6,
                'distance': 561
            },
            {
                'id': 8,
                'distance': 298
            },
            {
                'id': 9,
                'distance': 811
            },
            {
                'id': 10,
                'distance': 388
            },
            {
                'id': 11,
                'distance': 550
            },
            {
                'id': 12,
                'distance': 490
            },
            {
                'id': 13,
                'distance': 489
            },
            {
                'id': 14,
                'distance': 337
            },
            {
                'id': 15,
                'distance': 318
            },
            {
                'id': 16,
                'distance': 972
            },
            {
                'id': 17,
                'distance': 346
            },
            {
                'id': 18,
                'distance': 427
            },
            {
                'id': 19,
                'distance': 806
            },
            {
                'id': 20,
                'distance': 478
            },
            {
                'id': 21,
                'distance': 551
            },
            {
                'id': 22,
                'distance': 315
            },
            {
                'id': 23,
                'distance': 190
            },
            {
                'id': 24,
                'distance': 538
            },
            {
                'id': 25,
                'distance': 149
            },
        ]
    },
    {
        'id': 8,
        'connections': [
            {
                'id': 1,
                'distance': 316
            },
            {
                'id': 2,
                'distance': 294
            },
            {
                'id': 3,
                'distance': 520
            },
            {
                'id': 4,
                'distance': 407
            },
            {
                'id': 5,
                'distance': 303
            },
            {
                'id': 6,
                'distance': 618
            },
            {
                'id': 7,
                'distance': 298
            },
            {
                'id': 9,
                'distance': 668
            },
            {
                'id': 10,
                'distance': 664
            },
            {
                'id': 11,
                'distance': 710
            },
            {
                'id': 12,
                'distance': 174
            },
            {
                'id': 13,
                'distance': 294
            },
            {
                'id': 14,
                'distance': 246
            },
            {
                'id': 15,
                'distance': 627
            },
            {
                'id': 16,
                'distance': 570
            },
            {
                'id': 17,
                'distance': 506
            },
            {
                'id': 18,
                'distance': 547
            },
            {
                'id': 19,
                'distance': 883
            },
            {
                'id': 20,
                'distance': 387
            },
            {
                'id': 21,
                'distance': 225
            },
            {
                'id': 22,
                'distance': 435
            },
            {
                'id': 23,
                'distance': 126
            },
            {
                'id': 24,
                'distance': 637
            },
            {
                'id': 25,
                'distance': 363
            },
        ]
    },
    {
        'id': 9,
        'connections': [
            {
                'id': 1,
                'distance': 1057
            },
            {
                'id': 2,
                'distance': 394
            },
            {
                'id': 3,
                'distance': 148
            },
            {
                'id': 4,
                'distance': 1182
            },
            {
                'id': 5,
                'distance': 365
            },
            {
                'id': 6,
                'distance': 1402
            },
            {
                'id': 7,
                'distance': 811
            },
            {
                'id': 8,
                'distance': 668
            },
            {
                'id': 10,
                'distance': 1199
            },
            {
                'id': 11,
                'distance': 379
            },
            {
                'id': 12,
                'distance': 857
            },
            {
                'id': 13,
                'distance': 977
            },
            {
                'id': 14,
                'distance': 474
            },
            {
                'id': 15,
                'distance': 1129
            },
            {
                'id': 16,
                'distance': 739
            },
            {
                'id': 17,
                'distance': 253
            },
            {
                'id': 18,
                'distance': 1289
            },
            {
                'id': 19,
                'distance': 1539
            },
            {
                'id': 20,
                'distance': 333
            },
            {
                'id': 21,
                'distance': 806
            },
            {
                'id': 22,
                'distance': 1177
            },
            {
                'id': 23,
                'distance': 706
            },
            {
                'id': 24,
                'distance': 1292
            },
            {
                'id': 25,
                'distance': 951
            },
        ]
    },
    {
        'id': 10,
        'connections': [
            {
                'id': 1,
                'distance': 382
            },
            {
                'id': 2,
                'distance': 805
            },
            {
                'id': 3,
                'distance': 1111
            },
            {
                'id': 4,
                'distance': 257
            },
            {
                'id': 5,
                'distance': 681
            },
            {
                'id': 6,
                'distance': 328
            },
            {
                'id': 7,
                'distance': 388
            },
            {
                'id': 8,
                'distance': 664
            },
            {
                'id': 9,
                'distance': 1199
            },
            {
                'id': 11,
                'distance': 152
            },
            {
                'id': 12,
                'distance': 780
            },
            {
                'id': 13,
                'distance': 856
            },
            {
                'id': 14,
                'distance': 725
            },
            {
                'id': 15,
                'distance': 70
            },
            {
                'id': 16,
                'distance': 1052
            },
            {
                'id': 17,
                'distance': 734
            },
            {
                'id': 18,
                'distance': 159
            },
            {
                'id': 19,
                'distance': 413
            },
            {
                'id': 20,
                'distance': 866
            },
            {
                'id': 21,
                'distance': 869
            },
            {
                'id': 22,
                'distance': 263
            },
            {
                'id': 23,
                'distance': 578
            },
            {
                'id': 24,
                'distance': 336
            },
            {
                'id': 25,
                'distance': 949
            },
        ]
    },
    {
        'id': 11,
        'connections': [
            {
                'id': 1,
                'distance': 360
            },
            {
                'id': 2,
                'distance': 975
            },
            {
                'id': 3,
                'distance': 1221
            },
            {
                'id': 4,
                'distance': 423
            },
            {
                'id': 5,
                'distance': 833
            },
            {
                'id': 6,
                'distance': 135
            },
            {
                'id': 7,
                'distance': 550
            },
            {
                'id': 8,
                'distance': 710
            },
            {
                'id': 9,
                'distance': 1379
            },
            {
                'id': 10,
                'distance': 152
            },
            {
                'id': 12,
                'distance': 850
            },
            {
                'id': 13,
                'distance': 970
            },
            {
                'id': 14,
                'distance': 891
            },
            {
                'id': 15,
                'distance': 232
            },
            {
                'id': 16,
                'distance': 1073
            },
            {
                'id': 17,
                'distance': 896
            },
            {
                'id': 18,
                'distance': 128
            },
            {
                'id': 19,
                'distance': 261
            },
            {
                'id': 20,
                'distance': 1028
            },
            {
                'id': 21,
                'distance': 1141
            },
            {
                'id': 22,
                'distance': 240
            },
            {
                'id': 23,
                'distance': 740
            },
            {
                'id': 24,
                'distance': 278
            },
            {
                'id': 25,
                'distance': 690
            },
        ]
    },
    {
        'id': 12,
        'connections': [
            {
                'id': 1,
                'distance': 471
            },
            {
                'id': 2,
                'distance': 343
            },
            {
                'id': 3,
                'distance': 611
            },
            {
                'id': 4,
                'distance': 677
            },
            {
                'id': 5,
                'distance': 377
            },
            {
                'id': 6,
                'distance': 747
            },
            {
                'id': 7,
                'distance': 490
            },
            {
                'id': 8,
                'distance': 174
            },
            {
                'id': 9,
                'distance': 857
            },
            {
                'id': 10,
                'distance': 780
            },
            {
                'id': 11,
                'distance': 850
            },
            {
                'id': 13,
                'distance': 120
            },
            {
                'id': 14,
                'distance': 420
            },
            {
                'id': 15,
                'distance': 864
            },
            {
                'id': 16,
                'distance': 282
            },
            {
                'id': 17,
                'distance': 681
            },
            {
                'id': 18,
                'distance': 754
            },
            {
                'id': 19,
                'distance': 999
            },
            {
                'id': 20,
                'distance': 556
            },
            {
                'id': 21,
                'distance': 51
            },
            {
                'id': 22,
                'distance': 590
            },
            {
                'id': 23,
                'distance': 300
            },
            {
                'id': 24,
                'distance': 642
            },
            {
                'id': 25,
                'distance': 640
            },
        ]
    },
    {
        'id': 13,
        'connections': [
            {
                'id': 1,
                'distance': 428
            },
            {
                'id': 2,
                'distance': 468
            },
            {
                'id': 3,
                'distance': 731
            },
            {
                'id': 4,
                'distance': 557
            },
            {
                'id': 5,
                'distance': 497
            },
            {
                'id': 6,
                'distance': 627
            },
            {
                'id': 7,
                'distance': 489
            },
            {
                'id': 8,
                'distance': 294
            },
            {
                'id': 9,
                'distance': 977
            },
            {
                'id': 10,
                'distance': 856
            },
            {
                'id': 11,
                'distance': 970
            },
            {
                'id': 12,
                'distance': 120
            },
            {
                'id': 14,
                'distance': 540
            },
            {
                'id': 15,
                'distance': 741
            },
            {
                'id': 16,
                'distance': 392
            },
            {
                'id': 17,
                'distance': 800
            },
            {
                'id': 18,
                'distance': 660
            },
            {
                'id': 19,
                'distance': 1009
            },
            {
                'id': 20,
                'distance': 831
            },
            {
                'id': 21,
                'distance': 171
            },
            {
                'id': 22,
                'distance': 548
            },
            {
                'id': 23,
                'distance': 420
            },
            {
                'id': 24,
                'distance': 515
            },
            {
                'id': 25,
                'distance': 529
            },
        ]
    },
    {
        'id': 14,
        'connections': [
            {
                'id': 1,
                'distance': 593
            },
            {
                'id': 2,
                'distance': 196
            },
            {
                'id': 3,
                'distance': 390
            },
            {
                'id': 4,
                'distance': 468
            },
            {
                'id': 5,
                'distance': 270
            },
            {
                'id': 6,
                'distance': 898
            },
            {
                'id': 7,
                'distance': 337
            },
            {
                'id': 8,
                'distance': 246
            },
            {
                'id': 9,
                'distance': 474
            },
            {
                'id': 10,
                'distance': 725
            },
            {
                'id': 11,
                'distance': 891
            },
            {
                'id': 12,
                'distance': 420
            },
            {
                'id': 13,
                'distance': 540
            },
            {
                'id': 15,
                'distance': 665
            },
            {
                'id': 16,
                'distance': 635
            },
            {
                'id': 17,
                'distance': 261
            },
            {
                'id': 18,
                'distance': 825
            },
            {
                'id': 19,
                'distance': 1149
            },
            {
                'id': 20,
                'distance': 141
            },
            {
                'id': 21,
                'distance': 471
            },
            {
                'id': 22,
                'distance': 653
            },
            {
                'id': 23,
                'distance': 279
            },
            {
                'id': 24,
                'distance': 892
            },
            {
                'id': 25,
                'distance': 477
            },
        ]
    },
    {
        'id': 15,
        'connections': [
            {
                'id': 1,
                'distance': 311
            },
            {
                'id': 2,
                'distance': 95  # dfdf
            },
            {
                'id': 3,
                'distance': 1045
            },
            {
                'id': 4,
                'distance': 187
            },
            {
                'id': 5,
                'distance': 925
            },
            {
                'id': 6,
                'distance': 296
            },
            {
                'id': 7,
                'distance': 318
            },
            {
                'id': 8,
                'distance': 627
            },
            {
                'id': 9,
                'distance': 1129
            },
            {
                'id': 10,
                'distance': 70
            },
            {
                'id': 11,
                'distance': 239
            },
            {
                'id': 12,
                'distance': 864
            },
            {
                'id': 13,
                'distance': 741
            },
            {
                'id': 14,
                'distance': 665
            },
            {
                'id': 16,
                'distance': 1157
            },
            {
                'id': 17,
                'distance': 664
            },
            {
                'id': 18,
                'distance': 162
            },
            {
                'id': 19,
                'distance': 484
            },
            {
                'id': 20,
                'distance': 805
            },
            {
                'id': 21,
                'distance': 834
            },
            {
                'id': 22,
                'distance': 193
            },
            {
                'id': 23,
                'distance': 508
            },
            {
                'id': 24,
                'distance': 331
            },
            {
                'id': 25,
                'distance': 458
            },
        ]
    },
    {
        'id': 16,
        'connections': [
            {
                'id': 1,
                'distance': 844
            },
            {
                'id': 2,
                'distance': 446
            },
            {
                'id': 3,
                'distance': 591
            },
            {
                'id': 4,
                'distance': 803
            },
            {
                'id': 5,
                'distance': 365
            },
            {
                'id': 6,
                'distance': 1070
            },
            {
                'id': 7,
                'distance': 972
            },
            {
                'id': 8,
                'distance': 570
            },
            {
                'id': 9,
                'distance': 739
            },
            {
                'id': 10,
                'distance': 1052
            },
            {
                'id': 11,
                'distance': 1173
            },
            {
                'id': 12,
                'distance': 282
            },
            {
                'id': 13,
                'distance': 392
            },
            {
                'id': 14,
                'distance': 635
            },
            {
                'id': 15,
                'distance': 1157
            },
            {
                'id': 17,
                'distance': 896
            },
            {
                'id': 18,
                'distance': 1097
            },
            {
                'id': 19,
                'distance': 1363
            },
            {
                'id': 20,
                'distance': 652
            },
            {
                'id': 21,
                'distance': 221
            },
            {
                'id': 22,
                'distance': 964
            },
            {
                'id': 23,
                'distance': 696
            },
            {
                'id': 24,
                'distance': 981
            },
            {
                'id': 25,
                'distance': 1112
            },
        ]
    },
    {
        'id': 17,
        'connections': [
            {
                'id': 1,
                'distance': 602
            },
            {
                'id': 2,
                'distance': 430
            },
            {
                'id': 3,
                'distance': 706
            },
            {
                'id': 4,
                'distance': 477
            },
            {
                'id': 5,
                'distance': 477
            },
            {
                'id': 6,
                'distance': 908
            },
            {
                'id': 7,
                'distance': 346
            },
            {
                'id': 8,
                'distance': 506
            },
            {
                'id': 9,
                'distance': 253
            },
            {
                'id': 10,
                'distance': 734
            },
            {
                'id': 11,
                'distance': 896
            },
            {
                'id': 12,
                'distance': 681
            },
            {
                'id': 13,
                'distance': 800
            },
            {
                'id': 14,
                'distance': 261
            },
            {
                'id': 15,
                'distance': 664
            },
            {
                'id': 16,
                'distance': 896
            },
            {
                'id': 18,
                'distance': 774
            },
            {
                'id': 19,
                'distance': 1138
            },
            {
                'id': 20,
                'distance': 190
            },
            {
                'id': 21,
                'distance': 732
            },
            {
                'id': 22,
                'distance': 662
            },
            {
                'id': 23,
                'distance': 540
            },
            {
                'id': 24,
                'distance': 883
            },
            {
                'id': 25,
                'distance': 350
            },
        ]
    },
    {
        'id': 18,
        'connections': [
            {
                'id': 1,
                'distance': 232
            },
            {
                'id': 2,
                'distance': 877
            },
            {
                'id': 3,
                'distance': 1100
            },
            {
                'id': 4,
                'distance': 298
            },
            {
                'id': 5,
                'distance': 977
            },
            {
                'id': 6,
                'distance': 134
            },
            {
                'id': 7,
                'distance': 427
            },
            {
                'id': 8,
                'distance': 547
            },
            {
                'id': 9,
                'distance': 1289
            },
            {
                'id': 10,
                'distance': 159
            },
            {
                'id': 11,
                'distance': 128
            },
            {
                'id': 12,
                'distance': 754
            },
            {
                'id': 13,
                'distance': 660
            },
            {
                'id': 14,
                'distance': 825
            },
            {
                'id': 15,
                'distance': 162
            },
            {
                'id': 16,
                'distance': 1097
            },
            {
                'id': 17,
                'distance': 774
            },
            {
                'id': 19,
                'distance': 338
            },
            {
                'id': 20,
                'distance': 987
            },
            {
                'id': 21,
                'distance': 831
            },
            {
                'id': 22,
                'distance': 112
            },
            {
                'id': 23,
                'distance': 575
            },
            {
                'id': 24,
                'distance': 176
            },
            {
                'id': 25,
                'distance': 568
            },
        ]
    },
    {
        'id': 19,
        'connections': [
            {
                'id': 1,
                'distance': 575
            },
            {
                'id': 2,
                'distance': 1130
            },
            {
                'id': 3,
                'distance': 1391
            },
            {
                'id': 4,
                'distance': 671
            },
            {
                'id': 5,
                'distance': 1488
            },
            {
                'id': 6,
                'distance': 280
            },
            {
                'id': 7,
                'distance': 706
            },
            {
                'id': 8,
                'distance': 883
            },
            {
                'id': 9,
                'distance': 1539
            },
            {
                'id': 10,
                'distance': 413
            },
            {
                'id': 11,
                'distance': 261
            },
            {
                'id': 12,
                'distance': 999
            },
            {
                'id': 13,
                'distance': 1009
            },
            {
                'id': 14,
                'distance': 1149
            },
            {
                'id': 15,
                'distance': 484
            },
            {
                'id': 16,
                'distance': 1363
            },
            {
                'id': 17,
                'distance': 1138
            },
            {
                'id': 18,
                'distance': 338
            },
            {
                'id': 20,
                'distance': 1292
            },
            {
                'id': 21,
                'distance': 165
            },
            {
                'id': 22,
                'distance': 465
            },
            {
                'id': 23,
                'distance': 984
            },
            {
                'id': 24,
                'distance': 444
            },
            {
                'id': 25,
                'distance': 951
            },
        ]
    },
    {
        'id': 20,
        'connections': [
            {
                'id': 1,
                'distance': 734
            },
            {
                'id': 2,
                'distance': 213
            },
            {
                'id': 3,
                'distance': 335
            },
            {
                'id': 4,
                'distance': 690
            },
            {
                'id': 5,
                'distance': 287
            },
            {
                'id': 6,
                'distance': 1040
            },
            {
                'id': 7,
                'distance': 472
            },
            {
                'id': 8,
                'distance': 387
            },
            {
                'id': 9,
                'distance': 333
            },
            {
                'id': 10,
                'distance': 866
            },
            {
                'id': 11,
                'distance': 128
            },
            {
                'id': 12,
                'distance': 556
            },
            {
                'id': 13,
                'distance': 831
            },
            {
                'id': 14,
                'distance': 141
            },
            {
                'id': 15,
                'distance': 805
            },
            {
                'id': 16,
                'distance': 652
            },
            {
                'id': 17,
                'distance': 190
            },
            {
                'id': 18,
                'distance': 987
            },
            {
                'id': 19,
                'distance': 1299
            },
            {
                'id': 21,
                'distance': 576
            },
            {
                'id': 22,
                'distance': 854
            },
            {
                'id': 23,
                'distance': 420
            },
            {
                'id': 24,
                'distance': 136
            },
            {
                'id': 25,
                'distance': 608
            },
        ]
    },
    {
        'id': 21,
        'connections': [
            {
                'id': 1,
                'distance': 521
            },
            {
                'id': 2,
                'distance': 376
            },
            {
                'id': 3,
                'distance': 560
            },
            {
                'id': 4,
                'distance': 624
            },
            {
                'id': 5,
                'distance': 297
            },
            {
                'id': 6,
                'distance': 798
            },
            {
                'id': 7,
                'distance': 551
            },
            {
                'id': 8,
                'distance': 225
            },
            {
                'id': 9,
                'distance': 806
            },
            {
                'id': 10,
                'distance': 869
            },
            {
                'id': 11,
                'distance': 141
            },
            {
                'id': 12,
                'distance': 51
            },
            {
                'id': 13,
                'distance': 171
            },
            {
                'id': 14,
                'distance': 471
            },
            {
                'id': 15,
                'distance': 834
            },
            {
                'id': 16,
                'distance': 221
            },
            {
                'id': 17,
                'distance': 732
            },
            {
                'id': 18,
                'distance': 831
            },
            {
                'id': 19,
                'distance': 165
            },
            {
                'id': 20,
                'distance': 576
            },
            {
                'id': 22,
                'distance': 641
            },
            {
                'id': 23,
                'distance': 351
            },
            {
                'id': 24,
                'distance': 713
            },
            {
                'id': 25,
                'distance': 691
            },
        ]
    },
    {
        'id': 22,
        'connections': [
            {
                'id': 1,
                'distance': 120
            },
            {
                'id': 2,
                'distance': 765
            },
            {
                'id': 3,
                'distance': 988
            },
            {
                'id': 4,
                'distance': 185
            },
            {
                'id': 5,
                'distance': 875
            },
            {
                'id': 6,
                'distance': 246
            },
            {
                'id': 7,
                'distance': 315
            },
            {
                'id': 8,
                'distance': 435
            },
            {
                'id': 9,
                'distance': 1171
            },
            {
                'id': 10,
                'distance': 263
            },
            {
                'id': 11,
                'distance': 240
            },
            {
                'id': 12,
                'distance': 590
            },
            {
                'id': 13,
                'distance': 548
            },
            {
                'id': 14,
                'distance': 653
            },
            {
                'id': 15,
                'distance': 193
            },
            {
                'id': 16,
                'distance': 964
            },
            {
                'id': 17,
                'distance': 662
            },
            {
                'id': 18,
                'distance': 112
            },
            {
                'id': 19,
                'distance': 455
            },
            {
                'id': 20,
                'distance': 854
            },
            {
                'id': 21,
                'distance': 641
            },
            {
                'id': 23,
                'distance': 463
            },
            {
                'id': 24,
                'distance': 190
            },
            {
                'id': 25,
                'distance': 455
            },
        ]
    },
    {
        'id': 23,
        'connections': [
            {
                'id': 1,
                'distance': 343
            },
            {
                'id': 2,
                'distance': 324
            },
            {
                'id': 3,
                'distance': 547
            },
            {
                'id': 4,
                'distance': 321
            },
            {
                'id': 5,
                'distance': 405
            },
            {
                'id': 6,
                'distance': 709
            },
            {
                'id': 7,
                'distance': 190
            },
            {
                'id': 8,
                'distance': 126
            },
            {
                'id': 9,
                'distance': 706
            },
            {
                'id': 10,
                'distance': 578
            },
            {
                'id': 11,
                'distance': 740
            },
            {
                'id': 12,
                'distance': 300
            },
            {
                'id': 13,
                'distance': 420
            },
            {
                'id': 14,
                'distance': 279
            },
            {
                'id': 15,
                'distance': 508
            },
            {
                'id': 16,
                'distance': 696
            },
            {
                'id': 17,
                'distance': 540
            },
            {
                'id': 18,
                'distance': 575
            },
            {
                'id': 19,
                'distance': 984
            },
            {
                'id': 20,
                'distance': 420
            },
            {
                'id': 21,
                'distance': 351
            },
            {
                'id': 22,
                'distance': 463
            },
            {
                'id': 24,
                'distance': 660
            },
            {
                'id': 25,
                'distance': 330
            },
        ]
    },
    {
        'id': 24,
        'connections': [
            {
                'id': 1,
                'distance': 312
            },
            {
                'id': 2,
                'distance': 891
            },
            {
                'id': 3,
                'distance': 1141
            },
            {
                'id': 4,
                'distance': 389
            },
            {
                'id': 5,
                'distance': 957
            },
            {
                'id': 6,
                'distance': 143
            },
            {
                'id': 7,
                'distance': 538
            },
            {
                'id': 8,
                'distance': 637
            },
            {
                'id': 9,
                'distance': 1292
            },
            {
                'id': 10,
                'distance': 336
            },
            {
                'id': 11,
                'distance': 278
            },
            {
                'id': 12,
                'distance': 642
            },
            {
                'id': 13,
                'distance': 515
            },
            {
                'id': 14,
                'distance': 892
            },
            {
                'id': 15,
                'distance': 331
            },
            {
                'id': 16,
                'distance': 981
            },
            {
                'id': 17,
                'distance': 883
            },
            {
                'id': 18,
                'distance': 176
            },
            {
                'id': 19,
                'distance': 444
            },
            {
                'id': 20,
                'distance': 1036
            },
            {
                'id': 21,
                'distance': 713
            },
            {
                'id': 22,
                'distance': 190
            },
            {
                'id': 23,
                'distance': 660
            },
            {
                'id': 25,
                'distance': 695
            },
        ]
    },
    {
        'id': 25,
        'connections': [
            {
                'id': 1,
                'distance': 396
            },
            {
                'id': 2,
                'distance': 672
            },
            {
                'id': 3,
                'distance': 867
            },
            {
                'id': 4,
                'distance': 271
            },
            {
                'id': 5,
                'distance': 747
            },
            {
                'id': 6,
                'distance': 701
            },
            {
                'id': 7,
                'distance': 149
            },
            {
                'id': 8,
                'distance': 363
            },
            {
                'id': 9,
                'distance': 951
            },
            {
                'id': 10,
                'distance': 949
            },
            {
                'id': 11,
                'distance': 690
            },
            {
                'id': 12,
                'distance': 640
            },
            {
                'id': 13,
                'distance': 529
            },
            {
                'id': 14,
                'distance': 477
            },
            {
                'id': 15,
                'distance': 458
            },
            {
                'id': 16,
                'distance': 1112
            },
            {
                'id': 17,
                'distance': 350
            },
            {
                'id': 18,
                'distance': 568
            },
            {
                'id': 19,
                'distance': 951
            },
            {
                'id': 20,
                'distance': 608
            },
            {
                'id': 21,
                'distance': 691
            },
            {
                'id': 22,
                'distance': 455
            },
            {
                'id': 23,
                'distance': 330
            },
            {
                'id': 24,
                'distance': 695
            },
        ]
    },
]

ant = Ant(combinations3, items3)
ant.run()

write_stats_to_file('lab10/all.txt', ant.statistics, 'all')
write_stats_to_file('lab10/first_10_perc.txt', ant.statistics, 'first_10')
write_stats_to_file('lab10/first_50_perc.txt', ant.statistics, 'first_50')
write_stats_to_file('lab10/last_50_perc.txt', ant.statistics, 'last_50')
write_stats_to_file('lab10/last_10_perc.txt', ant.statistics, 'last_10')
