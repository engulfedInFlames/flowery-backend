# 과제 안내
# 1. 예제 코드를 직접 작성하여 깃허브에 푸쉬
# 2. 변수 이름은 자신의 영문 이름으로 할 것

# 1. 문자열 메소드 ✅
# count

# gyeongsu = "Hello, World!"
# count = gyeongsu.count("l")
# print(count)

# # find
# # 특정 문자열의 첫 위치 반환, ⭐ 없으면 -1 반환 ⭐
# position = gyeongsu.find("World")
# print(position)

# # index
# # 없으면 ValueError
# # try - except는 Error가 나더라도 로직을 진행시키기 위한 처리이다.
# try:
#     position = gyeongsu.index("World")
#     print(position)
# except ValueError:
#     print("찾는 문자열이 없습니다.")

# # join
# fruits = ["apple", "banana", "cherry"]
# joined_fruits = ", ".join(fruits)
# print(joined_fruits)

# # split
# new_fruits = joined_fruits.split(",")
# print(new_fruits)

# # upper, lower
# uppered = gyeongsu.upper()
# print(uppered)

# lowered = gyeongsu.lower()
# print(lowered)

# # replace
# replaced = gyeongsu.replace("World", "Python")
# print(replaced)

################################################################
################################################################
################################################################

# # 2. 리스트 메소드 ✅
# # len
# gyeongsu = [1, 2, 3, 4, 5]
# print(len(gyeongsu))

# # ⭐ del ⭐
# new_gyeongsu = gyeongsu.copy()
# del new_gyeongsu[2]
# print(new_gyeongsu)

# # append
# new_gyeongsu = gyeongsu.copy()
# new_gyeongsu.append(6)
# print(new_gyeongsu)

# # sort
# new_gyeongsu = gyeongsu.copy()
# new_gyeongsu.sort(reverse=True)  # default는 오름차순
# print(new_gyeongsu)

# # reverse
# new_gyeongsu = gyeongsu.copy()
# new_gyeongsu.reverse()
# print(new_gyeongsu)

# # index
# new_gyeongsu = gyeongsu.copy()
# position = new_gyeongsu.index(3)
# print(position)

# # insert & remove
# new_gyeongsu = gyeongsu.copy()
# new_gyeongsu.insert(2, 999)
# print(new_gyeongsu)

# new_gyeongsu.remove(999)
# print(new_gyeongsu)

# # pop
# new_gyeongsu = gyeongsu.copy()
# popped = new_gyeongsu.pop(2)
# print(popped)

# # count
# new_gyeongsu = gyeongsu.copy()
# new_gyeongsu.append(3)
# count_three = new_gyeongsu.count(3)
# print(count_three)

# # extend, +=
# new_gyeongsu = gyeongsu.copy()
# new_gyeongsu.extend([6, 7, 8, 9])
# print(new_gyeongsu)

# new_gyeongsu += [10, 11, 12, 13]
# print(new_gyeongsu)

################################################################
################################################################
################################################################

# 3. 딕셔너리 메소드 ✅
# 메모리가 충분할 때, 빠른 키-값 쌍 찾기에 사용된다. e.g. 해쉬

# 키-값 추가 삭제
# gyeongsu = {}
# gyeongsu["1"] = 1
# gyeongsu["2"] = 2
# print(gyeongsu)
# del gyeongsu["2"]
# print(gyeongsu)

# # items: 키-값 쌍을 튜플 리스트로 반환
# print(gyeongsu.items())

# # get
# print(gyeongsu.get("1"))  # ⭐ Error가 아닌 None 반환 ⭐

# # in: 키 존재 여부
# print("1" in gyeongsu)

################################################################
################################################################
################################################################

# 4. 프로세스 ✅

# 프로세스: 실행 중인 프로그램. 프로그램이 실행되면 프로세스가 되고, 메모리에 적재된다. 윈도우 작업 관리자로 프로세스를 직접 확인할 수 있다. 리눅스나 맥OS에서 ps 명령어로 프로세스를 확인할 수 있다.

# ps: 현재 실행 중의 프로세스 목록과 상태를 출력
# ps -ef: 현재 실행 중의 모든 프로세스를 자세히 출력

# 포그라운드(Foreground) 프로세스: 사용자가 볼 수 있는 공간에서 실행되는 프로세스; 사용자가 끄거나 켜면서 상호작용할 수 있는 프로세스

# 백그라운드 프로세스: 사용자가 볼 수 없는 ~; 사용자와 상호작용하지 않고 정해진 일만 수행; 데몬, 서비스라고도 불린다.


# 프로세스 제어 블록(PCB): 메모리 리소스를 관리하여 프로세스에 할당
# PCB에 담기는 대표 정보: PID(프로세스를 구분하기 위한 ID); 프로세스 상태; 사용한 파일과 입출력 장치 정보(VSCode 혹은 Pycharm 등)

# 프로세스의 4가지 구성 요소: 코드 영역, 데이터 영역, 스택 영역, 힙 영역

# 5. 스레드 ✅
# 스레드 : 한 프로세스의 구성 요소; 실행 흐름

# 6. 멀티 프로세스와 멀티 스레드 ✅
# 멀티 프로세스는 여러 개의 프로그램이 실행되는 것이며; 프로그램 간에는 대체로 독립적, 자원 공유 X
# 멀티 스레드는 한 프로세스 내에서 여러 스레드가 있는 것; 스레드 간에는 대체로 의존적, 자원 공유 O
