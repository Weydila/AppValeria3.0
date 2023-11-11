class TaskManager():
    def __init__(self) -> None:
        self.tasks = []

    ''' Adiciona uma nova tarefa. '''

    def add_task(self, prio, tarefa, data, status):
        print("Adicionando novo registro")

        self.obj = {
            "prioridade": "",
            "tarefa": "",
            "data": "",
            "status": ""
        }

        self.obj["prioridade"] = prio
        self.obj["tarefa"] = tarefa
        self.obj["data"] = data
        self.obj["status"] = status

        print(f"Tarefa adicionada com sucesso: {self.obj}")
        self.tasks.append(self.obj)

    ''' Remove uma tarefa. '''

    # {'prioridade': 'ALTA', 'tarefa': 'IR AO BANCO', 'data': '09/11/2023', 'status': 'FINALIZADA'}
    def remove_task(self, tarefa):
        print(f"Removendo tarefa: {tarefa}")

        def rem(t):
            if tarefa["tarefa"] in t["tarefa"]:
                self.tasks.remove(t)

        list(map(rem, self.tasks))

    ''' Lista tarefa por prioridade. '''

    def list_tasks(self, prio):

        def prios(p):
            if prio in p["prioridade"]:
                print(p)

        filtro = filter(prios, self.tasks)

        return list(filtro)

    ''' Alterar status da tarefa. '''

    def change_status(self, lista):

        def prios(p):
            if lista[0] in p["status"]:
                if lista[1] in p["tarefa"]:
                    if lista[2] in p["data"]:
                        if lista[3] in p["prioridade"]:

                            if p["status"] == "NOVO":
                                p["status"] = "EM PROCESSO"
                            elif p["status"] == "EM PROCESSO":
                                p["status"] = "FINALIZADA"
                            elif p["status"] == "FINALIZADA":
                                self.remove_task(p)

                            return p

        filtro = filter(prios, self.tasks)

        return list(filtro)

    ''' Lista todas as tarefas'''

    def list_all(self):
        return self.tasks

    def list_last(self):
        return self.tasks[-1]

    ''' Deleta tarefa do tasks. '''

    def deleteTarefa(self, lista):
        # ('NOVO', 'IR AO BANCO', '09/11/2023', 'ALTA')
        def prios(p):
            if lista[0] in p["status"]:
                if lista[1] in p["tarefa"]:
                    if lista[2] in p["data"]:
                        if lista[3] in p["prioridade"]:
                            self.remove_task(p)
                            return True

        filtro = filter(prios, self.tasks)

        if filtro:
            return True

