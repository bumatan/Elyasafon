import connection_controller
import project_types

class device_manager(object):
    def __init__(self):
        self.connections = dict()

        for connection_type in project_types.connection_types:
            self.connections[connection_type] = connection_controller.connection_controller(project_types.connection_enable[connection_type], project_types.connection_pins[connection_type])

    def connect(self, connection_type, index):
        self.connections[connection_type].connect(index)

    def release(self, connection_type):
        self.connections[connection_type].release()