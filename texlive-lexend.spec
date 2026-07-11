%global tl_name lexend
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.0.70
Release:	%{tl_revision}.1
Summary:	The Lexend fonts for XeLaTeX and LuaLaTeX through fontspec
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/lexend
License:	lppl1.3c ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lexend.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lexend.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The purpose of this package is pretty straightforward: The Lexend font
collection has been designed by Dr. Bonnie Shaver-Troup and Thomas
Jockin to make reading easier for everyone. Now my goal is to bring this
wonderful collection to the world of LaTeX.

