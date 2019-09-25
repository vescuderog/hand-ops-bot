class Command:

    def __init__(self):
        self.commands = {
            '> build': self.deploy,
            '> help': self.help
        }

    def handle_command(self, user, command):
        response = '<@' + user + '>: '

        if command in self.commands:
            response += self.commands[command]()
        else:
            response += "Sorry I don't understand the command:\n*" + command + "* " + self.help()

        return response

    def deploy(self):
        return 'Building new version...'

    def help(self):
        response = 'Currently I support the following commands:\r\n'

        for command in self.commands:
            response += command + '\r\n'

        return response
