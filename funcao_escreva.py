import sys
def write(*args, sep = " ", end="\n", flush=True):
    texto = sep.join(str(arg) for arg in args)

    texto += end

    sys.stdout.write(texto)

    if flush:
        sys.stdout.flush()

write("Olá, Pessoal")
write("Bem vindos", "ao meu programa!")
write(1+103)
write("a", "e", "i", "o", "u", sep="|")
