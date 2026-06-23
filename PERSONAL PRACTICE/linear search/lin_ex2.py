def is_flagged(comment_words, banned_list):
    for word in comment_words:
        if word in banned_list:
            return True
    return False

