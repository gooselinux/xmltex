Summary:	Namespace-aware XML parser written in TeX
Name:		xmltex
Version:	20020625
Release:	16%{?dist}
License:	LPPL
Group:		Applications/Publishing
URL:	http://www.dcarlisle.demon.co.uk/xmltex/manual.html
#Source0 located at ftp://ftp.tex.ac.uk/tex-archive/macros/xmltex
Source0:	xmltex-1.9.tar.gz
Source1:	xmltex.1
Requires:	tex(latex)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: tex(latex)

%description
Namespace-aware XML parser written in TeX.

%prep
%setup -q -c %{name}-%{version}
mv -f xmltex/base/* .


%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/xmltex
install -d $RPM_BUILD_ROOT%{_bindir}
install -p -m 0644 *.xmt %{name}.cfg *.ini *.tex $RPM_BUILD_ROOT%{_datadir}/texmf/tex/xmltex
ln -s pdftex ${RPM_BUILD_ROOT}%{_bindir}/pdf%{name}
ln -s latex ${RPM_BUILD_ROOT}%{_bindir}/%{name}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -c -p -m 0644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_mandir}/man1
ln -s xmltex.1.gz ${RPM_BUILD_ROOT}%{_mandir}/man1/pdfxmltex.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :
for f in xmltex pdfxmltex; do
/usr/bin/env - PATH=$PATH:%{_bindir} fmtutil-sys --byfmt $f > /dev/null 2>&1
done
exit 0

%postun
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :

%triggerin -- texlive
for f in xmltex pdfxmltex; do
/usr/bin/env - PATH=$PATH:%{_bindir} fmtutil-sys --byfmt $f > /dev/null 2>&1
done
exit 0

%files
%defattr(-,root,root,-)
%doc readme.txt manual.html
%attr(755,root,root) %{_bindir}/xmltex
%attr(755,root,root) %{_bindir}/pdfxmltex
%{_datadir}/texmf/tex/xmltex
%{_mandir}/man1/xmltex.1*
%{_mandir}/man1/pdfxmltex.1*

%changelog
* Fri Dec 11 2009 Ondrej Vasik <ovasik@redhat.com> - 20020625-16
- Merge review(#226567) - fix buildroot, source0 location, do not
  zip readme.txt

* Fri Aug 28 2009 Ondrej Vasik <ovasik@redhat.com> - 20020625-15
- ship xmltex manpage from Debian

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020625-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 Ondrej Vasik <ovasik@redhat.com> - 20020625-13
- fix trigger to use texlive instead of virtual provide

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020625-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 20 2008 Ondrej Vasik <ovasik@redhat.com> - 20020625-11
- use Texlive provides

* Wed Mar 19 2008 Stepan Kasal <skasal@redhat.com> - 20020625-10
- drop xmltexfmtutil.cnf, the system fmtutil.cnf defines xmltex
  formats
- do not package (nor build) %%{_datadir}/texmf/web2c/*.fmt; these
  days, formats are built when the rpm is installed, and go to another
  directory

* Mon Jan  7 2008 Ondrej Vasik <ovasik@redhat.com> - 20020625-9
- used texcongig-sys rehash instead of texhash
- added URL
- added dist tag
- shortened License tag

* Fri Jul 14 2006 Jesse Keating <jkeating@redhat.com> - 20020625-8
- rebuild

* Tue Feb  7 2006 Tim Waugh <twaugh@redhat.com> 20020625-7
- Fix xmltex symlink (-> latex) (bug #168728).

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Sep 20 2005 Tim Waugh <twaugh@redhat.com> 20020625-6
- Build fmt file using &latex not &hugelatex (bug #168728).

* Wed Mar  2 2005 Tim Waugh <twaugh@redhat.com> 20020625-5
- Use fmtutil-sys instead of fmtutil (bug #150089).
- Use etex/pdfetex as engine.

* Wed Mar  2 2005 Tim Waugh <twaugh@redhat.com> 20020625-4
- Rebuild for new teTeX.

* Wed Sep 22 2004 Than Ngo <than@redhat.com> 20020625-3
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jan 16 2004 Tim Waugh <twaugh@redhat.com> 20020625-1
- Slightly newer upstream version.

* Thu Nov 27 2003 Tim Waugh <twaugh@redhat.com> 20020118-15
- Build requires tetex (bug #110736).

* Fri Sep 12 2003 Tim Waugh <twaugh@redhat.com> 20020118-14.1
- Rebuilt.

* Fri Sep 12 2003 Tim Waugh <twaugh@redhat.com> 20020118-14
- Requires tetex-latex (bug #104307).

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Nov 20 2002 Tim Powers <timp@redhat.com>
- rebuild in current collinst

* Tue Jul 23 2002 Tim Powers <timp@redhat.com> 20020118-11
- rebuild using gcc-3.2-0.1

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 20020118-10
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com> 20020118-9
- automated rebuild

* Thu Feb 21 2002 Tim Waugh <twaugh@redhat.com> 20020118-8
- Fix group (bug #60177).

* Thu Feb 21 2002 Tim Waugh <twaugh@redhat.com> 20000118-7
- Rebuild in new environment.

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 20000118-6
- automated rebuild

* Wed Dec 12 2001 Tim Waugh <twaugh@redhat.com> 20000118-5
- Trigger recreation of the format file on tetex-latex.

* Wed Dec  5 2001 Tim Waugh <twaugh@redhat.com> 20000118-4
- New xmltex.tex (from Sebastian).
- Fmt files should be marked as ghosts so that RPM verification works.

* Sat Oct  6 2001 Tim Waugh <twaugh@redhat.com> 20000118-3
- Built for Red Hat Linux.  Package from PLD.

* Sat Oct  6 2001 PLD Team <pld-list@pld.org.pl>
All persons listed below can be reached at <cvs_login>@pld.org.pl

$Log: xmltex.spec,v $
Revision 1.6  2001/03/27 16:50:29  wiget
add xmltex.cfg file and one missing dir in %%files; release 3

Revision 1.5  2001/03/27 11:10:41  wiget
include xmltex macros; requires tex/pdftex

Revision 1.4  2001/01/24 14:18:54  klakier
- archive file changed

Revision 1.3  2001/01/24 13:28:40  klakier
- link fixed

Revision 1.2  2001/01/24 12:34:27  klakier
- added Version and more doc

Revision 1.1  2001/01/24 12:03:51  klakier
- initial

