# Makefile.in generated automatically by automake 1.5 from Makefile.am.

# Copyright 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001
# Free Software Foundation, Inc.
# This Makefile.in is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.



SHELL = /bin/sh

srcdir = .
top_srcdir = ..

prefix = /home/ssi/abarus/source/grep_Mutation/grep_mutant164
exec_prefix = ${prefix}

bindir = ${exec_prefix}/bin
sbindir = ${exec_prefix}/sbin
libexecdir = ${exec_prefix}/libexec
datadir = ${prefix}/share
sysconfdir = ${prefix}/etc
sharedstatedir = ${prefix}/com
localstatedir = ${prefix}/var
libdir = ${exec_prefix}/lib
infodir = ${prefix}/info
mandir = ${prefix}/man
includedir = ${prefix}/include
oldincludedir = /usr/include
pkgdatadir = $(datadir)/grep
pkglibdir = $(libdir)/grep
pkgincludedir = $(includedir)/grep
top_builddir = ..

ACLOCAL = ${SHELL} /home/ssi/abarus/source/grep-2.5.1a/missing --run aclocal
AUTOCONF = ${SHELL} /home/ssi/abarus/source/grep-2.5.1a/missing --run autoconf
AUTOMAKE = ${SHELL} /home/ssi/abarus/source/grep-2.5.1a/missing --run automake
AUTOHEADER = ${SHELL} /home/ssi/abarus/source/grep-2.5.1a/missing --run autoheader

INSTALL = /usr/bin/install -c
INSTALL_PROGRAM = ${INSTALL}
INSTALL_DATA = ${INSTALL} -m 644
INSTALL_SCRIPT = ${INSTALL}
INSTALL_HEADER = $(INSTALL_DATA)
transform = s,x,x,
NORMAL_INSTALL = :
PRE_INSTALL = :
POST_INSTALL = :
NORMAL_UNINSTALL = :
PRE_UNINSTALL = :
POST_UNINSTALL = :
host_alias = 
host_triplet = i686-pc-linux-gnu
AMTAR = ${SHELL} /home/ssi/abarus/source/grep-2.5.1a/missing --run tar
AWK = gawk
BUILD_INCLUDED_LIBINTL = no
CATALOGS =  cs.gmo de.gmo el.gmo eo.gmo es.gmo et.gmo fr.gmo gl.gmo hr.gmo id.gmo it.gmo ja.gmo ko.gmo nl.gmo no.gmo pl.gmo pt_BR.gmo ru.gmo sl.gmo sv.gmo
CATOBJEXT = .gmo
CC = gcc
CPP = gcc -E
DATADIRNAME = share
DEPDIR = .deps
EXEEXT = 
GENCAT = gencat
GETCONF = getconf
GLIBC21 = yes
GMOFILES =  cs.gmo de.gmo el.gmo eo.gmo es.gmo et.gmo fr.gmo gl.gmo hr.gmo id.gmo it.gmo ja.gmo ko.gmo nl.gmo no.gmo pl.gmo pt_BR.gmo ru.gmo sl.gmo sv.gmo
GMSGFMT = /usr/bin/msgfmt
INSTALL_STRIP_PROGRAM = ${SHELL} $(install_sh) -c -s
INSTOBJEXT = .mo
INTLBISON = bison
INTLLIBS = 
INTLOBJS = 
INTL_LIBTOOL_SUFFIX_PREFIX = 
LIBICONV = 
MKINSTALLDIRS = ./mkinstalldirs
MSGFMT = /usr/bin/msgfmt
OBJEXT = o
PACKAGE = grep
POFILES =  cs.po de.po el.po eo.po es.po et.po fr.po gl.po hr.po id.po it.po ja.po ko.po nl.po no.po pl.po pt_BR.po ru.po sl.po sv.po
POSUB = po
RANLIB = ranlib
SEP = :
U = 
USE_INCLUDED_LIBINTL = no
USE_NLS = yes
VERSION = 2.5.1
am__include = include
am__quote = 
install_sh = /home/ssi/abarus/source/grep-2.5.1a/install-sh

AUTOMAKE_OPTIONS = no-dependencies

info_TEXINFOS = grep.texi

man_MANS = grep.1 fgrep.1 egrep.1

EXTRA_DIST = grep.1 egrep.man fgrep.man

