Name:		texlive-carolmin-ps
Version:	15878
Release:	2
Summary:	Adobe Type 1 format of Carolingian Minuscule fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/carolmin-ps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carolmin-ps.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carolmin-ps.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle offers Adobe Type 1 format versions of Peter
Wilson's Carolingian Minuscule font set (part of the bookhands
collection). The fonts in the bundle are ready-to-use
replacements for the MetaFont originals.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/carolmin-ps/cmin10.afm
%{_texmfdistdir}/fonts/afm/public/carolmin-ps/cmin17.afm
%{_texmfdistdir}/fonts/afm/public/carolmin-ps/cmin7.afm
%{_texmfdistdir}/fonts/afm/public/carolmin-ps/cminb10.afm
%{_texmfdistdir}/fonts/afm/public/carolmin-ps/cminb17.afm
%{_texmfdistdir}/fonts/afm/public/carolmin-ps/cminb7.afm
%{_texmfdistdir}/fonts/map/dvips/carolmin-ps/cmin.map
%{_texmfdistdir}/fonts/type1/public/carolmin-ps/cmin10.pfb
%{_texmfdistdir}/fonts/type1/public/carolmin-ps/cmin17.pfb
%{_texmfdistdir}/fonts/type1/public/carolmin-ps/cmin7.pfb
%{_texmfdistdir}/fonts/type1/public/carolmin-ps/cminb10.pfb
%{_texmfdistdir}/fonts/type1/public/carolmin-ps/cminb17.pfb
%{_texmfdistdir}/fonts/type1/public/carolmin-ps/cminb7.pfb
%doc %{_texmfdistdir}/doc/fonts/carolmin-ps/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
