import hackhub

def next_message():
    FILENAME="msgs.txt"
    msg = ''
    lines = []
    with open(FILENAME, 'rw') as f:
        lines = f.readlines()
    msg = lines[0]
    lines = lines[1:] + [lines[0]] # rotate
    with open(FILENAME, 'w') as f:
        f.writelines(lines)
    return msg


def close_space():
    current  = hackhub.Status()
    print "Open condition:", current.status['open']
    if current.status['open']:
        print "Updating status..."
        hackhub.new_status(0, next_message(), 'hackhub')
        print "Done."

if __name__=="__main__":
    close_space()
