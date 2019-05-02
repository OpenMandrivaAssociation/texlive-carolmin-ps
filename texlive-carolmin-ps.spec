# revision 15878
# category Package
# catalog-ctan /fonts/carolmin-ps
# catalog-date 2007-02-21 12:51:17 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-carolmin-ps
Version:	20190228
Release:	1
Summary:	Adobe Type 1 format of Carolingian Minuscule fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/carolmin-ps
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carolmin-ps.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/carolmin-ps.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070221-2
+ Revision: 749976
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070221-1
+ Revision: 718008
- texlive-carolmin-ps
- texlive-carolmin-ps
- texlive-carolmin-ps
- texlive-carolmin-ps
- texlive-carolmin-ps

