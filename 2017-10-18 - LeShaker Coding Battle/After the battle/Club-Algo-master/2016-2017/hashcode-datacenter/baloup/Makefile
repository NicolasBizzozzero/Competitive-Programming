# = MAKEFILE FOR SIMPLE JAVA PROJECTS =

# ===== Configuration =================
ARCHIVE_RENDU = baloup_badiane_TP2
ARCHIVE_RENDU_CONTENT = src tests Makefile Readme.md


SOURCEDIR = src
BINDIR = bin

# class containing the main method
MAINCLASS = Main

# File name of the executable jar file
JARFILE = Pallet.jar
# =====================================


# ========== DONT TOUCH THIS ==========
all: compile

.PHONY: all compile clean exec package rendu

SOURCEFILES := $(patsubst $(SOURCEDIR)/%,%,$(shell find $(SOURCEDIR) -name '*.java'))

CLASSFILES := $(SOURCEFILES:.java=.class)

$(BINDIR)/%.class: $(SOURCEDIR)/%.java
	mkdir -p $(BINDIR)
	javac -d $(BINDIR) -classpath $(SOURCEDIR) $<

compile: $(addprefix $(BINDIR)/,$(CLASSFILES))

package: compile
	jar cvfe $(JARFILE) $(MAINCLASS) -C $(BINDIR) .

clean:
	rm -Rf $(BINDIR) $(JARFILE)

archive: compile clean
	mkdir $(ARCHIVE_RENDU)
	cp -r $(ARCHIVE_RENDU_CONTENT) $(ARCHIVE_RENDU)
	zip -r $(ARCHIVE_RENDU).zip $(ARCHIVE_RENDU)
	rm -Rf $(ARCHIVE_RENDU)

# =====================================


exec: compile
	@java -cp $(BINDIR) $(MAINCLASS) $(COLORS) < $(FILE)
