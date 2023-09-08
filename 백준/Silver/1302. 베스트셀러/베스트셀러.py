n = int(input()) # 오늘 하루 동안 팔린 책의 개수
book_dict = {}
for _ in range(n) :
    bookname = input()
    book_dict[bookname] = book_dict.get(bookname ,0) + 1
    
bestseller = [k for k, v in book_dict.items() if v == max(book_dict.values())]
bestseller.sort()
print(bestseller[0])