def show(self, file):
    logger.info("Calling the show method.")
    with open(file, "r") as f:
        content = json.loads(f.read())
        return content