# pip install rembg[gpu]
import os

from rembg import remove
from rembg.session_factory import new_session
from PIL import Image
from pathlib import Path


def remove_bg():
    list_of_extensions = ['*.png', '*.jpg', '*.jpeg']
    all_files = []
    
    for ext in list_of_extensions:
        all_files.extend(Path('./input_imgs').glob(ext))

    for index, item in enumerate(all_files):
        input_path = Path(item)
        file_name = input_path.stem

        directory = os.path.dirname("./output_imgs/")
        if not os.path.exists(directory):
            os.makedirs(directory)

        output_path = f'{directory}/{file_name}_output.png'
        output_path_hs = f'{directory}/{file_name}_output_human_seg.png'

        input_img = Image.open(input_path)

        output_img = remove(data=input_img)
        output_img.save(output_path)
        print(f'Completed: {index + 1}/{len(all_files)}')

        output_img = remove(data=input_img, session=new_session("u2net_human_seg"))
        output_img.save(output_path_hs)
        print(f'Completed_hs: {index + 1}/{len(all_files)}')


def main():
    remove_bg()
    
    
if __name__ == '__main__':
    main()
