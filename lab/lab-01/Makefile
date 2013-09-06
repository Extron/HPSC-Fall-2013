
CC = icc
FC = ifort
OPT = 
EXE = triad
OBJ = timing.o dummy.o triad.o

all: $(EXE)

$(EXE): $(OBJ)
	$(FC) -o $(EXE)

%.o: %.c
	$(CC) $(OPT) -c $<

%.o: %.f90
	$(FC) $(OPT) -c $<

build: timing.o dummy.o triad.f90
	$(FC) $(OPT) timing.o dummy.o triad.f90 -o triad  

clean:
	rm -f *.o
	rm -f $(EXE)




