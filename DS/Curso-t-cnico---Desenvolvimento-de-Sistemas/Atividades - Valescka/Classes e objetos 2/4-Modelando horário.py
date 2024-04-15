#4. Crie uma classe para representar um horario (hora, minuto e segundo). 
#Implemente os metodos para fazer as operacoes de incremento (de segundos) no horario e diferença entre dois horarios.
class Horario:
  def __init__(self, hora, minuto, segundo):
    self.hora = hora
    self.minuto = minuto
    self.segundo = segundo

  def incrementar(self, segundos):
    self.segundo += segundos
    while self.segundo >= 60:
      self.segundo -= 60
      self.minuto += 1
    while self.minuto >= 60:
      self.minuto -= 60
      self.hora += 1

  def diferenca(self, outro_horario):
    segundos_self = self.hora * 3600 + self.minuto * 60 + self.segundo
    segundos_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo
    return segundos_self - segundos_outro

horario1 = Horario(10, 30, 0)
horario2 = Horario(11, 0, 0)

print("Horário 1:", horario1.hora, ":", horario1.minuto, ":", horario1.segundo)
print("Horário 2:", horario2.hora, ":", horario2.minuto, ":", horario2.segundo)

horario1.incrementar(3600)
print("Horário 1 após incremento:", horario1.hora, ":", horario1.minuto, ":", horario1.segundo)

diferenca = horario2.diferenca(horario1)
print("Diferença entre os horários:", diferenca, "segundos")