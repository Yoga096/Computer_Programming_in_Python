itemsA = {"蘋果", "香蕉", "鳳梨", "芭樂"}
itemsB = {"鳳梨", "蘋果", "水梨", "蓮霧"}

itemsA.add(str(input()))
itemsA.add(str(input()))
itemsA.remove("蘋果")

itemsB.add(str(input()))
itemsB.add(str(input()))
itemsB.remove("蓮霧")

print("iA:", sorted(list(itemsA)))
print("iB:", sorted(list(itemsB)))
print("union:", sorted(list(itemsA | itemsB)))
print("intersection:", sorted(list(itemsA & itemsB)))
print("A diff B:", sorted(list(itemsA - itemsB)))
print("B diff A:", sorted(list(itemsB - itemsA)))
print("A xor B:", sorted(list(itemsA ^ itemsB)))