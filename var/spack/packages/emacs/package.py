# FIXME:
# This is a template package file for Spack.  We've conveniently
# put "FIXME" labels next to all the things you'll want to change.
#
# Once you've edited all the FIXME's, delete this whole message,
# save this file, and test out your package like this:
#
#     spack install emacs
#
# You can always get back here to change things with:
#
#     spack edit emacs
#
# See the spack documentation for more information on building
# packages.
#
from spack import *

class Emacs(Package):
    """GNU Emacs is an extensible, customizable text editor. Begun in the
    mid-1970s as a set of macros on top of TECO, it was re-written
    using C and Emacs Lisp to provide portability and an extendable
    interface. It continues to be actively developed today.

    Emacs provides context-sensitive editing modes with syntax
    coloring, is self documenting, has full Unicode support and
    extensions to do almost anything. It similarly has extensive
    packaging support through the built-in package.el package.

    Emacs' package selection includes color themes, language-specific
    editing modes, RSS readers, email clients, web browsers,
    etc. Die-hard Emacs users do most everything from within Emacs:
    write, compile, run and debug code; read/compose email; browse the
    web; do project planning etc. Some other editors, like Visual
    Studio or Eclipse, provide Emacs keybindings.
    """

    homepage = "https://www.gnu.org/software/emacs/"
    url      = "https://ftp.gnu.org/gnu/emacs/emacs-24.5.tar.xz"

    version('24.5', '50560ee00bac9bb9cf0e822764cd0832')
    version('24.4', 'ad487658ad7421ad8d7b5152192eb945')

    # FIXME: Add dependencies if this package requires them.
    # depends_on("foo")

    def install(self, spec, prefix):
        # TODO: look at CFLAGS as mentioned in the following link
        # http://ergoemacs.org/emacs/building_emacs_on_linux.html#comment-1728596571
        # FIXME: look at which flags are actually needed.
        configure("--prefix=%s" % prefix,
                  "--without-xpm",
                  "--without-jpeg",
                  "--without-tiff",
                  "--without-gif",
                  "--without-png",
                  )

        make()
        make("install")
