monsters = []  # 빈 list
print(monsters)
monsters.append("화끈몬")  # 메서드로 추가
print(monsters)
monsters = monsters + ["축축몬", "수풀몬"]  # 추가
print(monsters)
monsters.insert(1, "찌릿몬")
print(monsters)
new_monsters = ["가스몬", "바람몬"]
monsters.extend(new_monsters)  # extend는 변수를 추가할때 많이 사용한다.
print(monsters)
