class Tester:

    def __init__(salf, name): #Не было salf во всей функции
        salf.name = name

    def work_hard(self, deadline): #Исправил переменную deadline
        if deadline: #Лишний self
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!'