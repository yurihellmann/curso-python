arquivo = open(
    r"C:\Users\yuri\Documents\Cursos\05 - Python\03 - Manipulação de arquivos\teste.txt", "w"
)

arquivo.write("I have brought peace, freedom, justice and security to my new Empire!")
arquivo.writelines(["\n" "Your ", "new ", "Empire?"])
arquivo.writelines("\nDon't make me kill you!")
arquivo.writelines("\nAnakin my allegiance is to the republic to democracy!")
arquivo.writelines("\nIf you're not with me, then you're my enemy.")
arquivo.writelines("\nOnly a sith deals in absolutes. I will do what I must.")
arquivo.writelines("\nYou will try.")
arquivo.close()