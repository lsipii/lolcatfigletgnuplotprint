from typing import List
import sh
import random
from shutil import which
from PlotPrinter import PlotPrinter

from utils.CommandlinePrinter import CommandlinePrinter
from utils.data_structures import singleton
from utils.strings import chunk_string_by_length
from utils.types import PrinterAttachment


@singleton
class LolcatFigletPrinter:
    def __init__(self):
        self.shell_apps = self.___initiailize_shell_apps()
        self.printer = CommandlinePrinter()

    def print(
        self,
        message: str,
        heading_text: str = None,
        description_text: str = None,
        attachements: List[PrinterAttachment] = [],
        priority: int = None,
    ):
        #
        # Clear previous view
        #
        self.printer.clear_screen()

        #
        # Print heading text
        #
        self.___print_heading_text(heading_text=heading_text, priority=priority)

        #
        # Print description text
        #
        self.___print_description_text(description_text=description_text)
        #
        # Print attachments
        #
        self.___print_attachments(attachements=attachements)

        #
        # Print the message
        #
        if message is not None:
            self.printer.print(message)

        # Print some new lines for end margin
        self.printer.print("\n" * 2)

    def ___print_heading_text(self, heading_text: str = None, priority: int = None):
        if heading_text is not None:

            # Print some new lines for top margin
            self.printer.print("\n" * 6)

            if "figlet" in self.shell_apps:
                heading_output = sh.figlet("-ctf", "slant", heading_text)
            else:
                heading_output = str(heading_text).center(50)

            if "lolcat" in self.shell_apps:
                heading_output = sh.lolcat(heading_output)

            #
            # Print the lolcat figlet message
            #
            if "lolcat" not in self.shell_apps:
                output_text = str(heading_output)
                if priority is None or priority > 0:
                    figlet_colours = ["aqua", "green", "magenta", "yellow"]
                    figlet_colour = random.choice(figlet_colours)
                else:
                    figlet_colour = "grey"
                self.printer.print(text=output_text, inline=False, colour=figlet_colour)
            else:
                self.printer.print(heading_output)

    def ___print_description_text(self, description_text: str = None):
        if description_text is not None:
            description_output = description_text.center(50)
            self.printer.print(text=description_output, inline=True, colour="white")
            self.printer.print("\n")  # 2x new line

    def ___print_attachments(self, attachements: List[PrinterAttachment] = []):
        if len(attachements) > 0:

            # The first and new messages colour
            firstMessageColour = "green"
            priorityMessageColour = "magenta"
            # The colours of later on messages
            colours = ["yellow", "white", "grey"]

            coloursLength = len(colours) - 1
            colourIndex = 0
            indent = "	  "

            for responseIndex, responseMessage in enumerate(attachements):
                text_is_bold = False
                text_is_underlined = False

                # Set message block colour
                if "isPriority" in responseMessage and responseMessage["isPriority"]:
                    messageColour = priorityMessageColour
                    text_is_bold = True
                    text_is_underlined = True
                elif responseIndex == 0:
                    messageColour = firstMessageColour
                else:
                    messageColour = colours[colourIndex]
                    if colourIndex < coloursLength:
                        colourIndex = colourIndex + 1

                # Print message parts in chunks divided by length
                messageChunks = chunk_string_by_length(message=responseMessage["message"], length=53)
                for messageChunkIndex, messagePart in enumerate(messageChunks):

                    if messageChunkIndex == 0:
                        # Print sender
                        # .. some indent
                        self.printer.print(indent, end=" ")
                        # Coloured message part
                        if "senderName" in responseMessage:
                            self.printer.print(text=responseMessage["senderName"] + " ", inline=True, colour="aqua")
                        # Coloured message part
                        self.printer.print(
                            text=messagePart,
                            inline=False,
                            colour=messageColour,
                            is_bold=text_is_bold,
                            is_underlined=text_is_underlined,
                        )
                    else:
                        # Coloured message part
                        self.printer.print(text=indent + " " + messagePart, inline=False, colour=messageColour)

                # 1x new line
                self.printer.print("")

    def ___initiailize_shell_apps(self):
        shell_apps = []
        for app_name in ["lolcat", "figlet"]:
            app_path = which(app_name)
            if app_path is not None:
                shell_apps.append(app_name)
        return shell_apps


if __name__ == "__main__":
    heading_text = "Heading text"
    description_text = "Description text"
    attachements = [
        {"message": "attachment one"},
        {"message": "attachment two"},
        {"message": "attachment three, a priority message", "isPriority": True},
        {"message": "attachment four"},
        {"message": "attachment five"},
        {"message": "attachment six"},
    ]

    message = PlotPrinter().printPlot(
        values=[
            {"value": 1, "timestamp": 1655146582},
            {"value": 5, "timestamp": 1655146583},
            {"value": 9, "timestamp": 1655146584},
        ],
        output_as_return_value=True,
    )

    LolcatFigletPrinter().print(
        message=message,
        heading_text=heading_text,
        description_text=description_text,
        attachements=attachements,
    )
