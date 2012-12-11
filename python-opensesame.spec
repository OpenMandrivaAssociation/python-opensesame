%define upver	0.25
%define uprel	1

Name:		python-opensesame
Version:	%{upver}
Release:	1
Summary:	Graphical experiment builder
Group:		Sciences/Other
License:	GPLv2
URL:		http://www.cogsci.nl/software/opensesame
Source0:	http://files.cogsci.nl/software/opensesame/opensesame_%{upver}-%{uprel}.tar.gz
Patch0:		opensesame-0.25-mdv-desktop.patch
BuildArch:	noarch
BuildRequires:	pygame pygame-devel python-qt4-devel python-numpy-devel
Requires:	pygame python-qt4 python-numpy
%py_requires

%description
OpenSesame is a graphical experiment builder. OpenSesame provides an easy
to use, point-and-click interface for creating psychological experiments.
In addition to a powerful sketchpad for creating visual stimuli, OpenSesame
features a sampler and synthesizer for sound playback. For more complex tasks,
OpenSesame supports Python scripting using the built-in editor with syntax
highlighting.

%files
%{_bindir}/*
%{_datadir}/opensesame
%{_datadir}/applications/opensesame.desktop
%{py_puresitedir}/opensesame-*.egg-info
%{py_puresitedir}/openexp
%{py_puresitedir}/libopensesame
%{py_puresitedir}/libqtopensesame
%doc README

%prep
%setup -q -n opensesame-%{version}
%patch0 -p1

%build

%install
PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}
chmod 755 %{buildroot}%{py_puresitedir}/libopensesame/misc.py


%changelog
* Tue Dec 06 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.25-1
+ Revision: 738359
- imported package python-opensesame

