monsters = ["화끈몬", "찌릿몬", "축축몬", "수풀몬", "가스몬", "바람몬"]
print(monsters)
monsters.remove("가스몬")  # remove 메소드로 삭제를 하였다.
print(monsters)
# monsters.pop("수풀몬") error
monsters.pop(3)
print(monsters)
monsters.pop()
print(monsters)
del monsters[0]
print(monsters)
# del monsters
monsters.clear()
print(monsters)
