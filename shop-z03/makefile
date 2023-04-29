Tests: Tests.o Product.o Money.o Database.o Date.o
	g++ -o tests.out Tests.o Product.o Money.o Database.o Date.o

Tests.o: Tests.cpp
	g++ -c Tests.cpp

Product.o: Product.cpp
	g++ -c Product.cpp

Money.o: Money.cpp
	g++ -c Money.cpp

Date.o: Date.cpp
	g++ -c Date.cpp

Database.o: Database.cpp
	g++ -c Database.cpp


clean:
	rm -f tests.out Tests.o Product.o Database.o Money.o Date.o