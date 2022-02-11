import logging


class Console:

    def log(self, *args):
        """
        Outputs a message to the console
        :param args:
        """
        logging.warning(" ".join(map(str, args)))

    # FIXME: function name
    def _assert(self, *args):
        """
        Writes an error message to the console if a assertion is false
        :param args:
        """
        if args[0] == True:
            logging.error(" ".join(map(str, args[1:])))

    def clear(self):
        """
        Clears the console.
        """
        raise ValueError("not supported")

    def count(self):
        """
        Logs the number of times that this particular call to count() has been called
        """
        raise ValueError("not supported")

    def error(self, *args):
        """
        Outputs an error message to the console
        :param args:
        """
        logging.error(" ".join(map(str, args)))

    def group(self):
        """
        Creates a new inline group in the console. This indents following console messages by an additional level,
        until console.groupEnd() is called
        """
        raise ValueError("not supported")

    def group_collapsed(self):
        """
        Creates a new inline group in the console. However, the new group is created collapsed. The user will need to use the disclosure button to expand it
        """
        raise ValueError("not supported")

    def group_end(self):
        """
        Exits the current inline group in the console
        """
        raise ValueError("not supported")

    def info(self, *args):
        """
        Outputs an informational message to the console
        :param args:
        """
        logging.info(" ".join(map(str, args)))

    def table(self):
        """
        Displays tabular data as a table
        """
        raise ValueError("not supported")

    def time(self):
        """
        Starts a timer (can track how long an operation takes)
        """
        raise ValueError("not supported")

    def time_end(self):
        """
        Stops a timer that was previously started by console.time()
        :return:
        """
        raise ValueError("not supported")

    def trace(self, *args):
        """
        Outputs a stack trace to the console
        :param args:
        """
        logging.info(" ".join(map(str, args)))

    def warn(self, *args):
        """
        Outputs a warning message to the console
        :param args:
        """
        logging.warning(" ".join(map(str, args)))

    def __call__(self, *args):
        pass