apple_price=200
input_count=input('りんごの個数を入力してください:')

count = int(input_count)
print('購入するりんごの個数は'+str(count)+'個です')

total_price=apple_price*count

print('支払い金額は'+str(total_price)+'円です')