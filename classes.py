class Television:
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    # the default values
    def __init__(self):
        self.active = False
        self.channel = 0
        self.volume = 0

    # Method to turn the power on and off
    def power(self):
        if self.active == False:
            self.active = True
        else:
            self.active = False

    # Method to turn the channel up
    def channel_up(self):
        if self.active == True:
            if self.channel == 3:
                self.channel = 0
            else:
                self.channel += 1

    # Method to turn the channel down
    def channel_down(self):
        if self.active == True:
            if self.channel == 0:
                self.channel -= 0
            else:
                self.channel -= 1

    # Method to turn the volume up
    def volume_up(self):
        if self.active == True:
            if self.volume == 2:
                self.volume -= 0
            else:
                self.volume += 1

    # Method to turn the volume down
    def volume_down(self):
        if self.active == True:
            if self.volume == 0:
                self.volume -= 0
            else:
                self.volume -= 1

    # Method to print out the status of the TV
    def __str__(self):
        return 'TV status: Is on = {active}, channel= {channel}, volume= {volume} '.format(active=self.active,
                                                                                           channel=self.channel,
                                                                                           volume=self.volume)
