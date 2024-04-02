BINDIR= ./bin
SRCDIR= ./src
CCFLAGS= -Wall
SCFLAGS= -Wall -S
GCC= gcc
TARGET= output

cc:		$(wildcard $(SRCDIR)/*.c)
		$(GCC) $(CCFLAGS) $< -o $(TARGET)					# zkompiluje soubor .c ve slozce $(SRCDIR) do exe souboru s nazvem $(OUTPUT), flag -Wall povoluje vsechny mozne varovani compileru
		mkdir -p $(BINDIR) 									# -p vytvori slozku, pokud neexistuje
		mv $(TARGET) $(BINDIR)

asm:	$(wildcard $(SRCDIR)/*.c)
		$(GCC) $(SCFLAGS) $< -o $(TARGET).s					# -S generuje zdrojak v assembleru -> $(TARGET).s
		mkdir -p $(BINDIR)
		mv $(TARGET).s	 $(BINDIR)

clean:
	rm -rf $(BINDIR)