"""
変数:seat_number, member_name
できること:member_name をランダムに並べ替える。

"""

import random

seat_number = range(1, 15)
join_members = ['吉田力',
                '田中潤',
                '舞鶴翔',
                '兼松智恵子',
                '速水駿',
                '徳田貴一',
                '中野英磨',
                '熊谷航',
                '下川孝宣',
                '柴田雅幸',
                '山田いつき',
                '塚田崇博',
                '高橋通',
                '望月ちかこ']


def changing_seat(join_member):
    random.shuffle(join_member)
    # random.shuffle関数でjoin_member自体がシャッフルされ変更されている

    print('左テーブル')

    for i in range(1, 4):
        print(f' {i}{join_member[i]}')


# changing_seat(seat_number, join_menber)
# 最終的にchanging_seat にjoin_memberを入れたら
# 席番号.名前 の順で並んだリストを返してくれる


changing_seat(join_members)
