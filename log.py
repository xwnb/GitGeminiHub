import io

class Logger:

    def __init__(self, fout: io.FileIO = None) -> None:
        self.file: io.FileIO = fout

    def log_raw(self, msg: str):
        if self.file:
            self.file.write(msg)
        
        print(msg)

        return msg

    def log_msg(self, msg: str):
        ret = "\n**********************************************************\n"
        ret += str(msg)
        ret += "\n**********************************************************\n"
        return self.log_raw(ret)

    def __log(self, msg: str, level: str="DEBUG"):
        ret = "\n**********************************************************\n"
        ret += "**" + level + " occurs:**\n" + str(msg)
        ret += "\n**********************************************************\n"
        return self.log_raw(ret)

    def log_error(self, msg: str):
        return self.__log(msg, "ERROR")

    def log_warning(self, msg: str):
        return self.__log(msg, "WARNING")

    def log_debug(self, msg: str):
        return self.__log(msg, "DEBUG")

    def log_info(self, msg: str):
        return self.__log(msg, "INFO")