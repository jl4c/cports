pkgname = "acpica"
pkgver = "20260408"
pkgrel = 1
build_style = "makefile"
make_build_args = ["NOFORTIFY=TRUE", "NOWERROR=TRUE"]
make_use_env = True
hostmakedepends = ["bison", "flex"]
pkgdesc = "Intel ACPI Component Architecture utilities"
license = "GPL-2.0-only OR BSD-3-Clause-acpica OR Intel-ACPI"
url = "https://www.acpica.org"
source = (
    f"https://github.com/open-acpica/acpica/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "ddc5d3e0f54030e2348484fff681861a161efb4e388e20631209574e7884ad39"
tool_flags = {"CFLAGS": ["-Wno-unknown-warning-option"]}
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
