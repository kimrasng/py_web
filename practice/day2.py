# # 객체 지향 프로그래밍

# # 롤 캐릭터 생성

# # 티모
# # - 행동(속도)
# def timo_run():
#     speed = 1

# # - 대사
# def timo_say():
#     print("티모대위, 명을 받겠습니다.");

# # 스킬
# timo_skill = {'q':'실명다트', 'w':'신속한 이동', 'e':'맹독다트', 'r':'독버섯'}

# # 룰루
# # - 행동(속도)
# def lulu_run():
#     speed = 10

# # - 대사
# def lulu_say():
#     print("만나서 반갑습니다.")

# # - 스킬
# lulu_skill = {'q':'글리터랜스', 'w':'변덕', 'e':'도와줘, 픽스!', 'r':'급속한 성장'}

# # 트리스타나
# # - 행동(속도)

# def tristan_run():
#     speed = 10

# # - 대사

# def tristana_say():
#     print("일단 한 번 쏘고 나면 또 쏘고 싶을 거예요!")

# # - 스킬

# tristan_skill = {'q':'신속한 화재', 'w':'로켓 점프', 'e':'폭발물', 'r':'버스터 샷'}









# # classs 1

# # step1. 클래스 만들기

# class Character:
#     def run(self):
#         self.speed = 10

#     def say(self):
#         print("티모 대위, 명을 받들겠습니다.")

# # step2. 객체 생성

# timo = Character()


# # step3. 속성(스킬) 추가

# timo.q = "실명다트"
# timo.w = "신속한 이동"
# timo.e = "맹독 다트"
# timo.r = "독버섯"

# # step4. 객체의 속성과 메소드 사용

# print(timo.q, timo.w, timo.e, timo.r)


# timo.run()
# print(timo.speed)

# timo.say()




# # class 2

# # step1. class 만들기

# class Character:
#     def run(self):
#         self.speed = 10
    
#     def say(self):
#         print("티모 대위, 명을 받들곘습니다.")

#     q = "실명다트"
#     w = "신속한 이동" 
#     e = "맹독 다트"
#     r = "독버섯"


# # step2. 객체 생성
# timo = Character()



# # step3. 속성 출력
# print(timo.q)
# print(timo.w)
# print(timo.e)
# print(timo.r)


# # step4. 메소드 호출
# # print(timo.speed)   # attribute ERROR : 속성 ERROR
# # AttributeError: 'Character' object has no attribute 'speed' : speed 라는 속성이 없다.
# timo.run()
# print(timo.speed)


# # step5. lulu, tristana객체 생성

# class Character:
#     def run(self):
#         self.speed = 10
    
#     def say(self):
#         print("만나서 반갑습니다.")

#     q = "글리터랜스"
#     w = "변덕" 
#     e = "도와줘, 픽스!"
#     r = "급속한 성장"


# lulu = Character()


# lulu.run()
# print(lulu.speed)

# print(lulu.q)
# print(lulu.w)
# print(lulu.e)
# print(lulu.r)




# class Character:
#     def run(self):
#         self.speed = 10
    
#     def say(self):
#         print("일단 한 번 쏘고 나면 또 쏘고 싶을 거예요!")

#     q = "신속한 화재"
#     w = "로켓 점프" 
#     e = "폭발물"
#     r = "버스트 샷"


# tristana = Character()


# tristana.run()
# print(tristana.speed)

# print(tristana.q)
# print(tristana.w)
# print(tristana.e)
# print(tristana.r)



# # class3

# # step1. class 생성

# class Character:
    
#     def __init__(self, speed, q, w, e, r):
#         self.speed = speed
#         self.q = q
#         self.w = w
#         self.e = e
#         self.r = r

#     def run(self):
#         self.speed = 10


# # step2. 객체 생성
# timo = Character(0, "실명다트", "신속한 이동", "맹독다트", "독버섯")

# # step3. 속성 출력

# print(timo.q)
# print(timo.w)
# print(timo.e)
# print(timo.r)


# # step4. 메소드 호출
# print(timo.speed)

# timo.run()
# print(timo.speed)



# class4

# lulu

# class Character:
    
#     def __init__(self, speed, q, w, e, r):
#         self.speed = speed
#         self.q = q
#         self.w = w
#         self.e = e
#         self.r = r

#     def run(self):
#         self.speed = 10


# # step2. 객체 생성
# lulu = Character(0, "그릴터랜스", "변덕", "도와줘, 픽스!", "급속한 성장")


# tristan = Character(0, "신속한 화재", "로켓 점프", "폭발물", "버스터 샷")
# # step3. 속성 출력

# print(lulu.q)
# print(lulu.w)
# print(lulu.e)
# print(lulu.r)

# print(tristan.q)
# print(tristan.w)
# print(tristan.e)
# print(tristan.r)


# #class 5

# class Character:
    
#     def __init__(self, speed, q, w, e, r):
#         self.speed = speed
#         self.q = q
#         self.w = w
#         self.e = e
#         self.r = r

#     def run(self):
#         self.speed = 10

#         def __str__(self):
#         info = "속도: {} / q스킬: {} / w스킬: {} / e스킬: {} / r스킬: {}".format(self.speed, self.q, self.w, self.e, self.r)
#         return info


# timo = Character(0, "실명다트", "신속한 이동", "맹독다트", "독버섯")

# # str 사용전
# print(timo)

# # __srt__ 사용후
# print(timo)


# # class6

# class Character:
    
#     def __init__(self, speed, q, w, e, r):
#         self.speed = speed
#         self.q = q
#         self.w = w
#         self.e = e
#         self.r = r

#     def run(self):
#         self.speed = 10



# timo = Character(0, "실명다트", "신속한 이동", "맹독다트", "독버섯")

# lulu = Character(0, "그릴터랜스", "변덕", "도와줘, 픽스!", "급속한 성장")


# # 메소드 호출

# timo.run()
# lulu.run()

# print(timo.speed)
# print(lulu.speed)


# class 7


# class A:
#     def momcar(self):
#         print("엄마차는 벤츠")

# class B(A):
#     def mycar(self):
#         print("내차는 테슬라")

# b = B()

# b.momcar()
# b.mycar()


# # class8


# class A:
#     def momcar(self):
#         print("엄마차는 벤츠")

# class B(A):
#     def mycar(self):
#         print("내차는 테슬라")

#     def momcar(self):
#         print("엄마차는 BMW")

# b = B()

# b.momcar()
# b.mycar()


# class9


class A:
    def momcar(self):
        print("엄마차는 벤츠")

class B(A):
    def mycar(self):
        print("내차는 테슬라")

    def momcar(self):
        super().momcar()
        print("엄마차는 BMW")

b = B()

b.momcar()
b.mycar()