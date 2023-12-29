Name:		texlive-changebar
Version:	69220
Release:	1
Summary:	Generate changebars in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/changebar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changebar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changebar.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changebar.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/changebar
%doc %{_texmfdistdir}/doc/latex/changebar
#- source
%doc %{_texmfdistdir}/source/latex/changebar

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
