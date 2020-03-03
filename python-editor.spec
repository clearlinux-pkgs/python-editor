#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-editor
Version  : 1.0.4
Release  : 27
URL      : https://files.pythonhosted.org/packages/0a/85/78f4a216d28343a67b7397c99825cff336330893f00601443f7c7b2f2234/python-editor-1.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/0a/85/78f4a216d28343a67b7397c99825cff336330893f00601443f7c7b2f2234/python-editor-1.0.4.tar.gz
Summary  : Programmatically open an editor, capture the result
Group    : Development/Tools
License  : Apache-2.0
Requires: python-editor-license = %{version}-%{release}
Requires: python-editor-python = %{version}-%{release}
Requires: python-editor-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
`python-editor` is a library that provides the `editor` module for programmatically
interfacing with your system's $EDITOR.

Examples
--------

```python
import editor
commit_msg = editor.edit(contents=b"# Enter commit message here")
```

Opens an editor, prefilled with the contents, `# Enter commit message here`.
When the editor is closed, returns the contents (bytes) in variable `commit_msg`.
Note that the argument to `contents` needs to be a bytes object on Python 3.


```python
editor.edit(file="README.txt")
```

Opens README.txt in an editor.  Changes are saved in place.  If there is
a `contents` argument then the file contents will be overwritten.

```python
editor.edit(..., use_tty=True)
```

Opens the editor in a TTY.  This is usually done in programs which output is
piped to other programs.  In this case the TTY is used as the editor's stdout,
allowing interactive usage.


How it Works
------------

`editor` first looks for the ${EDITOR} environment variable.  If set, it uses
the value as-is, without fallbacks.

If no $EDITOR is set, editor will search through a list of known editors, and
use the first one that exists on the system.

For example, on Linux, `editor` will look for the following editors in order:

* vim
* emacs
* nano

When calling `editor.edit`, an editor will be opened in a subprocess, inheriting
the parent process's stdin, stdout.

%package license
Summary: license components for the python-editor package.
Group: Default

%description license
license components for the python-editor package.


%package python
Summary: python components for the python-editor package.
Group: Default
Requires: python-editor-python3 = %{version}-%{release}

%description python
python components for the python-editor package.


%package python3
Summary: python3 components for the python-editor package.
Group: Default
Requires: python3-core
Provides: pypi(python-editor)

%description python3
python3 components for the python-editor package.


%prep
%setup -q -n python-editor-1.0.4
cd %{_builddir}/python-editor-1.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583211976
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-editor
cp %{_builddir}/python-editor-1.0.4/LICENSE %{buildroot}/usr/share/package-licenses/python-editor/c700a8b9312d24bdc57570f7d6a131cf63d89016
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-editor/c700a8b9312d24bdc57570f7d6a131cf63d89016

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
