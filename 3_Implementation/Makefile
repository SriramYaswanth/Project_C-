PROJ_NAME = SMART_SWITCH
SRC= appliances.cpp main.cpp

TEST_SRC= smartsw_test.cpp appliances.cpp

ifdef OS
   RM = del /q
   FixPath = $(subst /,\,$1)
   EXEC = exe
else
   ifeq ($(shell uname), Linux)
      RM = rm -rf
      FixPath = $1
	   EXEC = out
   endif
endif


Build : $(SRC) #remember to use this in .github/workflow
	g++ $(SRC) -o $(call FixPath,$(PROJ_NAME).$(EXEC)) -lm

run : Build
	./$(call FixPath,$(PROJ_NAME).$(EXEC))


build_test : 
	g++ $(TEST_SRC) -o $(call FixPath,$(PROJ_NAME).$(EXEC)) -lm -lgtest -lgtest_main -lpthread

run_test : build_test
	./$(call FixPath,$(PROJ_NAME).$(EXEC))

Analyse:
	cppcheck --enable=all $(SRC)

Valgrind: Build
	valgrind ./$(call FixPath,$(PROJ_NAME).$(EXEC))

coverage:
	g++ -fprofile-arcs -ftest-coverage $(SRC) -o $(call FixPath,$(PROJ_NAME).$(EXEC)) -lm
	gcov -a $(call FixPath,$(PROJ_NAME).$(EXEC))

clean:
	$(RM) $(call FixPath,*.out)