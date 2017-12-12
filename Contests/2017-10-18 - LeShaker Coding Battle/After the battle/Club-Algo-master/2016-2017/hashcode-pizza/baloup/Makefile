# nom d'archive
ARCHIVE=TP4_Baloup_Badiane.zip


# fichiers binaires à produire
# les prérequis (.o) des binaires sont à définir plus bas dans le fichier
BINARIES = pizza

# commande de compilation
CCPP      = g++
CC      = gcc

# options de compilation (.o et linkage)
CPPFLAGS  = -O3 -std=c++11
CFLAGS  = -O3 -std=c11

LDLIBS = -lz






# =========== NE PAS TOUCHER ===========
# commande 'make' sans argument
all: ${BINARIES}

#LDLIBS  = -L${LIBDIR} $(addprefix -l,$(LIBS))

# Compilation séparée
%.opp: %.cpp
	${CCPP} ${CPPFLAGS} -o $@ -c $<
%.o: %.c
	${CC} ${CFLAGS} -c $<

clean:
	rm *.o ${BINARIES} || true

# cible utilisée pour le rendu sous forme d'archive
archive: clean
	zip -r ../${ARCHIVE} *

.PHONY: all clean archive

${BINARIES}:
	${CCPP} ${CPPFLAGS} -o $@ $^ ${LDLIBS}
#${CC} ${CFLAGS} -o $@ $^
# ======================================




# ----- les exécutables à produire -----
pizza: pizza.opp gzstream.opp
