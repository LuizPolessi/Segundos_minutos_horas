def horario_segundo(hor):
   horas, minutos, segundos = map(int, hor.split(':'))
    
   total_segundos = horas*3600 + minutos*60 + segundos
   return total_segundos

def horario_minuto(hor):
   horas, minutos, segundos = map(int, hor.split(':'))

   total_minutos = horas*60 + minutos + segundos/60
   return total_minutos

def horario_hora(hor):
   horas, minutos, segundos = map(int, hor.split(':'))

   total_horas = horas + minutos/60 + segundos/3600
   return total_horas
   
hor = '01:30:45' 
resultado_segundos = horario_segundo(hor)
resultado_minutos = horario_minuto(hor)
resultado_horas = horario_hora(hor)

print(f'O horário {hor} equivale a {resultado_segundos} segundos')
print(f'O horário {hor} equivale a {resultado_minutos} minutos')
print(f'O horário {hor} equivale a  {resultado_horas} horas')