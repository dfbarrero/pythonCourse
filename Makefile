all:
	@for a in $$(ls); do \
		if [ -d $$a ]; then \
			echo "Compilando directorio $$a"; \
            $(MAKE) -C $$a; \
        fi; \
	done;
	@echo "Hecho"
