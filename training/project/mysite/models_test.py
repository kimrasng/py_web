# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

# from Board.models import Board
# from django.contrib.auth.models import User

# for i in range(1,101):
#     p = Board(title='Test_Board_{}'.format(i), content='Board Test Content', author=User.objects.get(id=1))
#     p.save()

# from MTV.models import Board

# def data_selete():
    # print(Board.objects.all())
    # print("Object Count: {}".format(Board.objects.count()))

    # print(Board.objects.filter(id=1))
    # print(Board.objects.filter(id=2))
    # print(Board.objects.get(id=1))
    # print(Board.objects.get(id=2))

    # print(Board.objects.filter(title__contains='Board'))
    # print(Board.objects.filter(title__contains='Django'))

    

# data_selete()


# def data_create():
#     Board_data = Board(title='Django Project', content='Django Project Model Data Create TEST')
#     Board_data.save()
#     print(Board.objects.all())

# data_create()


# def data_delete():
#     Board_data = Board.objects.get(title='Django Project')
#     Board_data.delete()
#     print(Board.objects.all())

# data_delete()


# def data_modify():
#     Board_data = Board.objects.get(title='Django Project')
#     Board_data.title = 'Django Model TEST'
#     Board_data.save()
#     print(Board.objects.all())

# data_modify()


# def data_objects():
#     Board_object = Board.objects.get(title='Board Title')
#     print("ID(PK): {}".format(Board_object.id))
#     print("Title: {}".format(Board_object.title))
#     print("Content: {}".format(Board_object.content))
#     print("Create_Date: {}".format(Board_object.create_date))
#     print("Modify_Date: {}".format(Board_object.modify_date))

# data_objects()


from MTV.models import Question, Answer

# def R_selete():
#     Q = Question.objects.get(id=1)
#     print(Q.id)
#     print(Q.title)
#     print(Q.content)

#     print(Q.answer_set.count())
#     print(Q.answer_set.all())
#     print(Q.answer_set.get(content__contains='Professor'))
#     print(Q.answer_set.filter(content__contains='Soccer'))

# R_selete()


# def R_create():
#     Q = Question.objects.get(id=1)
#     Q.answer_set.create(content='Office Worker')
#     print("Answer List: {}".format(Q.answer_set.all()))

# def R_delete():
#     Q = Question.objects.get(id=1)
#     A = Answer.objects.get(content__contains='Office Worker')
#     A.delete()
#     print("Answer List: {}".format(Q.answer_set.all()))

# R_create()
# R_delete()