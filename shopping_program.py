# 文字列のキーと数値の値を持つ辞書を作って、変数itemsに代入してください
items={'apple':100, 'banana':200, 'orange':400}

# for文を用いて、辞書itemsのキーを1つずつ取り出していく繰り返し処理を作成してください
for item_name in items:
    # 「---------------------------------------------」を出力してください
    print('---------------------------------------------')
    # 「◯◯は1個△△円です」となるように出力してください
    print(item_name+'は1個'+str(items[item_name])+'円です')