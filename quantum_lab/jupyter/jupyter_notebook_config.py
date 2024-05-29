# Configuration file for jupyter-notebook.

#------------------------------------------------------------------------------
# NotebookApp(JupyterApp) configuration
#------------------------------------------------------------------------------

## Hashed password to use for web authentication.
#  
#  To generate, type in a python/IPython shell:
#  
#    from notebook.auth import passwd; passwd()
#  
#  The string should be of the form type:salt:hashed-password.
c.NotebookApp.password = u'sha1:f5ec842e29cc:ba577bafc3ce7609a23b833762cdee1b8f86d523'

## If True, display a button in the dashboard to quit (shutdown the notebook
#  server).
c.NotebookApp.quit_button = False

#------------------------------------------------------------------------------
# MappingKernelManager(MultiKernelManager) configuration
#------------------------------------------------------------------------------

## Whether to consider culling kernels which are busy. Only effective if
#  cull_idle_timeout > 0.
c.MappingKernelManager.cull_busy = True

## Timeout (in seconds) after which a kernel is considered idle and ready to be
#  culled. Values of 0 or lower disable culling. Very short timeouts may result
#  in kernels being culled for users with poor network connections.
c.MappingKernelManager.cull_idle_timeout = 3600

## The interval (in seconds) on which to check for idle kernels exceeding the
#  cull timeout value.
c.MappingKernelManager.cull_interval = 300

## Timeout for giving up on a kernel (in seconds). On starting and restarting
#  kernels, we check whether the kernel is running and responsive by sending
#  kernel_info_requests. This sets the timeout in seconds for how long the kernel
#  can take before being presumed dead. This affects the MappingKernelManager
#  (which handles kernel restarts) and the ZMQChannelsHandler (which handles the
#  startup).
c.MappingKernelManager.kernel_info_timeout = 60
