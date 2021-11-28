import Generator
from data_base.parser.parser import MagnitDisasembler

if __name__ == "__main__":
    datainfo = Generator("sqlite:/// bd_from_magnit")
    disassembler = MagnitDisasembler("https://magnit.ru/promo/", datainfo)
    disassembler.run()