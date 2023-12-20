def justify_paragraph(paragraph, width):
    if paragraph is None:
        raise ValueError("Input paragraph string cannot be empty.")
    words = paragraph.split()
    result = []
    current_line = [words[0]]
    current_width = len(words[0])

    for word in words[1:]:
        if current_width + len(word) + 1 <= width:  # 1 is for the space between words
            current_line.append(word)
            current_width += len(word) + 1
        else:
            result.append(' '.join(current_line).ljust(width))
            current_line = [word]
            current_width = len(word)

    result.append(' '.join(current_line).ljust(width))
    return result