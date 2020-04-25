import json

def open_file():
    with open('user_case.txt', 'r') as f:
        content = f.read()
        return content
    return ''


def build_model(content):
    return json.loads(content)


if __name__ == '__main__':
    content = open_file()
    dcontent = build_model(content)
    print(type(dcontent))


