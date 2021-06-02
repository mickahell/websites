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