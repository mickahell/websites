if(location.pathname=="/tree") {
        if (window.confirm('By clicking OK you agree to have read the Term of use of this platform, if not please click Cancel to be redirect to read them.'))
        {
        }
        else{
        window.location.href='https://quantum-lab.xtraorbitals.xyz/#term-of-use';
        };
};

window.addEventListener('unload', function() {
    // For Firefox
    IPython.notebook.session.delete();
});

window.onbeforeunload = function () {
    // For Chrome
    IPython.notebook.session.delete();
};

$( window ).unload(function() {
  IPython.notebook.kernel.kill();
});