CLEANFILES = egrep.1 fgrep.1
subdir = doc
mkinstalldirs = $(SHELL) $(top_srcdir)/mkinstalldirs
CONFIG_HEADER = $(top_builddir)/config.h
CONFIG_CLEAN_FILES =
depcomp =
DIST_SOURCES =
INFO_DEPS = grep.info
DVIS = grep.dvi
TEXINFOS = grep.texi

NROFF = nroff
MANS = $(man_MANS)
DIST_COMMON = Makefile.am Makefile.in mdate-sh stamp-vti texinfo.tex \
	version.texi
all: all-am

.SUFFIXES:
.SUFFIXES: .dvi .info .ps .texi
$(srcdir)/Makefile.in:  Makefile.am  $(top_srcdir)/configure.in $(ACLOCAL_M4)
	cd $(top_srcdir) && \
	  $(AUTOMAKE) --gnu  doc/Makefile
Makefile:  $(srcdir)/Makefile.in  $(top_builddir)/config.status
	cd $(top_builddir) && \
	  CONFIG_HEADERS= CONFIG_LINKS= \
	  CONFIG_FILES=$(subdir)/$@ $(SHELL) ./config.status

$(srcdir)/version.texi:  $(srcdir)/stamp-vti
	@:
$(srcdir)/stamp-vti: grep.texi $(top_srcdir)/configure.in
	@(set `$(SHELL) $(srcdir)/mdate-sh $(srcdir)/grep.texi`; \
	echo "@set UPDATED $$1 $$2 $$3"; \
	echo "@set UPDATED-MONTH $$2 $$3"; \
	echo "@set EDITION $(VERSION)"; \
	echo "@set VERSION $(VERSION)") > vti.tmp
	@cmp -s vti.tmp $(srcdir)/version.texi \
	  || (echo "Updating $(srcdir)/version.texi"; \
	      cp vti.tmp $(srcdir)/version.texi)
	-@rm -f vti.tmp
	@cp $(srcdir)/version.texi $@

mostlyclean-vti:
	-rm -f vti.tmp

maintainer-clean-vti:
	-rm -f $(srcdir)/stamp-vti $(srcdir)/version.texi

grep.info: grep.texi $(srcdir)/version.texi
grep.dvi: grep.texi $(srcdir)/version.texi

.texi.info:
	@cd $(srcdir) && rm -f $@ $@-[0-9] $@-[0-9][0-9]
	cd $(srcdir) \
	  && $(MAKEINFO) $(AM_MAKEINFOFLAGS) $(MAKEINFOFLAGS) \
	       `echo $< | sed 's,.*/,,'`

.texi.dvi:
	TEXINPUTS=$(srcdir):$$TEXINPUTS \
	MAKEINFO='$(MAKEINFO) $(AM_MAKEINFOFLAGS) $(MAKEINFOFLAGS) -I $(srcdir)' \
	$(TEXI2DVI) $<

.texi:
	@cd $(srcdir) && rm -f $@ $@-[0-9] $@-[0-9][0-9]
	cd $(srcdir) \
	  && $(MAKEINFO) $(AM_MAKEINFOFLAGS) $(MAKEINFOFLAGS) \
	       `echo $< | sed 's,.*/,,'`

MAKEINFO = ${SHELL} /home/ssi/abarus/source/grep-2.5.1a/missing --run makeinfo
TEXI2DVI = texi2dvi
DVIPS = dvips
.dvi.ps:
	$(DVIPS) $< -o $@

uninstall-info-am:
	$(PRE_UNINSTALL)
	@if (install-info --version && \
	     install-info --version | fgrep -i -v debian) >/dev/null 2>&1; then \
	  list='$(INFO_DEPS)'; \
	  for file in $$list; do \
	    echo " install-info --info-dir=$(DESTDIR)$(infodir) --remove $(DESTDIR)$(infodir)/$$file"; \
	    install-info --info-dir=$(DESTDIR)$(infodir) --remove $(DESTDIR)$(infodir)/$$file; \
	  done; \
	else :; fi
	@$(NORMAL_UNINSTALL)
	@list='$(INFO_DEPS)'; \
	for file in $$list; do \
	  (if cd $(DESTDIR)$(infodir); then \
	     echo " rm -f $$file $$file-[0-9] $$file-[0-9][0-9])"; \
	     rm -f $$file $$file-[0-9] $$file-[0-9][0-9]; \
	   else :; fi); \
	done

