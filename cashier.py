import math

print("Total belanja seorang customer :")
total_customer = input()

print("Pembeli membayar :")
total_pay = input()

# set array & set config
array_fractions = [100000, 75000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5]
last_total = 0

def check_cashback():

    # step perhitungan jika cashback harus di pecah lebih dari 1x
    step = 1

    # menentukan berapa total cashback dari yang dibayar
    cashback = int(total_pay) - int(total_customer)

    # membulatkan total cashback
    total_cashback = round(cashback, -2)

    # validasi total yang dibayar harus lebih besar dari total belanja
    if int(total_pay) > int(total_customer):
        print('Kembalian yang harus diberikan kasir : ' + str(cashback))
        print('Dibulatkan menjadi : ' + str(total_cashback))

        print('Pecahan uang :')

        # mencari total cashback yang sesuai dengan satuan nominal yang telah ditentukan
        for x in array_fractions:

            # step pertama (pemecahan nominal cashback pertama)
            if step == 1:

                if int(total_cashback) >= x:

                    # penentuan berapa jumlah lembaran atau koin yang akan dibayar
                    mod = int(total_cashback) / int(x)
                    mod = math.floor(mod)

                    # menentukan jumlah akhir berapa sisa cashback
                    calculate = int(total_cashback) - (int(x) * mod)
                    last_total = calculate

                    # menentukan lembaran atau koin yang akan di jadikan cashback
                    if x >= 1000:
                        print(str(mod) + ' lembar ' + str(x))
                    else:
                        print(str(mod) + ' koin ' + str(x))

                    # merubah ke step 2, agar jika cashback harus lebih dari 1x pecahan. dapat dilanjutkan ke condition else
                    step = 2

            # step kedua (jika cashback harus dipecah lebih dari 1x)
            else:
                if int(last_total) > x:

                    # penentuan berapa jumlah lembaran atau koin yang akan dibayar
                    mod = int(last_total) / int(x)
                    mod = math.floor(mod)

                    # menentukan jumlah akhir berapa sisa cashback
                    calculate = int(last_total) - (int(x) * mod)
                    last_total = calculate

                    # menentukan lembaran atau koin yang akan di jadikan cashback
                    if x >= 1000:
                        print(str(mod) + ' lembar ' + str(x))
                    else:
                        print(str(mod) + ' koin ' + str(x))

    # validasi jika total yang dibayar sama dengan total belanja
    elif int(total_pay) == int(total_customer):
        print('Pembayaran dengan uang pas, maka tidak ada kembalian')

    # validasi jika total yang dibayar kurang dari total belanja
    else:
        print('Pembayaran, kurang bayar')

check_cashback()

