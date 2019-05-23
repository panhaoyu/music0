import os
import json
import eyed3.mp3


def get_files():
    result = list()
    for storage in ('music1', 'music2'):
        for dir_name, sub_dirs, files in os.walk(storage):
            for file in files:
                _, extension = os.path.splitext(file)
                if extension in ('.mp3',):
                    result.append(os.path.join(dir_name, file))
    return result


def get_meta(file_path):
    file = eyed3.mp3.Mp3AudioFile(path=file_path)
    dir_name, file_name = os.path.split(file_path)
    dir_name = os.path.split(dir_name)[1]
    return {
        'title': file.tag.title,
        'artist': file.tag.artist.split('.'),
        'file': file_name,
        'storage': dir_name,
    }


def main():
    result = [get_meta(file) for file in get_files()]
    for i in result:
        print(i['artist'])
    with open('index.json', mode='w', encoding='utf-8') as file:
        json.dump(result, file)
    input('Done.')


if __name__ == '__main__':
    main()
