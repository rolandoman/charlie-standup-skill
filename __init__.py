from mycroft import MycroftSkill, intent_file_handler
import serial
# This will be crazy fun

class CharlieStandup(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('standup.charlie.intent')
    def handle_standup_charlie(self, message):
        self.speak_dialog('standup.charlie')


def create_skill():
    return CharlieStandup()

