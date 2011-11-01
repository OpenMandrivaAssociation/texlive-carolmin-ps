Name:		texlive-carolmin-ps
Version:	20070221
Release:	1
Summary:	Adobe Type 1 format of Carolingian Minuscule fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/carolmin-ps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carolmin-ps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carolmin-ps.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The bundle offers Adobe Type 1 format versions of Peter
Wilson's Carolingian Minuscule font set (part of the bookhands
collection). The fonts in the bundle are ready-to-use
replacements for the MetaFont originals.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
