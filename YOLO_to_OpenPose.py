import numpy as np
import json

# Сопоставление индексов суставов COCO и NTU
coco_to_ntu = {
    0: 21,  # нос -> кончик носа
    5: 5,  # левое плечо -> левое плечо
    6: 9,  # правое плечо -> правое плечо
    7: 6,  # левый локоть -> левый локоть
    8: 10,  # правый локоть -> правый локоть
    9: 7,  # левое запястье -> левое запястье
    10: 11,  # правое запястье -> правое запястье
    11: 13,  # левое бедро -> левое бедро
    12: 17,  # правое бедро -> правое бедро
    13: 14,  # левое колено -> левое колено
    14: 18,  # правое колено -> правое колено
    15: 15,  # левая лодыжка -> левая лодыжка
    16: 19  # правая лодыжка -> правая лодыжка
}


def convert_coco_to_ntu(coco_skeleton):
    ntu_skeleton = np.zeros((25, 3))  # NTU skeleton имеет 25 суставов, предполагая 3D координаты
    for coco_idx, ntu_idx in coco_to_ntu.items():
        ntu_skeleton[ntu_idx] = coco_skeleton[coco_idx]
    return ntu_skeleton


def convert_dataset(coco_dataset_path, output_path):
    with open(coco_dataset_path, 'r') as f:
        coco_data = json.load(f)

    ntu_data = []
    for entry in coco_data:
        coco_skeleton = np.array(entry['keypoints']).reshape(-1, 3)
        ntu_skeleton = convert_coco_to_ntu(coco_skeleton)
        ntu_data.append({
            'frame_index': entry['frame_index'],
            'skeleton': ntu_skeleton.tolist()
        })

    with open(output_path, 'w') as f:
        json.dump(ntu_data, f)


# Пример использования
convert_dataset('/mnt/data/coco_skeleton_data.json', '/mnt/data/ntu_skeleton_data.json')
