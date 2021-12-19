# Faça um programa que tenha uma funçao notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informaçoes:
# quantidade de notas
# maior nota
# menor nota
# a média da turma
# a situação (opcional)
# adicione também as docstring da funçã
ficha = dict()


def notas(*notas, sit=False):
    """
    mostrar as notas e informaçoes das notas
    :param notas: notas do aluno
    :param sit: (opcional) mostar ou não a situação
    :return: retorna um dicionario com as notas do aluno
    """
    ficha['total'] = len(notas)
    ficha['maior'] = max(notas)
    ficha['menor'] = min(notas)
    ficha['media'] = sum(notas)/len(notas)
    if sit:
        if ficha['media'] > 6:
            ficha['stuacao'] = 'BOA'
        if ficha['media'] > 5:
            ficha['situacao'] = 'RASOAVEL'
        if ficha['media'] <= 5:
            ficha['situacao'] = 'RUIM'
    return ficha


resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)


