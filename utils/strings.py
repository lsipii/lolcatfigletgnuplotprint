def chunk_string_by_length(message: str, length: int):
    """
    Splits the message to length size of chunks
    http://stackoverflow.com/a/9475270
    """
    chunks = []
    message = message.replace("\n", " ")
    while message:
        chunks.append(message[:length])
        message = message[length:]
    return chunks


def ensurePrefix(text: str, prefix: str) -> str:
    if not text.startswith(prefix):
        return f"{prefix}{text}"
    return text


def ensurePostfix(text: str, postfix: str) -> str:
    if not text.endswith(postfix):
        return f"{text}{postfix}"
    return text
