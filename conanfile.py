import os
import shutil
import sys

from conans import ConanFile, tools

class QtConan(ConanFile):
    name = "qtbase"
    version = "5.11.3"
    description = "Qt Base (Core, Gui, Widgets, Network, ...)"
    topics = ("conan", "qt", "ui")
    url = "https://github.com/altairwei/conan-qtbase"
    homepage = "https://www.qt.io"
    license = "LGPL-3.0-only"
    author = "Altair Wei <altair_wei@outlook.com>"
    exports = ["*.diff"]
    settings = "os", "arch", "compiler", "build_type"

    def source(self):
        url = "https://download.qt.io/archive/qt/{0}/{1}/submodules/qtbase-everywhere-src-{1}" \
            .format(self.version[:self.version.rfind('.')], self.version)
        if tools.os_info.is_windows:
            tools.get("%s.zip" % url, md5='3ae01e0ac7d5301ff05a15dd34faf0d3')
        elif sys.version_info.major >= 3:
            tools.get("%s.tar.xz" % url, md5='dd5a2a295c38cbb852cb7b45cb3a8e27')
        else:  # python 2 cannot deal with .xz archives
            self.run("wget -qO- %s.tar.xz | tar -xJ " % url)
        shutil.move("qtbase-everywhere-src-%s" % self.version, "qtbase")

        for patch in ["cc04651dea4c4678c626cb31b3ec8394426e2b25.diff"]:
            tools.patch("qtbase", patch)