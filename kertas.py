import random
print("daftar pilihan")
print()
print("1.batu")
print("2.gunting")
print("3.kertas")
print()

def game_sederhana():
	kom=random.choice(["batu","gunting","kertas"])
	pil=int(input("masukan pilihan: "))
	if pil==1:
		print("anda        :batu")
		print("komputer    :",kom)
		if kom=="batu":
			print("\tdraw")
		if kom=="kertas":
			print("\tkamu kalah")
		if kom=="gunting":
			print("\tkamu menang")
	f pil==2:
		print("anda			:gunting")
		print(""komputer	:",kom)
		if kom=="batu":
			print("\tkamu kalah")
		if kom=="kertas":
			print("\tkamu menang")
		if kom=="gunting":
			print("\tdraw")
