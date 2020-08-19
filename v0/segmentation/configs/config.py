config_django = {
    'n_class': 4,
    'img_path': "v0/segmentation/OSCC-Tile/5x_1600/val_1600/",
    'mask_path': "v0/segmentation/OSCC-Tile/5x_1600/val_masl_1600/",
    'meta_path' :"v0/segmentation/OSCC-Tile/5x_1600/tile_info_val_1600.json",
    'log_path' :"v0/segmentation/results/logs/",
    'output_path' :"IMAGES/Masks/",
    'ckpt_path' :"v0/segmentation/unet-resnet34-dan-1e-4-adam-cos-sce-7.15-74-0.8582.pth",
    'batch_size': 1,
    'num_workers': 2,
}

config = {
    'n_class': 4,
    'img_path': "segmentation/OSCC-Tile/5x_1600/val_1600/",
    'mask_path': "segmentation/OSCC-Tile/5x_1600/val_masl_1600/",
    'meta_path' :"segmentation/OSCC-Tile/5x_1600/tile_info_val_1600.json",
    'log_path' :"segmentation/results/logs/",
    'output_path' :"../IMAGES/Masks/",
    'ckpt_path' :"segmentation/unet-resnet34-dan-1e-4-adam-cos-sce-7.15-74-0.8582.pth",
    'batch_size': 1,
    'num_workers': 2,
}
