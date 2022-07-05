#Nome: Lucas Batista Pereira
#Matricula: 2020007290
#COM 220
#TRAB 6

class Aluno:
    def __init__(self, matric, nome, curso):
        self.matric = matric
        self.nome = nome
        self.curso = curso
        self.historico = Historico(curso) #Arriquei fazer a composição de historico com 'Aluno'
        
    def getDados(self):
        print("Nome do Aluno(a): {}".format(self.nome))
        print("Matricula do Aluno(a): {}".format(self.matric))
        print("Curso do Aluno(a): {}".format(self.curso.nome))

    def mostrarDisciplinasCurso(self):
        print("Disciplinas do curso: {} | Aluno(a): {}".format(self.curso.nome, self.nome))
        self.curso.mostrar_disciplinasGrade()
        
    def adicionarDisciplinaAluno(self, disciplina):
        self.historico.adicionarDisiciplina(disciplina)

    def mostrarTodasDisciplinasAluno(self):
        print("Todas as disciplinas do histórico | Aluno(a): {}".format(self.nome))
        self.historico.mostrarTodasDisiciplinas()

class Curso:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
        self.grade = Grade(nome, ano)

    def insere_cursoGrade(self, disciplina):
        self.grade.disciplinas.append(disciplina)  

    def mostrar_disciplinasGrade(self):
        soma = 0
        for disciplina in self.grade.disciplinas:
            print("--> Disciplina: {} | Código: {} | Carga Horária: {}".format(disciplina.nome, disciplina.codigo, disciplina.cargaHoraria))
            soma += disciplina.cargaHoraria
        print(">> Carga Horária total do curso: {}".format(soma))

    def getNomeCurso(self):
        return self.nome

class Grade:
    def __init__(self, curso, ano):
        self.curso = curso
        self.ano = ano
        self.disciplinas = []

class Disciplina:
    def __init__(self, nome, codigo, cargaHoraria):
        self.codigo = codigo
        self.nome = nome
        self.cargaHoraria = cargaHoraria

class Historico:
    def __init__(self, curso):
        self.curso = curso
        self.historico_disciplinas = []
        self.somaObrigatoria = 0
        self.somaEletiva = 0

        for disciplina in self.curso.grade.disciplinas:
            self.historico_disciplinas.append(disciplina)
            self.somaObrigatoria += disciplina.cargaHoraria
        

    def adicionarDisiciplina(self, disciplina):
        self.historico_disciplinas.append(disciplina)
        self.somaEletiva += disciplina.cargaHoraria

    def mostrarTodasDisiciplinas(self):
        for disciplina in self.historico_disciplinas:
            print("--> Disciplina: {} | Código: {} | Carga Horária: {}".format(disciplina.nome, disciplina.codigo, disciplina.cargaHoraria))
        print(">> Soma das horas de disciplinas obrigatórias: {}".format(self.somaObrigatoria))
        print(">> Soma das horas de disciplinas eletivas: {}".format(self.somaEletiva))

if __name__ == "__main__":

    #Disciplinas que compõem a grade de CCO
    listaDscpCCO = []
    dscpCCO1 = Disciplina("Matématica discreta", 1000, 64)
    dscpCCO2 = Disciplina("Calculo Númerico", 1001, 64)
    dscpCCO3 = Disciplina("Arquitetura de computadores", 1002, 64)

    listaDscpCCO.append(dscpCCO1)
    listaDscpCCO.append(dscpCCO2)
    listaDscpCCO.append(dscpCCO3)

    #Disciplinas que compões a grade de SIN
    listaDscpSIN = []
    dscpSIN1 = Disciplina("Negócios e informática", 2000, 64)
    dscpSIN2 = Disciplina("Administração de redes", 2001, 64)
    dscpSIN3 = Disciplina("organização informática", 2002, 64)

    listaDscpSIN.append(dscpSIN1)
    listaDscpSIN.append(dscpSIN2)
    listaDscpSIN.append(dscpSIN3)

    #Disiciplinas opcionais
   
    dscpOPC1 = Disciplina("Opcional 1", 3000, 48)
    dscpOPC2 = Disciplina("Opcional 2", 3001, 48)
    dscpOPC3 = Disciplina("Opcional 3", 3002, 48)

    #Declararação dos cursos
    cursoCCO = Curso("CCO", 2021)
    cursoSIN = Curso("SIN", 2021)

    #Preenchimento das grades dos cursos
    for Disciplina in listaDscpCCO:
        cursoCCO.insere_cursoGrade(Disciplina)

    for Disciplina in listaDscpSIN:
        cursoSIN.insere_cursoGrade(Disciplina)

    #Declaração dos Alunos em seus respectivos cursos
    aluno1 = Aluno(400, "João", cursoCCO)
    aluno2 = Aluno(420, "Maria", cursoSIN)

    #Mostra os dados dos alnunos
    aluno1.getDados()
    print()
    aluno2.getDados()
    print()

    #Mostras as disiciplinas do curso de cada aluno
    aluno1.mostrarDisciplinasCurso()
    print()
    aluno2.mostrarDisciplinasCurso()
    print()

    #Adiciona disciplinas opicionais para cada aluno
    aluno1.adicionarDisciplinaAluno(dscpOPC1)
    aluno2.adicionarDisciplinaAluno(dscpOPC2)
    aluno2.adicionarDisciplinaAluno(dscpOPC3)

    #Mostra todas as materias do historico de cada aluno
    aluno1.mostrarTodasDisciplinasAluno()
    print()
    aluno2.mostrarTodasDisciplinasAluno()