Name:		texlive-hyphen-catalan
Version:	58609
Release:	2
Summary:	Catalan hyphenation patterns
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-catalan.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Catalan in T1/EC and UTF-8 encodings.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-catalan
%_texmf_language_def_d/hyphen-catalan
%_texmf_language_lua_d/hyphen-catalan
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-catalan <<EOF
\%% from hyphen-catalan:
catalan loadhyph-ca.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-catalan
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-catalan <<EOF
\%% from hyphen-catalan:
\addlanguage{catalan}{loadhyph-ca.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-catalan
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-catalan <<EOF
-- from hyphen-catalan:
	['catalan'] = {
		loader = 'loadhyph-ca.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-ca.pat.txt',
		hyphenation = 'hyph-ca.hyp.txt',
	},
EOF
