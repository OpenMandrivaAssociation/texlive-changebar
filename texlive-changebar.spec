%global tl_name changebar
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.7e
Release:	%{tl_revision}.1
Summary:	Generate changebars in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/changebar
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/changebar.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/changebar.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/changebar.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Identify areas of text to be marked with changebars with the \cbstart
and \cbend commands; the bars may be coloured. The package uses
'drivers' to place the bars; the available drivers can work with
dvitoln03, dvitops, dvips, the emTeX and TeXtures DVI drivers, and VTeX
and pdfTeX.

