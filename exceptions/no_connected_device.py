class NoConnectedDeviceException(Exception):
    """
    NoConnectedDeviceException class.

    Exception raised when trying to disconnect a connected device from a projector
    when the projector has no connected devices.
    """
    def __init__(self, message="Trying to disconnect a connected device from a projector\
    when the projector has no connected devices"):
        self.message = message
        super().__init__(self.message)
