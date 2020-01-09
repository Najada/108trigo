all:
	ln -s 108trigo.py 108trigo
	chmod +x 108trigo
clean:
	rm -f 108trigo

fclean: clean
	rm -f *~
re:	fclean all

tests_run:
	make -C tests/
