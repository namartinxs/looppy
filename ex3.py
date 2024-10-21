nome= input("INSIRA SEU NOME ")
while(len(nome)< 3):
    nome= input("O NOME DEVE TER MAIS DO QUE TRÊS CARACTERES\nINSIRA SEU NOME ")
idade= int(input("INSIRA SUA IDADE "))
while(idade < 0) or (idade > 150):
    idade= int(input("SUA IDADE DEVE SER ENTRE 0-150 ANOS\nINSIRA SUA IDADE "))
salario= float(input("INSIRA SEU SALÁRIO "))
while(salario < 0):
    salario= input("SALÁRIO DEVE SER MAIR QUE ZERO\nINSIRA SEU SALÁRIO ")
sexo= input("INSIRA SEU SEXO ")
sexo = sexo.lower()
while (sexo[0] != "f") and (sexo[0] != "m"):
   sexo= input("DEVE SER FEMININO OU MASCULINO\nINSIRA SEU SEXO ") 
estado_civil= input("INSIRA SEU ESTADO CIVIL")
estado_civil = estado_civil.lower()
while(estado_civil[0]!= "s") and (estado_civil[0]!= "c") and (estado_civil[0]!= "v") and (estado_civil[0]!= "d"):
    estado_civil= input("ESTADO CIVIL DEVE SER SOLTEIRO(A), CASADO(A), VIUVO(A) OU DIVORCIADO(A)\nINSIRA SEU ESTADO CIVIL")

sexo = "feminino" if sexo[0] == "f" else "masculino" 

if estado_civil[0]=="s" and sexo[0] == "f":
    estado_civil= "solteira"
elif estado_civil[0]=="s" and sexo[0] == "m":
    estado_civil = "solteiro" 

elif estado_civil[0]=="c" and sexo[0] == "f":
    estado_civil= "casada"
elif estado_civil[0]=="c" and sexo[0] == "m":
    estado_civil = "casado" 

elif estado_civil[0]=="v" and sexo[0] == "f":
    estado_civil= "viuva"
elif estado_civil[0]=="v" and sexo[0] == "m":
    estado_civil = "viuvo" 
elif estado_civil[0]=="d" and sexo[0] == "f":
    estado_civil= "divorciada"
else:
    estado_civil = "divorciado" 

print(f"DADOS DO USUÁRIO:\nNOME:{nome}\nIDADE:{idade}\nSALÁRIO:R${salario}\nSEXO:{sexo}\nESTADO CIVIL:{estado_civil}\n")

