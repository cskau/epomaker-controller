from .EpomakerCommand import EpomakerCommand
from .reports.Report import Report

class EpomakerKeyMapCommand(EpomakerCommand):
    """"""  # TODO

    def __init__(self, page: int, key_bytes: str) -> None:
        command = 0x0C
        check_sum = 0xFF - (command + 0x80 + 0x01 + page)
        initialization_data = (
            f"{command:02x}008001{page:02x}0000{check_sum:02x}"
            + key_bytes
        )
        initial_report = Report(initialization_data, index=0, checksum_index=None)
        super().__init__(initial_report)