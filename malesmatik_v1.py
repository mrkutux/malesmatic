def persegi(a):
	return a**2

def kelpersegi(a):
	return 4*a

def segitiga(a,t):
	return 1/2*a*t

def jargen(a,t):
	return a*t

def lingkaran(a):
	return 22/7*a*a

def trapesium(a,t,z):
	return (a+t)*z/2

def persegipanjang(a,t):
	return a*t

def belahketupat(a,t):
	return 1/2*a*t

#Menu
print("|========================================|")
print("|=Luas & Keliling Bangunan By Helmy Agta=|")
print("|========================================|")
print("|============Pilih Menu==================|")
print("|===< 1. Luas Persegi              >=====|")
print("|===< 2. Keliling Persegi          >=====|")
print("|===< 3. Luas Segitiga             >=====|")
print("|===< 4. Luas Jajargenjang         >=====|")
print("|===< 5. Luas Lingkaran            >=====|")
print("|===< 6. Luas Trapesium            >=====|")
print("|===< 7. Luas Persegi Panjang      >=====|")
print("|===< 8. Luas Belah Ketupat        >=====|")
print("|========================================|")

#inputmenu
choice = input("pilih mana (1/2/3/4/5/6/7) : ")

if choice == '1':
	satu = int(input("Masukan Sisi : "))
elif choice == '2':
	satu = int(input("Masukan Sisi : "))
elif choice == '3':
	satu = int(input("Masukan Alas : "))
	dua = int(input("Masukan Tinggi : "))
elif choice == '4':
	satu = int(input("Masukan Alas : "))
	dua = int(input("Masukan Tinggi : "))
elif choice == '5':
	satu = int(input("Masukan Jari-Jari :"))
elif choice == '6':
	satu = int(input("Masukan Sisi Atas : "))
	dua = int(input("Masukan Sisi Bawah : "))
	tiga = int(input("Masukan Tinggi : "))
elif choice == '7':
	satu = int(input("Masukan Panjang : "))
	dua = int(input("Masukan Lebar : ")) 
elif choice == '8':
	satu = int(input("Masukan Diagonal 1 : "))
	dua = int(input("Masukan Diagonal 2 : "))


#Eksekusimen
if choice == '1':
	print(satu,"x",satu,"=",persegi(satu))
elif choice == '2':
	print("4","x",satu,"=",kelpersegi(satu))
elif choice == '3':
	print("1/2","x",satu,"x",dua,"=",segitiga(satu,dua))
elif choice == '4':
	print (satu,"x",dua,"=",jargen(satu,dua))
elif choice == '5':
	print ("22/7","x",satu,"x",satu,"=",lingkaran(satu))
elif choice == '6':
	print ("(",satu,"+",dua,")",tiga,"=",trapesium(satu,dua,tiga))
elif choice == '7':
	print (satu,"x",dua,"=",persegipanjang(satu,dua))
elif choice == '8':
	print ("1/2","x",satu,"x",dua,"=",belahketupat(satu,dua))