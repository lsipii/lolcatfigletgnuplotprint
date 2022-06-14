from typing import List

from printers.utils.dates import get_datetime_now

from .LolcatFigletPrinter import LolcatFigletPrinter
from .PlotPrinter import PlotPrinter
from .utils.types import PlotPrinterValueGroup, PrinterAttachment


def plot_print(
    value_groups: List[PlotPrinterValueGroup], width=75, height=17, output_as_return_value: bool = False
) -> str:
    """
    Prints xy-plot
    """
    return PlotPrinter().print(value_groups, width, height, output_as_return_value)


def lolcat_figlet_print(
    message: str,
    heading_text: str = None,
    description_text: str = None,
    attachements: List[PrinterAttachment] = [],
    priority: int = None,
    output_as_return_value: bool = False,
) -> str:
    """
    Prints texts with a fancy look
    """
    return LolcatFigletPrinter().print(
        message=message,
        heading_text=heading_text,
        description_text=description_text,
        attachements=attachements,
        priority=priority,
        output_as_return_value=output_as_return_value,
    )


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

    timestampNow = get_datetime_now().timestamp()

    message = plot_print(
        value_groups=[
            {
                "title": "Data 1",
                "values": [
                    {"value": 1, "timestamp": timestampNow},
                    {"value": 5, "timestamp": timestampNow + 5},
                    {"value": 2, "timestamp": timestampNow + 15},
                ],
            },
            {
                "title": "Data 2",
                "values": [
                    {"value": 7, "timestamp": timestampNow},
                    {"value": 3, "timestamp": timestampNow + 5},
                    {"value": 5, "timestamp": timestampNow + 15},
                ],
            },
        ],
        output_as_return_value=True,
    )

    lolcat_figlet_print(
        message=message,
        heading_text=heading_text,
        description_text=description_text,
        attachements=attachements,
    )
