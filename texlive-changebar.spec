# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/changebar
# catalog-date 2009-09-24 20:53:04 +0200
# catalog-license lppl
# catalog-version 3.5c
Name:		texlive-changebar
Version:	3.5c
Release:	1
Summary:	Generate changebars in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/changebar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changebar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changebar.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changebar.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Identify areas of text to be marked with changebars with the
\cbstart and \cbend commands; the bars may be coloured. The
package uses 'drivers' to place the bars; the available drivers
can work with dvitoln03, dvitops, dvips, the emTeX and TeXtures
DVI drivers, and VTeX and PDFTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/changebar/changebar.sty
%doc %{_texmfdistdir}/doc/latex/changebar/00readme.txt
%doc %{_texmfdistdir}/doc/latex/changebar/catalog.txt
%doc %{_texmfdistdir}/doc/latex/changebar/cbtest1-ltx.pdf
%doc %{_texmfdistdir}/doc/latex/changebar/cbtest1-pdf.pdf
%doc %{_texmfdistdir}/doc/latex/changebar/cbtest1.tex
%doc %{_texmfdistdir}/doc/latex/changebar/cbtest2-ltx.pdf
%doc %{_texmfdistdir}/doc/latex/changebar/cbtest2-pdf.pdf
%doc %{_texmfdistdir}/doc/latex/changebar/cbtest2.tex
%doc %{_texmfdistdir}/doc/latex/changebar/changebar.bug
%doc %{_texmfdistdir}/doc/latex/changebar/changebar.pdf
%doc %{_texmfdistdir}/doc/latex/changebar/chbar.1
%doc %{_texmfdistdir}/doc/latex/changebar/chbar.sh
%doc %{_texmfdistdir}/doc/latex/changebar/manifest.txt
#- source
%doc %{_texmfdistdir}/source/latex/changebar/changebar.dtx
%doc %{_texmfdistdir}/source/latex/changebar/changebar.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