dist-info: $(INFO_DEPS)
	list='$(INFO_DEPS)'; \
	for base in $$list; do \
	  d=$(srcdir); \
	  for file in `CDPATH=: && cd $$d && eval echo $$base*`; do \
	    test -f $(distdir)/$$file \
	    || cp -p $$d/$$file $(distdir)/$$file; \
	  done; \
	done

mostlyclean-aminfo:
	-rm -f grep.aux grep.cp grep.cps grep.dvi grep.fn grep.fns grep.ky grep.log \
	  grep.op grep.pg grep.ps grep.toc grep.tp grep.vr

maintainer-clean-aminfo:
	cd $(srcdir) && \
	for i in $(INFO_DEPS); do \
	  rm -f $$i; \
	  if test "`echo $$i-[0-9]*`" != "$$i-[0-9]*"; then \
	    rm -f $$i-[0-9]*; \
	  fi; \
	done

man1dir = $(mandir)/man1
install-man1: $(man1_MANS) $(man_MANS)
	@$(NORMAL_INSTALL)
	$(mkinstalldirs) $(DESTDIR)$(man1dir)
	@list='$(man1_MANS) $(dist_man1_MANS) $(nodist_man1_MANS)'; \
	l2='$(man_MANS) $(dist_man_MANS) $(nodist_man_MANS)'; \
	for i in $$l2; do \
	  case "$$i" in \
	    *.1*) list="$$list $$i" ;; \
	  esac; \
	done; \
	for i in $$list; do \
	  if test -f $(srcdir)/$$i; then file=$(srcdir)/$$i; \
	  else file=$$i; fi; \
	  ext=`echo $$i | sed -e 's/^.*\\.//'`; \
	  inst=`echo $$i | sed -e 's/\\.[0-9a-z]*$$//'`; \
	  inst=`echo $$inst | sed -e 's/^.*\///'`; \
	  inst=`echo $$inst | sed '$(transform)'`.$$ext; \
	  echo " $(INSTALL_DATA) $$file $(DESTDIR)$(man1dir)/$$inst"; \
	  $(INSTALL_DATA) $$file $(DESTDIR)$(man1dir)/$$inst; \
	done
uninstall-man1:
	@$(NORMAL_UNINSTALL)
	@list='$(man1_MANS) $(dist_man1_MANS) $(nodist_man1_MANS)'; \
	l2='$(man_MANS) $(dist_man_MANS) $(nodist_man_MANS)'; \
	for i in $$l2; do \
	  case "$$i" in \
	    *.1*) list="$$list $$i" ;; \
	  esac; \
	done; \
	for i in $$list; do \
	  ext=`echo $$i | sed -e 's/^.*\\.//'`; \
	  inst=`echo $$i | sed -e 's/\\.[0-9a-z]*$$//'`; \
	  inst=`echo $$inst | sed -e 's/^.*\///'`; \
	  inst=`echo $$inst | sed '$(transform)'`.$$ext; \
	  echo " rm -f $(DESTDIR)$(man1dir)/$$inst"; \
	  rm -f $(DESTDIR)$(man1dir)/$$inst; \
	done
tags: TAGS
TAGS:


DISTFILES = $(DIST_COMMON) $(DIST_SOURCES) $(TEXINFOS) $(EXTRA_DIST)

top_distdir = ..
distdir = $(top_distdir)/$(PACKAGE)-$(VERSION)

distdir: $(DISTFILES)
	@for file in $(DISTFILES); do \
	  if test -f $$file; then d=.; else d=$(srcdir); fi; \
	  dir=`echo "$$file" | sed -e 's,/[^/]*$$,,'`; \
	  if test "$$dir" != "$$file" && test "$$dir" != "."; then \
	    $(mkinstalldirs) "$(distdir)/$$dir"; \
	  fi; \
	  if test -d $$d/$$file; then \
	    cp -pR $$d/$$file $(distdir) \
	    || exit 1; \
	  else \
	    test -f $(distdir)/$$file \
	    || cp -p $$d/$$file $(distdir)/$$file \
	    || exit 1; \
	  fi; \
	done
	$(MAKE) $(AM_MAKEFLAGS) \
	  top_distdir="${top_distdir}" distdir="$(distdir)" \
	  dist-info
