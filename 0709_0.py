import csv
def signup():
    with open('data.csv', 'w', newline='') as f:
        cvswriter = csv.writer(f)
        cvswriter.writerow(["a", "b"])

signup()


with open("")

#파이썬 open w vs a 추가



 with open('a.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([id, pw])
        print("%s님 회원가입 되었습니다!" % id)


        with open('a.csv', 'a', newline='') as csvfile:
csvwriter = csv.writer(csvfile)
csvwriter.writerow([id, pw])
print("%s님 회원가입 되었습니다!" % id)
 
 
 
def userlist():
print("현재 존재하는 유저는?")
# csvfile 에서 현재 가입되어 있는 유저 전부 출력하기
with open('a.csv', 'r') as csvfile:
csvreader = csv.reader(csvfile)
 
for i in csvreader:
print("id: %s, pw: %s" % (i[0], i[1]))

numbers = [1,2]
def wrong():
    numbers.append('4')

def correct(array):
    array.append('4')
    return array

new numbers = correct(numbers)

print(new numbers)