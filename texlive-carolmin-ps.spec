%global tl_name carolmin-ps
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Adobe Type 1 format of Carolingian Minuscule fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/carolmin-ps
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/carolmin-ps.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/carolmin-ps.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle offers Adobe Type 1 format versions of Peter Wilson's
Carolingian Minuscule font set (part of the bookhands collection). The
fonts in the bundle are ready-to-use replacements for the Metafont
originals.