check-am: all-am
check: check-am
all-am: Makefile $(INFO_DEPS) $(MANS)

installdirs:
	$(mkinstalldirs) $(DESTDIR)$(infodir) $(DESTDIR)$(man1dir)

install: install-am
install-exec: install-exec-am
install-data: install-data-am
uninstall: uninstall-am

install-am: all-am
	@$(MAKE) $(AM_MAKEFLAGS) install-exec-am install-data-am

installcheck: installcheck-am
install-strip:
	$(MAKE) $(AM_MAKEFLAGS) INSTALL_PROGRAM="$(INSTALL_STRIP_PROGRAM)" \
	  `test -z '$(STRIP)' || \
	    echo "INSTALL_PROGRAM_ENV=STRIPPROG='$(STRIP)'"` install
mostlyclean-generic:

clean-generic:
	-test -z "$(CLEANFILES)" || rm -f $(CLEANFILES)

distclean-generic:
	-rm -f Makefile $(CONFIG_CLEAN_FILES) stamp-h stamp-h[0-9]*

maintainer-clean-generic:
	@echo "This command is intended for maintainers to use"
	@echo "it deletes files that may require special tools to rebuild."
clean: clean-am

clean-am: clean-generic mostlyclean-am

distclean: distclean-am

distclean-am: clean-am distclean-generic

dvi: dvi-am

dvi-am: $(DVIS)

info: info-am

info-am: $(INFO_DEPS)

install-data-am: install-info-am install-man

install-exec-am:

install-info: install-info-am

install-info-am: $(INFO_DEPS)
	@$(NORMAL_INSTALL)
	$(mkinstalldirs) $(DESTDIR)$(infodir)
	@list='$(INFO_DEPS)'; \
	for file in $$list; do \
	  d=$(srcdir); \
	  for ifile in `CDPATH=: && cd $$d && echo $$file $$file-[0-9] $$file-[0-9][0-9]`; do \
	    if test -f $$d/$$ifile; then \
	      echo " $(INSTALL_DATA) $$d/$$ifile $(DESTDIR)$(infodir)/$$ifile"; \
	      $(INSTALL_DATA) $$d/$$ifile $(DESTDIR)$(infodir)/$$ifile; \
	    else : ; fi; \
	  done; \
	done
	@$(POST_INSTALL)
	@if (install-info --version && \
	     install-info --version | fgrep -i -v debian) >/dev/null 2>&1; then \
	  list='$(INFO_DEPS)'; \
	  for file in $$list; do \
	    echo " install-info --info-dir=$(DESTDIR)$(infodir) $(DESTDIR)$(infodir)/$$file";\
	    install-info --info-dir=$(DESTDIR)$(infodir) $(DESTDIR)$(infodir)/$$file || :;\
	  done; \
	else : ; fi
install-man: install-man1

installcheck-am:

maintainer-clean: maintainer-clean-am

maintainer-clean-am: distclean-am maintainer-clean-aminfo \
	maintainer-clean-generic maintainer-clean-vti

mostlyclean: mostlyclean-am

mostlyclean-am: mostlyclean-aminfo mostlyclean-generic mostlyclean-vti

uninstall-am: uninstall-info-am uninstall-man

uninstall-man: uninstall-man1

.PHONY: all all-am check check-am clean clean-generic dist-info \
	distclean distclean-generic distdir dvi dvi-am info info-am \
	install install-am install-data install-data-am install-exec \
	install-exec-am install-info install-info-am install-man \
	install-man1 install-strip installcheck installcheck-am \
	installdirs maintainer-clean maintainer-clean-aminfo \
	maintainer-clean-generic maintainer-clean-vti mostlyclean \
	mostlyclean-aminfo mostlyclean-generic mostlyclean-vti \
	uninstall uninstall-am uninstall-info-am uninstall-man \
	uninstall-man1


fgrep.1: fgrep.man
	inst=`echo "grep" | sed '$(transform)'`.1; \
sed -e "s%@grep@%$$inst%g" $(srcdir)/fgrep.man > $@

egrep.1: egrep.man
	inst=`echo "grep" | sed '$(transform)'`.1; \
sed -e "s%@grep@%$$inst%g" $(srcdir)/egrep.man > $@
# Tell versions [3.59,3.63) of GNU make to not export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
.NOEXPORT:
