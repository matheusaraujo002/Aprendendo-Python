cpf = input('Digite o CPF para verificar: ')
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')

if len(cpf) == 11 and cpf.isdigit():
  a = int(cpf[0])
  b = int(cpf[1])
  c = int(cpf[2])
  d = int(cpf[3])
  e = int(cpf[4])
  f = int(cpf[5])
  g = int(cpf[6])
  h = int(cpf[7])
  i = int(cpf[8])
  
  dv1 = 10*a + 9*b + 8*c + 7*d + 6*e + 5*f + 4*g + 3*h + 2*i
  dv1 = dv1 % 11
  
  if dv1 < 2:
    dv1 = 0
  else:
    dv1 = 11 - dv1
    
  dv2 = 11*a + 10*b + 9*c + 8*d + 7*e + 6*f + 5*g + 4*h + 3*i + 2*dv1
  dv2 = dv2 % 11
  
  if dv2 < 2:
    dv2 = 0
  else:
    dv2 = 11 - dv2

  if int(cpf[9]) == dv1 and int(cpf[10]) == dv2:
    print("CPF válido.")
  else:
    print("CPF inválido.")
else:
  print("CPF inválido. Certifique-se de inserir 11 dígitos numéricos.")