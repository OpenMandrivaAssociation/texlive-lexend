Name:		texlive-lexend
Version:	57564
Release:	1
Summary:	The Lexend fonts for XeLaTeX and LuaLaTeX through fontspec
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lexend
License:	lppl1.3c ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lexend.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lexend.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The purpose of this package is pretty straightforward: The
Lexend font collection has been designed by Dr. Bonnie
Shaver-Troup and Thomas Jockin to make reading easier for
everyone. Now my goal is to bring this wonderful collection to
the world of LaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/lexend
%{_texmfdistdir}/fonts/truetype/public/lexend
%doc %{_texmfdistdir}/doc/fonts/lexend

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
