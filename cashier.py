import math

print("Total belanja seorang customer :")
total_customer = input()

print("Pembeli membayar :")
total_pay = input()

# set array & set config
array_fractions = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5]
last_total = 0

def check_cashback():
    step = 1
    cashback = int(total_pay) - int(total_customer)
    total_cashback = round(cashback, -2)

    if int(total_pay) > int(total_customer):
        print('Kembalian yang harus diberikan kasir : ' + str(cashback))
        print('Dibulatkan menjadi : ' + str(total_cashback))

        print('Pecahan uang :')
        for x in array_fractions:

            if step == 1:
                if int(total_cashback) >= x:
                    mod = int(total_cashback) / int(x)
                    mod = math.floor(mod)

                    calculate = int(total_cashback) - int(x)
                    last_total = calculate

                    if x >= 1000:
                        print(str(mod) + ' lembar ' + str(x))
                    else:
                        print(str(mod) + ' koin ' + str(x))

                    step = 2
            else:
                if int(last_total) > x:

                    mod = int(last_total) / int(x)
                    mod = math.floor(mod)

                    calculate = int(last_total) - (int(x) * mod)
                    last_total = calculate

                    if x >= 1000:
                        print(str(mod) + ' lembar ' + str(x))
                    else:
                        print(str(mod) + ' koin ' + str(x))

    elif int(total_pay) == int(total_customer):
        print('Pembayaran dengan uang pas, maka tidak ada kembalian')

    else:
        print('Pembayaran, kurang bayar')

check_cashback()

