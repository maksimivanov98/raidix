build:
	gcc -Wall -o raidix raidix.c

clean:
	rm raidix

install:
	mkdir -p $(DESTDIR)/usr/bin
	install -m 0755 raidix $(DESTDIR)/usr/bin/raidix
