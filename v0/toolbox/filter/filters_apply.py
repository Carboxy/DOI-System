import os
from tqdm import tqdm 

from .util import Time
from .color_filter import color_filter, open_image_np, np_to_pil

ROOT = './filter_x8/'
FILTER_ING_DIR = ROOT + 'filtering'
FILTER_DIR = ROOT + 'filtered_png'
FILTER_MASK_DIR = ROOT + 'filtered_mask'
FILTER_NH_DIR = ROOT + 'filtered_nh_png'
FILTER_MASK_NH_DIR = ROOT + 'filtered_mask_nh'


def apply_color_filter_to_dir(dir, save=True, display=False, hole_size=1000, object_size=600):
    t = Time()
    print("Applying filters to images\n")

    image_list = sorted(os.listdir(dir))
    print('Number of images :  {}'.format(len(image_list)))
    # image_list = ['_20190403091259.png']
    # image_list = [image_list[11], image_list[22]]
    # image_list = ['_20190718215800.svs-080-32x-28662x73872-895x2308.png']

    for item in tqdm(image_list):
        apply_color_filter_to_image(item, dir, save=True, display=False, hole_size=hole_size, object_size=object_size)

    print("Time to apply filters to all images: %s\n" % str(t.elapsed()))


def apply_color_filter_to_image(item_old, item, item_folder, filtered_dir, filted_mask_dir, save=True, display=False, hole_size=1000, object_size=600):
    t = Time()
    print('Processing slide:  {}'.format(item))
    image_path = os.path.join(item_folder, item_old)
    np_orig = open_image_np(image_path)
    item = item.split('.')[0]
    filtered_np_img, filtered_mask, filter_np_img_noholes, filtered_mask_noholes = color_filter(np_orig, item, save_dir=FILTER_ING_DIR, save=False, display=display, hole_size=hole_size, object_size=object_size)
    
    save_suffix = '.png'
    item = item + save_suffix
    if save:
        if not os.path.isdir(filtered_dir):
            os.makedirs(filtered_dir)
        if not os.path.isdir(filted_mask_dir):
            os.makedirs(filted_mask_dir)

        t1 = Time()
        filter_path = os.path.join(filtered_dir, item)
        pil_img = np_to_pil(filtered_np_img)
        pil_img.save(filter_path)
        print("%-20s | Time: %-14s  Name: %s" % ("Save Filtered", str(t1.elapsed()), filter_path))

        t1 = Time()
        mask_path = os.path.join(filted_mask_dir, item)
        pil_mask = np_to_pil(filtered_mask)
        pil_mask.save(mask_path)
        print("%-20s | Time: %-14s  Name: %s" % ("Save Mask", str(t1.elapsed()), mask_path))



if __name__ == '__main__':
    src_dir = './scaledown8_png/'
    hole_size = 2000
    object_size = 3000
    apply_color_filter_to_dir(src_dir, hole_size=hole_size, object_size=object_size)